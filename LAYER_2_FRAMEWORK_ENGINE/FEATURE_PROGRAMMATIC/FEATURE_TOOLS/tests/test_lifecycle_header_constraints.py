from ATOM_LIFECYCLE.header_constraints import compile_header_constraints, load_header_constraints


def test_explicit_properties_selectors_and_literal_domains_only():
    body = '''## Claim
### Formal Claim
```CFEL
Atom.Header.Tier{::1}:: [int]{::1};
Atom/(.Header.Role: Concern).Header.Priority{::1}:: [string]{::1};
Atom/(.Header.Role: Concern).Header.Priority: High;
Atom.Header.Mode:: [in (One, Two)]{::1};
Atom.Header.Optional:: [string]{::1};
Atom.Header.Container.*[in(atom,scope_unit)]{::1};
Atom.Header.Topics.*[in(Main Subject, Dependencies)]{::1..2};
```
'''
    records = compile_header_constraints([{'id': 'CA-R-1', '_content_bytes': body.encode()}])
    schema = load_header_constraints(records, {'CA-R-1'})
    assert {r['path'] for r in records} == {'tier', 'priority', 'mode', 'container', 'topics'}
    assert {field for field, _, _ in schema.validate({'role': 'Concern', 'mode': 'Other'})} == {'tier', 'priority', 'mode'}
    assert schema.validate({'role': 'Concern', 'tier': 1, 'priority': 'Unknown'})[0][2] == {'High'}
    assert schema.validate({'role': 'Plan', 'tier': 1, 'mode': 'One'}) == []
    assert schema.validate({'tier': 1, 'topics': {'main_subject': 'Atom'}}) == []
    assert {field for field, _, _ in schema.validate({'tier': 1, 'topics': {}, 'container': {'other': 'X'}})} == {'topics', 'container'}


def test_grouped_model_paths_resolve_flat_and_nested_carriers():
    body = '''## Claim
### Formal Claim
```CFEL
Atom.Header.Identity.ID{::1} :: [string]{::1};
Atom.Header.Identity.Ref ID{::1} :: [string]{::1};
Atom.Header.Context.Role{::1} :: [string]{::1};
Atom.Header.State.Status{::1} :: [string]{::1};
Atom.Header.State.Version{::1} :: [int]{::1};
Atom.Header.State.Updated At{::1} :: [string]{::1};
Atom/(.Header.Context.Role in (Method)).Header.Context.Form{::1} :: [string]{::1};
Atom/(.Header.Context.Role in (Concern)).Header.Context.Concern.Priority{::1} :: [string]{::1};
Atom/(.Header.Context.Role in (Concern)).Header.Context.Concern.Priority :: High;
Atom/(.Header.Context.Role in (Concern)).Header.Context.Concern.Priority :: Medium;
Atom.Header.Context.Role :: Method;
Atom.Header.Relations.*[in(uses)]{::1};
```
'''
    records = compile_header_constraints([{'id': 'CA-R-1', '_content_bytes': body.encode()}])
    schema = load_header_constraints(records, {'CA-R-1'})
    assert {r['path'] for r in records} == {'atom_id', 'ref_id', 'role', 'status', 'version', 'updated_at',
                                            'form', 'priority', 'relations'}
    assert {r['value'] for r in records if r['kind'] == 'domain'} == {'High', 'Medium'}
    flat = {'atom_id': 'CA-M-1', 'ref_id': 'CA-M-1', 'role': 'method', 'status': 'Draft',
            'version': 1, 'updated_at': 'now', 'form': 'solution', 'relations': {'uses': []}}
    nested = {'identity': {'id': 'CA-M-1', 'ref_id': 'CA-M-1'},
              'context': {'role': 'method', 'form': 'solution'},
              'state': {'status': 'Draft', 'version': 1, 'updated_at': 'now'}, 'relations': {'uses': []},
              'role': 'method'}
    assert schema.validate(flat) == []
    assert schema.validate(nested) == []
    metadata = {key: value for key, value in nested.items() if key != 'role'}
    logical = {**nested, 'role': 'Method', 'form': 'Solution'}
    assert schema.validate(logical, metadata=metadata) == []
    concern = {**logical, 'role': 'Concern'}
    concern_metadata = {**metadata, 'context': {'role': 'concern', 'form': 'problem', 'concern': {'priority': 'Urgent'}}}
    assert schema.validate(concern, metadata=concern_metadata)[0][2] == {'High', 'Medium'}
    del flat['form']
    assert [error[0] for error in schema.validate(flat)] == ['form']
    del nested['state']['version']
    assert [error[0] for error in schema.validate(nested)] == ['version']


def test_required_groups_accept_equivalent_flat_carriers():
    body = '''## Claim
### Formal Claim
```CFEL
Atom.Header.Identity{::1} :: []{::0};
Atom.Header.Identity.*[in (ID, Ref ID)]{::2};
Atom.Header.Context{::1} :: []{::0};
Atom.Header.Context.*[in (Container, Role, Form, Label, Topics, Tier, Plan, Concern)]{::5..7};
Atom.Header.State{::1} :: []{::0};
Atom.Header.State.*[in (Status, Version, Updated At)]{::3};
Atom/(.Header.Context.Role in (Concern)).Header.Context.Concern{::1} :: []{::0};
Atom/(.Header.Context.Role in (Concern)).Header.Context.Concern.*[in (Priority)]{::1};
```
'''
    schema = load_header_constraints(
        compile_header_constraints([{'id': 'CA-R-1', '_content_bytes': body.encode()}]), {'CA-R-1'},
    )
    identity = {'id': 'CA-C-1', 'ref_id': 'CA-C-1'}
    context = {'container': {'scope_unit': 'CA-SU-00'}, 'role': 'concern', 'form': 'problem',
               'topics': {'main_subject': 'Atom'}, 'tier': 1}
    state = {'status': 'active', 'version': 1, 'updated_at': 'now'}
    flat = {**identity, **context, **state, 'atom_id': identity['id'], 'priority': 'High'}
    grouped = {'identity': identity, 'context': {**context, 'concern': {'priority': 'High'}}, 'state': state}
    assert schema.validate(flat) == []
    assert schema.validate({'role': 'Concern'}, metadata=grouped) == []
    assert schema.validate({'role': 'Concern'}, metadata={**grouped, 'identity': {**identity, 'extra': 'X'}})
    missing = schema.validate({key: value for key, value in flat.items() if key != 'priority'})
    assert {field for field, _, _ in missing} == {'priority'}
