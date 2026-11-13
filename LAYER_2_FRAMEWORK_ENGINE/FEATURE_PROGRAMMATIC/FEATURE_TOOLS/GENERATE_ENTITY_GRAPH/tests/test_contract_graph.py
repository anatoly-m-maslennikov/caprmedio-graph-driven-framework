"""Formal-contract graph preserves complete, source-bound Claim evidence."""

from pathlib import Path
import sys
import unittest


TOOL = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOL.parent), str(TOOL)]

from contract_graph import compose_contract_graph, render_contract_graph  # noqa: E402
from cfel_claim_constraints import extract_claim_constraints  # noqa: E402
from subject_projection_data import _formal_claims  # noqa: E402
from subject_projection_views import _claims, _cfel  # noqa: E402


def carrier(atom_id, active, body, *, role="Requirement", form="Declaration"):
    return {
        "source": {"atom_id": atom_id, "version": 1, "path": f"sources/{atom_id}.md"},
        "subjects": {"active": active, "passive": []}, "body": body,
        "read_view": {"content_role": role, "type": form},
    }


def body(*claim_lines, semantics=None):
    result = "## Claim\n\n" + "\n".join(claim_lines) + "\n"
    if semantics is not None:
        result += "\n## Semantics\n\n" + semantics + "\n"
    return result


class ContractGraphTests(unittest.TestCase):
    def test_content_recursion_is_general_and_ordering_is_rmed_only(self):
        from subject_projection_data import build_subject_projection_data

        roles = ("Requirement", "Method", "Evaluation", "Delivery")
        atom = carrier("CA-R-1", "Atom", body("```CFEL", "Atom;", "```"))
        role_rows = [carrier(f"CA-R-{index}", f"Atom/(.Header.Context.Role:={name})", body(
            "### Formal Claim", "```python", "from caprmedio.formal_claims import declare_entity",
            "from caprmedio.model import Atom", f"class {name}(Atom):", "    pass",
            f"declare_entity(entity_class={name}, entity_name='{name}', qualification_property_path='Atom.Header.Context.Role')", "```"))
            for index, name in enumerate((*roles, "Analysis"), start=2)]
        legacy_prefix = "Atom/(.Header.Context.Role in RMED).Content"
        legacy = body("```CFEL", "Atom.Content{::1} :: []{::0};", "Atom.Content.*[string]{::0+};",
                      "Atom.Content.**[string]{::0+};", "Atom.Content.**:: [markdown];",
                      f"{legacy_prefix}.Summary ;> {legacy_prefix}.Claim;",
                      f"{legacy_prefix}.Semantics <; {legacy_prefix}.Claim;",
                      f"{legacy_prefix}.Semantics ;> {legacy_prefix}.Details", "```")
        native = body("### Formal Claim", "```python", "from caprmedio.formal_claims import Cardinality, declare_entity",
                      "from caprmedio.model import Requirement, Method, Evaluation, Delivery",
                      "declare_entity(entity_name='Content', relation_name='IS_PROPERTY_OF', base_path='Atom',",
                      "  property_occurrence_cardinality=1, value_cardinality=0,",
                      "  dependent_property_cardinality=Cardinality(minimum=0, maximum=None), dependent_property_name_format=str,",
                      "  recursive_dependent_property_cardinality=Cardinality(minimum=0, maximum=None),",
                      "  recursive_dependent_property_name_format=str, recursive_dependent_property_value_format='markdown',",
                      "  ordered_dependent_property_roles=(Requirement, Method, Evaluation, Delivery),",
                      "  ordered_dependent_property_pairs=(('Summary', 'Claim'), ('Claim', 'Semantics'), ('Semantics', 'Details')))",
                      "```")
        extra = carrier("CA-R-8", "Atom.Content.Extra.Nested", body("```CFEL", "Atom.Content.Extra.Nested{::1}:", "```"))
        for claim in (legacy, native):
            projection = build_subject_projection_data([atom, *role_rows, carrier("CA-R-7", "Atom.Content", claim), extra])
            entries = projection["declarations"]["properties"]["Atom.Content"]
            self.assertFalse(entries[0]["diagnostics"])
            for name in (*roles, "Analysis"):
                entity = next(row for row in projection["entities"] if row["identity"].endswith(f":={name})"))
                props = {item["identity"]: item for item in entity["inherited_properties"]}
                self.assertEqual("markdown", props["Atom.Content.Extra.Nested"]["effective_value_format"])
                contracts = props["Atom.Content"]["contracts"]
                self.assertTrue(any(c.get("selection") == "recursive_dependents" for c in contracts))
                pairs = [(c["source_selector"].rsplit(".", 1)[1], c["target_selector"].rsplit(".", 1)[1])
                         for c in contracts if c.get("relation") == "IS_ORDERED_RIGHT_BEFORE"]
                self.assertEqual([("Summary", "Claim"), ("Claim", "Semantics"), ("Semantics", "Details")]
                                 if name in roles else [], pairs)

    def test_native_dependent_counts_match_legacy_claim(self):
        address = "Atom.Header.Relations"
        legacy = body("```CFEL", f"{address}{{::0..1}} :: []{{::0}};",
                      f"{address}.*[string]{{::1+}};", f"{address}.* :: [string]{{::1+}}", "```")
        native = body(
            "### Formal Claim", "```python", "from caprmedio.formal_claims import declare_entity",
            "from caprmedio.formal_claims import Cardinality",
            "declare_entity(entity_name='Relations', relation_name='IS_PROPERTY_OF', base_path='Atom.Header',",
            "  property_occurrence_cardinality=Cardinality(minimum=0, maximum=1), value_cardinality=0,",
            "  dependent_property_cardinality=Cardinality(minimum=1, maximum=None), dependent_property_name_format=str,",
            "  dependent_property_value_format=str,",
            "  dependent_property_value_cardinality=Cardinality(minimum=1, maximum=None))", "```")

        def contracts(claim):
            atom = carrier("CA-R-1", address, claim)
            graph = compose_contract_graph([atom])
            entry, = next(row for row in graph["entities"] if row["target"] == address)["own"]
            self.assertFalse(entry["diagnostics"])

            def format_name(value):
                return "string" if value == "str" else value or None

            return {
                clause["selection"]: (format_name(clause.get("name_format")),
                                      clause.get("occurrence_cardinality"),
                                      format_name(clause.get("value_format")), clause.get("value_cardinality"))
                for clause in entry["clauses"] if clause["kind"] == "property_constraint"
            }

        expected = contracts(legacy)
        self.assertEqual({"property", "immediate_dependents", "immediate_dependent_values"}, expected.keys())
        self.assertEqual(expected, contracts(native))

    def test_native_order_keeps_property_scope_and_source(self):
        from subject_projection_data import build_subject_projection_data

        atom = carrier("CA-R-1", "Atom", body("```CFEL", "Atom;", "```"))
        claim = carrier("CA-R-2", "Atom.Content.Claim", body(
            "### Formal Claim", "```python", "from caprmedio.formal_claims import declare_entity",
            "from caprmedio.model import Requirement, Method, Evaluation, Delivery",
            "declare_entity(entity_name='Claim', relation_name='IS_PROPERTY_OF', base_path='Atom.Content',",
            "  dependent_property_cardinality=2, allowed_dependent_property_names=('Prose Claim', 'Formal Claim'),",
            "  ordered_dependent_property_pairs=(('Prose Claim', 'Formal Claim'),),",
            "  applies_to_entity_classes=(Requirement, Method, Evaluation, Delivery))", "```"))
        graph = compose_contract_graph([atom, claim])
        prop = next(node for node in graph["entities"] if node["target"] == "Atom.Content.Claim")
        order, = [clause for clause in prop["own"][0]["clauses"]
                  if clause.get("relation") == "IS_ORDERED_RIGHT_BEFORE"]
        self.assertEqual("relation_cardinality", order["kind"])
        self.assertEqual("Atom.Content.Claim", order["bearer"])
        self.assertEqual(("Atom.Content.Claim.Prose Claim", "Atom.Content.Claim.Formal Claim"),
                         (order["source_selector"], order["target_selector"]))
        self.assertEqual(("Requirement", "Method", "Evaluation", "Delivery"), order["applicable_entity_classes"])
        self.assertEqual("CA-R-2", order["source"]["atom_id"])
        role = carrier("CA-R-3", "Atom/(.Header.Context.Role:=Requirement)", body(
            "### Formal Claim", "```python", "from caprmedio.formal_claims import declare_entity",
            "from caprmedio.model import Atom", "class Requirement(Atom):", "    pass",
            "declare_entity(entity_class=Requirement, entity_name='Requirement', qualification_property_path='Atom.Header.Context.Role')", "```"))
        projection = build_subject_projection_data([atom, claim, role])
        base = next(row for row in projection["entities"] if row["identity"] == "Atom")
        self.assertNotIn("Atom.Content.Claim", [row["identity"] for row in base["direct_properties"]])
        entity = next(row for row in projection["entities"] if row["identity"] == "Atom/(.Header.Context.Role:=Requirement)")
        projected = next(row for row in entity["inherited_properties"] if row["identity"] == "Atom.Content.Claim")
        self.assertIn(order, projected["contracts"])

    def test_native_property_uses_explicit_bearer_and_preserves_written_subject(self):
        step = "Atom/(.Header.Context.Role:=Operations)/Step"
        topic = "CAPRMEDIO_MODEL <+ Step.Kind"
        declarations = [
            carrier("CA-R-1", step, body("```CFEL", f"{step};", "```")),
            carrier("CA-R-2", "Other/Step", body("```CFEL", "Other/Step;", "```")),
            carrier("CA-R-3", topic, body(
                "### Formal Claim", "```python", "from caprmedio.formal_claims import declare_entity",
                f"declare_entity(entity_name='Kind', relation_name='IS_PROPERTY_OF', base_path={step!r})",
                "```")),
        ]
        graph = compose_contract_graph(declarations)
        node, = [row for row in graph["entities"] if row["target"] == f"{step}.Kind"]
        entry, = node["own"]
        self.assertEqual(topic, entry["subject"])
        self.assertEqual("CA-R-3", entry["source"]["atom_id"])
        self.assertEqual("native_property_base_path", entry["binding"])
        self.assertFalse(any(row["target"] in {"Step.Kind", "Other/Step.Kind"} for row in graph["entities"]))

    def test_native_nested_bearers_resolve_independently_of_source_order(self):
        def property_declaration(atom_id, subject, base, name):
            return carrier(atom_id, subject, body(
                "### Formal Claim", "```python", "from caprmedio.formal_claims import declare_entity",
                f"declare_entity(entity_name={name!r}, relation_name='IS_PROPERTY_OF', base_path={base!r})",
                "```"))

        declarations = [
            carrier("CA-R-1", "Atom", body("```CFEL", "Atom;", "```")),
            property_declaration("CA-R-2", "Short.Header", "Atom", "Header"),
            property_declaration("CA-R-3", "Header.Context", "Atom.Header", "Context"),
            property_declaration("CA-R-4", "Context.Role", "Atom.Header.Context", "Role"),
        ]
        for rows in (declarations, list(reversed(declarations))):
            graph = compose_contract_graph(rows)
            targets = {entry["source"]["atom_id"]: node["target"]
                       for node in graph["entities"] for entry in node["own"]}
            self.assertEqual("Atom.Header.Context.Role", targets["CA-R-4"])

    def test_native_python_class_inheritance_and_relation_metadata(self):
        from current_subject_graph import compose_narrowing_graph

        root = carrier("CA-R-1", "Atom", body("```CFEL", "Atom;", "```"))
        method = carrier("CA-R-2", "Atom/(.Header.Context.Role := Method)", body(
            "### Formal Claim", "```python", "from caprmedio.formal_claims import declare_entity",
            "from caprmedio.model import Atom", "class Method(Atom):", "    pass",
            "declare_entity(entity_class=Method, entity_name='Method', qualification_property_path='Atom.Header.Context.Role')",
            "```"))
        tree, _ = compose_narrowing_graph([root, method])
        identities = {node["id"]: node["identity"] for node in tree["nodes"]}
        self.assertIn(("Atom/(.Header.Context.Role:=Method)", "Atom"),
                      {(identities[edge["relation_source"]], identities[edge["relation_target"]])
                       for edge in tree["edges"]})
        relation = carrier("CA-R-3", "Relation//CARRIES", body(
            "### Formal Claim", "```python", "from caprmedio.formal_claims import declare_relation",
            "declare_relation(relation_name='CARRIES', source_endpoint={'level': 'instances', 'entity_paths': ('Carrier',)}, target_endpoint={'level': 'instances'}, inverse_alias='IS_CARRIED_BY', written_alias='>>')",
            "```"))
        clauses, diagnostics = extract_claim_constraints(relation)
        self.assertEqual([], diagnostics)
        self.assertEqual(2, sum(row["kind"] == "relation_endpoint" for row in clauses))
        self.assertTrue(any(row.get("relation") == "HAS_INVERSE" for row in clauses))
        self.assertTrue(any(row.get("glyph") == ">>" for row in clauses))

    def test_native_direct_relation_preserves_the_legacy_inverse_view(self):
        direct = carrier("CA-R-1", "Relation//CARRIES", body(
            "### Formal Claim", "```python", "from caprmedio.formal_claims import declare_relation",
            "declare_relation(relation_name='CARRIES', source_endpoint={'level': 'instances', 'entity_paths': ('Carrier',)},",
            "                 target_endpoint={'level': 'instances', 'ephemeral': False},",
            "                 inverse_alias='IS_CARRIED_BY', targets_per_source=1)", "```",
            "### Prose Claim", "The Carrier represents the object."))
        inverse = carrier("CA-R-2", "Relation//IS_CARRIED_BY", body(
            "### Formal Claim", "```CFEL", "Relation//IS_CARRIED_BY <((HAS_INVERSE)) Relation//CARRIES", "```"))
        graph = compose_contract_graph([direct, inverse])
        view = next(row["derived_view"] for row in graph["relations"] if row["target"] == "IS_CARRIED_BY")
        endpoint, = view["endpoints"]
        self.assertEqual({"level": "instances", "ephemeral": False}, endpoint["host"])
        self.assertEqual(("Carrier",), endpoint["target"]["entity_paths"])
        self.assertEqual({"minimum": 1, "maximum": 1}, endpoint["sources_per_target"])
        self.assertEqual([], graph["missing_relation_semantics"])
        direct_row = next(row for row in graph["relations"] if row["target"] == "CARRIES")
        self.assertNotIn("derived_aliases", direct_row)

    def test_native_inverse_without_separate_declaration_keeps_source_and_bounds(self):
        direct = carrier("CA-R-1", "Relation//CARRIES", body(
            "### Formal Claim", "```python",
            "from caprmedio.formal_claims import Cardinality, declare_relation",
            "declare_relation(relation_name='CARRIES',",
            "  source_endpoint={'level': 'instances', 'entity_paths': ('Carrier',)},",
            "  target_endpoint={'level': 'instances', 'entity_paths': ('Atom',)},",
            "  inverse_alias='IS_CARRIED_BY',",
            "  targets_per_source=Cardinality(minimum=2, maximum=3),",
            "  sources_per_target=Cardinality(minimum=1, maximum=5))",
            "```", semantics="The Carrier represents the object."))
        graph = compose_contract_graph([direct])
        self.assertEqual(["CARRIES"], [row["target"] for row in graph["relations"]])
        direct_row = graph["relations"][0]
        alias, = direct_row["derived_aliases"]
        self.assertEqual(("IS_CARRIED_BY", "Derived", "CARRIES"),
                         (alias["name"], alias["classification"], alias["direct_relation"]))
        self.assertEqual("CA-R-1", alias["source"]["atom_id"])
        endpoint, = alias["endpoints"]
        self.assertEqual(("Atom",), endpoint["host"]["entity_paths"])
        self.assertEqual(("Carrier",), endpoint["target"]["entity_paths"])
        self.assertEqual({"minimum": 1, "maximum": 5}, endpoint["targets_per_source"])
        self.assertEqual({"minimum": 2, "maximum": 3}, endpoint["sources_per_target"])
        self.assertEqual(2, len(direct_row["host_target"]))
        self.assertIn("Derived Relation `((IS_CARRIED_BY))`", render_contract_graph(graph))

    def test_ambiguous_native_inverse_does_not_create_a_derived_view(self):
        def direct(atom_id, name):
            return carrier(atom_id, "Relation//" + name, body(
                "### Formal Claim", "```python",
                "from caprmedio.formal_claims import declare_relation",
                f"declare_relation(relation_name='{name}', source_endpoint={{'level':'instances'}},",
                "  target_endpoint={'level':'instances'}, inverse_alias='SHARED')",
                "```", semantics="Direct meaning."))
        graph = compose_contract_graph([direct("CA-R-1", "FIRST"), direct("CA-R-2", "SECOND")])
        self.assertTrue(all("derived_aliases" not in row for row in graph["relations"]))
        declared = carrier("CA-R-3", "Relation//SHARED", body("### Prose Claim", "Other meaning."))
        graph = compose_contract_graph([direct("CA-R-1", "FIRST"), declared])
        self.assertTrue(all("derived_aliases" not in row for row in graph["relations"]))

    def test_native_forms_with_same_local_class_name_keep_distinct_parents(self):
        from current_subject_graph import compose_narrowing_graph

        root = carrier("CA-R-1", "Atom", body("```CFEL", "Atom;", "```"))
        carriers = [root]
        for index, role in enumerate(("Method", "Evaluation"), 2):
            parent = f"Atom/(.Header.Context.Role := {role})"
            carriers.append(carrier(f"CA-R-{index}", parent, body(
                "### Formal Claim", "```python", "from caprmedio.formal_claims import declare_entity",
                "from caprmedio.model import Atom", f"class {role}(Atom):", "    pass",
                f"declare_entity(entity_class={role}, entity_name='{role}')", "```")))
            carriers.append(carrier(f"CA-R-{index + 10}", parent + "/(.Header.Context.Form := Decision)", body(
                "### Formal Claim", "```python", "from caprmedio.formal_claims import declare_entity",
                f"from caprmedio.model import {role}", f"class Decision({role}):", "    pass",
                "declare_entity(entity_class=Decision, entity_name='Decision')", "```")))
        tree, _ = compose_narrowing_graph(carriers)
        identities = {node["id"]: node["identity"] for node in tree["nodes"]}
        edges = {(identities[edge["relation_source"]], identities[edge["relation_target"]])
                 for edge in tree["edges"]}
        for role in ("Method", "Evaluation"):
            parent = f"Atom/(.Header.Context.Role:={role})"
            self.assertIn((parent + "/(.Header.Context.Form:=Decision)", parent), edges)

    def test_native_namespace_classification_keeps_source(self):
        row = carrier("CA-R-1", "CAPRMEDIO_MODEL", body(
            "### Formal Claim", "```python", "from caprmedio.formal_claims import declare_entity",
            "from caprmedio.model import Node", "class Model(Node):", "    pass",
            'declare_entity(entity_class=Model, entity_name="MODEL", classifications={"Container": "yes"})',
            "```"))
        graph = compose_contract_graph([row])
        namespace, = graph["namespaces"]
        entry, = namespace["own"]
        condition, = [clause for clause in entry["clauses"] if clause["kind"] == "classification_condition"]
        self.assertEqual(("MODEL", "Container", "==", "yes"),
                         tuple(condition[key] for key in ("subject_selector", "axis", "operator", "value")))
        self.assertEqual(row["source"], condition["source"])
        self.assertIn("MODEL >| Container == yes", render_contract_graph(graph))

    def test_relation_declaration_and_scoped_property_projection(self):
        from subject_projection_data import build_subject_projection_data

        rows = [carrier("CA-R-1", "Atom", body("```CFEL", "Atom;", "```"))]
        for index, role in enumerate(("Method", "Plan"), 2):
            rows.append(carrier(f"CA-R-{index}", f"Atom/(.Header.Context.Role := {role})", body(
                "### Formal Claim", "```python", "from caprmedio.formal_claims import declare_entity",
                "from caprmedio.model import Atom", f"class {role}(Atom):", "    pass",
                f"declare_entity(entity_class={role}, entity_name='{role}')", "```")))
        rows.append(carrier("CA-R-6", "Atom.Content", body(
            "### Formal Claim", "```CFEL", "Atom.Content.**:: [markdown];", "```")))
        rows.append(carrier("CA-R-4", "Atom.Content.Semantics", body(
            "### Formal Claim", "```python", "from caprmedio.formal_claims import declare_entity",
            "from caprmedio.model import Method",
            "declare_entity(entity_name='Semantics', relation_name='IS_PROPERTY_OF', base_path='Atom.Content', applies_to_entity_classes=(Method,), value_cardinality=1)",
            "```")))
        rows.append(carrier("CA-R-5", "Relation//CARRIES", body(
            "### Formal Claim", "```python", "from caprmedio.formal_claims import declare_relation",
            "declare_relation(relation_name='CARRIES', source_endpoint={'level':'instances'}, target_endpoint={'level':'instances'})",
            "```"), form="Relation Declaration"))
        data = build_subject_projection_data(rows)
        entities = {row["identity"]: row for row in data["entities"]}
        method = entities["Atom/(.Header.Context.Role:=Method)"]
        plan = entities["Atom/(.Header.Context.Role:=Plan)"]
        self.assertIn("Content.Semantics", [row["relative_name"] for row in method["inherited_properties"]])
        semantics = next(row for row in method["inherited_properties"] if row["relative_name"] == "Content.Semantics")
        self.assertEqual("markdown", semantics["effective_value_format"])
        self.assertEqual("CA-R-6", semantics["effective_value_format_sources"][0]["atom_id"])
        self.assertNotIn("Content.Semantics", [row["relative_name"] for row in plan["inherited_properties"]])
        self.assertIn("CARRIES", data["declarations"]["relations"])

    def test_python_model_claim_matches_cfel_and_retains_authored_source(self):
        cfel = carrier("CA-R-1", "Atom.Name", body("```CFEL", "# model", "Atom.Name:: [string]{::1};", "```"))
        raw = '# model\nproperty_rule(address="Atom.Name", value_format="string", values="1")\n'
        python = carrier("CA-R-2", "Atom.Name", body("```python", raw.rstrip(), "```"))
        old, old_diagnostics = extract_claim_constraints(cfel)
        new, diagnostics = extract_claim_constraints(python)
        self.assertEqual([{k: v for k, v in row.items() if k != "source"} for row in old_diagnostics],
                         [{k: v for k, v in row.items() if k != "source"} for row in diagnostics])
        self.assertEqual([{k: v for k, v in row.items() if k != "source"} for row in old],
                         [{k: v for k, v in row.items() if k != "source"} for row in new])
        graph = compose_contract_graph([cfel, python])
        entries = [entry for row in graph["entities"] for entry in row["own"]]
        entry = next(entry for entry in entries if entry["source"]["atom_id"] == "CA-R-2")
        self.assertEqual(raw, entry["python_blocks"][0]["block"])
        self.assertEqual("python", entry["python_blocks"][0]["label"])
        _, projected, label = _claims(_formal_claims([entry]))[0]
        self.assertEqual("```python\n" + raw + "```", _cfel(projected, label))

    def test_python_claim_invalid_is_diagnostic_and_prose_and_operations_are_not_executed(self):
        bad = carrier("CA-R-1", "Atom", body("### Formal Claim", "```python", "execute()", "```"))
        _, diagnostics = extract_claim_constraints(bad)
        self.assertEqual("python-formal-claim-invalid", diagnostics[0]["code"])
        with self.assertRaisesRegex(ValueError, "CA-R-1@"):
            compose_contract_graph([bad])
        prose = carrier("CA-R-2", "Atom", body("### Prose Claim", "```python", "execute()", "```"))
        workflow = carrier("CA-O-1", "Atom", body("### Formal Claim", "```python", "execute()", "```"), role="Operations")
        self.assertEqual(([], []), extract_claim_constraints(prose))
        self.assertEqual(([], []), extract_claim_constraints(workflow))

    def test_python_order_claim_preserves_legacy_graph_diagnostics(self):
        cfel = carrier("CA-R-1", "Atom", body("```CFEL", "# model", "Atom.A ;> Atom.B;", "```"))
        python = carrier("CA-R-1", "Atom", body("```python", "# model",
                         'order_before(first="Atom.A", second="Atom.B")', "```"))
        self.assertEqual(extract_claim_constraints(cfel), extract_claim_constraints(python))

    def test_operator_symbol_is_bound_to_its_declared_subject(self):
        address = "CAPRMEDIO_MODEL <+ CFEL <+ Operator//Delivery"
        cfel = carrier("CA-R-1", address, body("### Formal Claim", "```CFEL", "# model",
                       'Operator//Delivery == ">>"', "```"))
        python = carrier("CA-R-1", address, body("### Formal Claim", "```python", "# model",
                         """set_value(address="Operator//Delivery", value='">>"')""", "```"))
        clauses, diagnostics = extract_claim_constraints(cfel)
        self.assertFalse(diagnostics)
        self.assertEqual(extract_claim_constraints(python), (clauses, diagnostics))
        self.assertEqual([(row["kind"], row["operator"], row["symbol"]) for row in clauses],
                         [("operator_symbol", "Delivery", ">>")])
        for subject, expression in ((address.replace("Delivery", "Alias"), 'Operator//Delivery == ">>"'),
                                    (address, r'Operator//Delivery == "\q"')):
            with self.subTest(subject=subject, expression=expression):
                malformed = carrier("CA-R-1", subject, body("### Formal Claim", "```CFEL", "# model",
                                    expression, "```"))
                records, issues = extract_claim_constraints(malformed)
                self.assertFalse(records)
                self.assertEqual(len(issues), 1)

    def test_unary_relation_counts_keep_source_scope_and_no_target(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Node", body("```CFEL", "# model", "(Node, Node.**) {:1}((IS_DECLARED_BY));", "```")),
            carrier("CA-R-2", "Atom", body("```CFEL", "# instances", "Atom//$atom {:0..1}((HAS_ACTIVE_SUBJECT));", "Atom//$atom {:0..1}((GOVERNS));", "```")),
        ])
        node = next(row for row in graph["entities"] if row["target"] == "Node")
        atom = next(row for row in graph["entities"] if row["target"] == "Atom")
        clauses = node["own"][0]["clauses"] + atom["own"][0]["instance_clauses"]
        self.assertEqual(["IS_DECLARED_BY", "HAS_ACTIVE_SUBJECT", "GOVERNS"], [row["relation"] for row in clauses])
        self.assertEqual(["model", "instances", "instances"], [row["group"] for row in clauses])
        self.assertEqual(["(Node, Node.**)", "Atom//$atom", "Atom//$atom"], [row["source_selector"] for row in clauses])
        self.assertEqual([{"minimum": 1, "maximum": 1}, {"minimum": 0, "maximum": 1}, {"minimum": 0, "maximum": 1}],
                         [row["source_cardinality"] for row in clauses])
        self.assertTrue(all(row["target_selector"] is None and row["target_domain"] == "unresolved" and row["written_direction"] == "forward" for row in clauses))
        self.assertEqual([], graph["relations"])
        self.assertEqual({"Node", "Atom"}, {row["target"] for row in graph["entities"]})
        document = render_contract_graph(graph)
        self.assertIn("`(Node, Node.**)` — IS_DECLARED_BY; outgoing count=1; target domain unresolved", document)
        self.assertIn("`Atom//$atom` — HAS_ACTIVE_SUBJECT; outgoing count=0..1; target domain unresolved", document)
        self.assertIn("`Atom//$atom` — GOVERNS; outgoing count=0..1; target domain unresolved", document)
        self.assertNotIn("→ `None`", document)

    def test_namespace_declaration_preserves_claim_without_creating_node(self):
        graph = compose_contract_graph([carrier("CA-R-1", "CAPRMEDIO_MODEL", body("```CFEL", "MODEL >| (Container == yes)", "```")),
                                        carrier("CA-R-2", "UNKNOWN_MODEL", body("Unknown."))])
        self.assertEqual(["CAPRMEDIO_MODEL"], [row["target"] for row in graph["namespaces"]])
        self.assertEqual(["UNKNOWN_MODEL"], [row["target"] for row in graph["entities"]])
        self.assertEqual([], graph["coverage_gaps"])
        self.assertIn("MODEL >| (Container == yes)", render_contract_graph(graph))

    def test_render_occurrence_and_population_scopes(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Node", body("Node.")),
            carrier("CA-R-2", "Node.Name", body(
                "```CFEL", "# model", "Node.Name{:0..1}: [string]{:0..1};",
                "# instances", "Node.**//{:1};", "Node//$node{:1}", "```")),
        ])
        document = render_contract_graph(graph)
        self.assertIn("written names count=0..1; effective names count=0..1", document)
        self.assertIn("values count=0..1", document)
        self.assertIn("for each Property schema per bearer", document)
        self.assertIn("in project population", document)

    def test_qualified_declared_by_derivation_is_not_an_unconditional_inverse(self):
        graph = compose_contract_graph([carrier("CA-R-1", "CFEL <+ Relation//IS_DECLARED_BY", body(
            "### Formal Claim", "```CFEL", "# model",
            "Relation//IS_DECLARED_BY ((IS_DERIVED_RELATION_OF)) Relation//GOVERNS;", "```",
            "### Prose Claim", "Only governing links satisfying the Declaration ownership rule."))])
        relation = graph["relations"][0]
        self.assertEqual(["GOVERNS"], [row["name"] for row in relation["derivation_links"]])
        self.assertEqual([], relation["inverses"])
        self.assertNotIn("derived_view", relation)
        self.assertIn("not structurally interpreted", relation["derivation_scope"])

    def test_instance_group_does_not_supply_relation_classification_or_alias(self):
        graph = compose_contract_graph([carrier("CA-R-1", "CFEL <+ Relation//TEST", body(
            "### Formal Claim", "```CFEL", "# instances",
            "Relation//TEST ((HAS_CLASSIFICATION)) Derivation == Direct;",
            'alias(Relation//TEST) == "/";', "```"))])
        relation = graph["relations"][0]
        self.assertEqual([], relation["metadata"])
        self.assertEqual(2, len(relation["own"][0]["instance_clauses"]))

    def test_grouped_formal_claims_keep_instance_variables_out_of_model_contracts(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Atom", body("Atom.")),
            carrier("CA-R-2", "Atom.Header.Name", body(
                "### Formal Claim", "```CFEL", "# model",
                "Atom.Header.Name: [string]{:1};", 'alias(Relation//CONTAINS) == "# instances";',
                "# a full-line comment", "# instances", "Atom//$atom;", "$atom.Header.Name: [string]{:1};", "```")),
        ])
        row = next(row for row in graph["entities"] if row["target"] == "Atom.Header.Name")
        entry = row["own"][0]
        self.assertEqual(["model", "model"], [x["group"] for x in entry["clauses"]])
        self.assertEqual(["instance_binding", "property_constraint"], [x["kind"] for x in entry["instance_clauses"]])
        self.assertEqual("$atom.Header.Name", entry["instance_clauses"][1]["property_selector"])
        self.assertEqual("# instances", entry["clauses"][1]["glyph"])
        self.assertEqual([], entry["diagnostics"])
        self.assertIn("# instances", entry["cfel_blocks"][0]["block"])
        self.assertFalse(any("$atom" in x["target"] for x in graph["entities"]))
        self.assertIn("Instance constraints:", render_contract_graph(graph))

    def test_minimal_inverse_uses_corroborated_direct_meaning_and_reversed_endpoint_view(self):
        direct = carrier("CA-R-1", "CFEL <+ Relation//DIRECT", body(
            "### Formal Claim", "```CFEL", "$left ((DIRECT)) $right;",
            "Relation//DIRECT ((HAS_INVERSE)) Relation//INVERSE;",
            "Relation//DIRECT ((HAS_CLASSIFICATION)) Derivation == Direct", "```",
            "### Prose Claim", "Direct meaning."))
        inverse = carrier("CA-R-2", "CFEL <+ Relation//INVERSE", body(
            "### Formal Claim", "```CFEL", "Relation//INVERSE <((HAS_INVERSE)) Relation//DIRECT", "```"))
        graph = compose_contract_graph([direct, inverse])
        row = next(row for row in graph["relations"] if row["target"] == "INVERSE")
        self.assertEqual("Derived", row["derived_view"]["classification"])
        self.assertEqual("Direct meaning.", row["derived_view"]["meaning"])
        self.assertEqual([{"host": "$right", "target": "$left"}], row["derived_view"]["endpoints"])
        self.assertEqual([], row["host_target"])
        self.assertEqual(0, graph["coverage"]["missing_relation_semantics"])
        self.assertIn("not new permissions", render_contract_graph(graph))

        missing = compose_contract_graph([inverse])
        self.assertEqual(1, missing["coverage"]["missing_relation_semantics"])
        self.assertNotIn("derived_view", missing["relations"][0])
        conflicting = carrier("CA-R-3", "CFEL <+ Relation//OTHER", body(
            "### Formal Claim", "```CFEL", "Relation//OTHER ((HAS_INVERSE)) Relation//INVERSE;",
            "Relation//OTHER ((HAS_CLASSIFICATION)) Derivation == Direct", "```",
            "### Prose Claim", "Other meaning."))
        ambiguous = compose_contract_graph([direct, inverse, conflicting])
        inverse_row = next(row for row in ambiguous["relations"] if row["target"] == "INVERSE")
        self.assertNotIn("derived_view", inverse_row)

    def test_relation_bounds_and_quoted_counterpart_alias_remain_distinct(self):
        clauses, diagnostics = extract_claim_constraints(carrier("CA-R-1", "Node", body(
            "```CFEL", 'alias(HAS_INVERSE) == "<-->";',
            "Node{:1}((REL)){:2}Node;", "Node:{:1}((REL)){:2}Node;", "```")))
        alias = next(row for row in clauses if row["kind"] == "relation_alias")
        relation = next(row for row in clauses if row["kind"] == "relation_cardinality")
        self.assertEqual("<-->", alias["glyph"])
        self.assertEqual({"minimum": 2, "maximum": 2}, relation["target_cardinality"])
        self.assertEqual(1, len(diagnostics))

    def test_explicit_namespace_header_qualifications_bind_declared_properties(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "CAPRMEDIO_MODEL <+ Atom", body("Atom.")),
            carrier("CA-R-2", "CAPRMEDIO_MODEL <+ Atom.Header", body("Header.")),
            carrier("CA-R-3", "CAPRMEDIO_MODEL <+ Atom.Header.Role", body("Role.")),
            carrier("CA-R-4", "CAPRMEDIO_MODEL <+ Atom.Header.Form", body("Form.")),
            carrier("CA-R-5", "CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Requirement)", body("Role rule."), form="Rule"),
            carrier("CA-R-6", "CAPRMEDIO_MODEL <+ Atom/(.Header.Form:=Declaration)", body("Form rule."), form="Rule"),
            carrier("CA-R-7", "CAPRMEDIO_MODEL <+ (Node, Node.**)", body("Scope."), form="Rule"),
            carrier("CA-R-8", "CAPRMEDIO_MODEL <+ Node", body("Node.")),
            carrier("CA-R-9", "CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Requirement)/(.Header.Form:=Declaration)", body("Combined rule."), form="Rule"),
            carrier("CA-R-10", "CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Method)/(.Header.Form: Declaration)", body("Combined colon rule."), form="Rule"),
            carrier("CA-R-11", "CAPRMEDIO_MODEL <+ Atom.Content.Claim", body("Claim.")),
            carrier("CA-R-12", "CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Delivery).Content.Claim", body("Claim rule."), form="Rule"),
        ])
        rows = {row["target"]: row for row in graph["entities"]}
        self.assertEqual({"Atom", "Atom.Header", "Atom.Header.Role", "Atom.Header.Form", "Atom.Content.Claim", "Node"}, set(rows))
        self.assertEqual({"Atom.Header.Role", "Atom.Header.Form"},
                         {row["binding_context"]["property"] for row in rows["Atom"]["shared"] if "property" in row["binding_context"]})
        combined = next(row for row in rows["Atom"]["shared"] if row["source"]["atom_id"] == "CA-R-9")
        self.assertEqual(["Atom.Header.Role", "Atom.Header.Form"], combined["binding_context"]["properties"])
        self.assertEqual("CA-R-12", rows["Atom.Content.Claim"]["shared"][0]["source"]["atom_id"])
        self.assertEqual([], rows["Node"]["shared"])
        self.assertIn("complex selection scope", graph["coverage_gaps"][0]["message"])

    def test_named_claim_children_keep_prose_markdown_and_only_extract_formal_cfel(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Atom", """## Claim

### Formal Claim

```CFEL
Atom.Header: [YAML]{:1};
```

### Prose Claim

#### Context

Prose with an example:

```CFEL
Atom.Example: [wrong]{:1};
```
"""),
        ])
        entry = graph["entities"][0]["own"][0]
        self.assertEqual(["Atom.Header"], [row["property_selector"] for row in entry["clauses"]])
        self.assertIn("#### Context", entry["prose"])
        self.assertIn("Atom.Example", entry["prose"])
        self.assertEqual(1, len(entry["cfel_blocks"]))

    def test_prose_only_claim_does_not_interpret_cfel_examples(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Atom", """## Claim

### Prose Claim

```CFEL
Atom.Example: [wrong]{:1};
```
"""),
        ])
        entry = graph["entities"][0]["own"][0]
        self.assertEqual([], entry["clauses"])
        self.assertEqual([], entry["cfel_blocks"])
        self.assertEqual([], entry["diagnostics"])
        self.assertIn("Atom.Example", entry["prose"])

    def test_prose_claim_keeps_unrecognized_headings_at_any_level(self):
        graph = compose_contract_graph([carrier("CA-R-1", "Atom", """## Claim
### Prose Claim
Opening.
### Sibling Title
Sibling text.
## Dependent Selection
More text.
```CFEL
Atom.Example: [wrong]{:1};
```
## Expression Lists
Last text.
## Details
Actual root detail.
""")])
        entry = graph["entities"][0]["own"][0]
        self.assertIn("### Sibling Title\nSibling text.", entry["prose"])
        self.assertIn("## Dependent Selection\nMore text.", entry["prose"])
        self.assertIn("Atom.Example", entry["prose"])
        self.assertIn("## Expression Lists\nLast text.", entry["prose"])
        self.assertNotIn("Actual root detail", entry["prose"])
        self.assertEqual([], entry["diagnostics"])
        self.assertEqual([], entry["clauses"])

    def test_attaches_exact_shared_rmed_evidence_and_links_transitive_properties_without_copies(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Node", body("Node declaration.")),
            carrier("CA-R-2", "Node/Parent", body("Parent declaration.")),
            carrier("CA-R-3", "Node/Parent/Child", body("Child declaration.")),
            carrier("CA-R-4", "Node/Parent.Status", body("```CFEL", "Node/Parent.Status: [string]{:1};", "```")),
            carrier("CA-R-5", "Node/Parent/Child", body("Rule for Child."), form="Rule"),
            carrier("CA-D-6", "Node/Parent/Child", body("Delivery for Child."), role="Delivery", form="Markdown"),
            carrier("CA-R-7", "Node/Unknown", body("```CFEL", "Node/Unknown.Status: [string]{:1};", "```"), form="Rule"),
        ])

        rows = {row["target"]: row for row in graph["entities"]}
        child = rows["Node/Parent/Child"]
        self.assertEqual(["CA-D-6@1", "CA-R-5@1"], child["shared_sources"])
        self.assertEqual(["Node/Parent", "Node"], [row["target"] for row in child["transitive_ancestors"]])
        self.assertEqual(["Node/Parent.Status"], [row["target"] for row in child["inherited_property_declarations"]])
        self.assertNotIn("Node/Parent/Child.Status", rows)
        self.assertEqual(1, graph["coverage"]["coverage_gaps"])
        self.assertIn("Node/Unknown.Status", graph["coverage_gaps"][0]["blocks"][0]["block"])
        rendered = render_contract_graph(graph)
        self.assertLess(rendered.index("## Declared Narrowing Tree"), rendered.index("## Entity and Property Contracts"))
        self.assertIn("Transitive ancestor Declarations", rendered)
        self.assertIn("Inherited Property Declaration refs", rendered)

    def test_keeps_cfel_component_and_semantics_without_inventing_a_node(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "CFEL <+ Format", body("Format declaration.", semantics="A CFEL component.")),
            carrier("CA-R-2", "CFEL", body("CFEL root declaration.")),
            carrier("CA-R-3", "Operator", body("Operator kind declaration.")),
            carrier("CA-R-4", "Operator//Anatoly", body("Operator instance declaration.")),
        ])

        self.assertEqual(["CFEL", "Format"], [row["target"] for row in graph["components"]])
        self.assertEqual({("Operator", "primary_node"), ("Operator//Anatoly", "instance")},
                         {(row["target"], row["kind"]) for row in graph["entities"]})
        instance = next(row for row in graph["entities"] if row["kind"] == "instance")
        self.assertEqual(["CA-R-3@1"], instance["instance_of"]["effective_source_refs"])
        rendered = render_contract_graph(graph)
        self.assertIn("CFEL, Carrier, and Term Component Contracts", rendered)
        self.assertIn("A CFEL component.", rendered)

    def test_keeps_explicit_cfel_component_properties_and_instances_out_of_narrowing_tree(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "CFEL", body("CFEL root declaration.")),
            carrier("CA-R-2", "CFEL <+ Format", body("Format declaration.")),
            carrier("CA-R-3", "CFEL <+ Format.Data Type", body("Format Property declaration.")),
            carrier("CA-R-4", "CFEL <+ Format//markdown", body("Markdown format declaration.")),
            carrier("CA-R-5", "CFEL <+ Operator", body("Operator declaration.")),
            carrier("CA-R-6", "CFEL <+ Operator//Addition", body("Addition declaration.")),
        ])

        rows = {row["target"]: row for row in graph["entities"]}
        self.assertEqual("property", rows["Format.Data Type"]["kind"])
        self.assertEqual("instance", rows["Format//markdown"]["kind"])
        self.assertEqual("instance", rows["Operator//Addition"]["kind"])
        self.assertEqual(["CA-R-2@1"], rows["Format//markdown"]["instance_of"]["effective_source_refs"])
        self.assertEqual(
            {"CFEL", "Format", "Operator"},
            {row["identity"] for row in graph["narrowing_tree"]["nodes"]},
        )
        self.assertEqual([], graph["narrowing_tree"]["edges"])
        self.assertFalse(graph["inheritance_diagnostics"])
        self.assertEqual(0, graph["coverage"]["coverage_gaps"])
        self.assertEqual(0, graph["coverage"]["instance_kind_gaps"])

    def test_binds_only_declared_value_and_qualifier_conditions_and_keeps_other_evidence_scoped(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Atom", body("Atom declaration.")),
            carrier("CA-R-2", "Atom.Status", body("Status declaration.")),
            carrier("CA-R-3", "Projection", body("Projection declaration.")),
            carrier("CA-R-4", "Projection.Form", body("Form declaration.")),
            carrier("CA-R-5", "Atom.Status:Draft", body("Draft status rule."), form="Rule"),
            carrier("CA-R-6", "Projection/(.Form:=ApplicableMethodology)", body("Projection form rule."), form="Rule"),
            carrier("CA-R-7", "Atom.Kind:Unknown", body("Unknown property rule."), form="Rule"),
            carrier("CA-M-8", "Method/PlanProcess", body("Method evidence."), role="Method", form="Policy"),
        ])

        rows = {row["target"]: row for row in graph["entities"]}
        self.assertEqual("allowed_value_condition", rows["Atom.Status"]["shared"][0]["binding"])
        self.assertEqual("Atom.Status:Draft", rows["Atom.Status"]["shared"][0]["subject"])
        self.assertEqual("property_qualification", rows["Projection"]["shared"][0]["binding"])
        self.assertNotIn("Projection/(.Form:=ApplicableMethodology)", rows)
        self.assertEqual(1, graph["coverage"]["coverage_gaps"])
        self.assertEqual(1, graph["coverage"]["outside_model_scope_sources"])
        self.assertEqual("outside_model_scope", graph["outside_model_scope"][0]["selection_disposition"])

    def test_binds_only_source_proven_scope_unit_declaration_instance_contexts(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Scope Unit", body("Scope Unit kind declaration.")),
            carrier("CA-R-2", "Project", body("Project kind declaration.")),
            carrier("CA-R-9", "Projection", body("Projection kind declaration.")),
            carrier("CA-R-10", "Named Selection", body("Selection kind declaration.")),
            carrier("CA-R-11", "CAPRMEDIO <+ MODEL <+ PROJECT STRUCTURE", body("Structure kind declaration.")),
            carrier("CA-R-3", "Scope Unit//CORE_META_MODEL", body("Core scope declaration."),
                    form="Scope Unit Declaration"),
            carrier("CA-R-4", "Project//caprmedio", body("Project declaration."),
                    form="Scope Unit Declaration"),
            carrier("CA-R-5", "Scope Unit//CORE_META_MODEL", body("Core scope evidence."),
                    form="Rule"),
            carrier("CA-R-6", "Project//caprmedio", body("Project evidence."), form="Rule"),
            carrier("CA-R-7", "Scope Unit//MISSING", body("Missing scope evidence."), form="Rule"),
            carrier("CA-R-8", "Actor//ANATOLY", body("Unknown kind declaration."),
                    form="Scope Unit Declaration"),
            carrier("CA-R-12", "Projection//PROJECT_SCOPE_UNIT_GRAPH", body("Projection context."),
                    form="Rule"),
            carrier("CA-R-13", "Named Selection//ExtensionSources", body("Selection context."),
                    form="Rule"),
            carrier("CA-R-14", "CAPRMEDIO <+ STRUCTURE", body("Structure context."),
                    form="Rule"),
            carrier("CA-R-15", "Named Selection//Unknown", body("Unknown selection context."),
                    form="Rule"),
            carrier("CA-R-16", "PROJECT STRUCTURE//CAPRMEDIO", body("Historical structure context."),
                    form="Rule"),
        ])

        entities = {row["target"]: row for row in graph["entities"]}
        scope_shared = entities["Scope Unit"]["shared"]
        project_shared = entities["Project"]["shared"]
        projection_shared = entities["Projection"]["shared"]
        selection_shared = entities["Named Selection"]["shared"]
        structure_shared = entities["PROJECT STRUCTURE"]["shared"]
        self.assertEqual(["CA-R-3@1", "CA-R-5@1"], entities["Scope Unit"]["shared_sources"])
        self.assertEqual("scope_unit_declaration_context", scope_shared[0]["binding"])
        self.assertEqual("scope_unit_declaration_context", project_shared[0]["binding"])
        self.assertEqual(
            "current_scope_unit_declaration",
            scope_shared[0]["binding_context"]["existence_provenance"],
        )
        self.assertEqual(
            {"atom_id": "CA-R-3", "version": 1, "path": "sources/CA-R-3.md"},
            scope_shared[1]["binding_context"]["declaration_source"],
        )
        self.assertEqual(
            "CA-R-4", project_shared[1]["binding_context"]["declaration_source"]["atom_id"],
        )
        self.assertEqual("known_instance_context", projection_shared[0]["binding"])
        self.assertEqual("known_instance_context", selection_shared[0]["binding"])
        self.assertEqual("known_instance_context", structure_shared[0]["binding"])
        self.assertEqual(
            "bounded_named_contract_context",
            selection_shared[0]["binding_context"]["existence_provenance"],
        )
        self.assertEqual(
            ["CA-R-1"], [row["source"]["atom_id"] for row in entities["Scope Unit"]["own"]],
        )
        self.assertNotIn("Scope Unit//CORE_META_MODEL", entities)
        self.assertNotIn("Actor//ANATOLY", entities)
        self.assertEqual(2, graph["coverage"]["coverage_gaps"])
        self.assertEqual(2, graph["coverage"]["outside_model_scope_sources"])
        self.assertEqual(
            {"CA-R-7", "CA-R-15"},
            {row["source"]["atom_id"] for row in graph["coverage_gaps"]},
        )
        self.assertEqual(
            {"CA-R-8", "CA-R-14"},
            {row["source"]["atom_id"] for row in graph["outside_model_scope"]},
        )

    def test_binds_prefixed_namespaces_to_local_targets_without_losing_subject_provenance(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "CAPRMEDIO <+ MODEL <+ Node", body("Node declaration.")),
            carrier("CA-R-2", "CAPRMEDIO <+ MODEL <+ Node.Status", body("Status declaration.")),
            carrier("CA-R-3", "CAPRMEDIO <+ MODEL <+ Node//Example", body("Example declaration.")),
            carrier("CA-R-4", "CAPRMEDIO <+ MODEL <+ CFEL <+ Format", body("Format declaration.")),
            carrier("CA-R-5", "CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//depends_on",
                    body("Relation declaration."), form="Relation Definition"),
            carrier("CA-R-6", "CAPRMEDIO <+ STRUCTURE <+ Project", body("Project declaration.")),
            carrier("CA-R-7", "CAPRMEDIO <+ STRUCTURE <+ Project//caprmedio",
                    body("Project declaration context."), form="Scope Unit Declaration"),
            carrier("CA-R-8", "CAPRMEDIO <+ MODEL <+ Node", body("Node rule."), form="Rule"),
            carrier("CA-R-9", "CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//depends_on",
                    body("Relation rule."), form="Rule"),
            carrier("CA-R-10", "CAPRMEDIO <+ STRUCTURE <+ Project//caprmedio",
                    body("Project rule."), form="Rule"),
            carrier("CA-R-11", "CAPRMEDIO <+ MODEL <+ Projection", body("Projection declaration.")),
            carrier("CA-R-12", "CAPRMEDIO <+ MODEL <+ Named Selection", body("Selection declaration.")),
            carrier("CA-R-13", "CAPRMEDIO <+ MODEL <+ (Node, Node.**)", body("Node scope."), form="Rule"),
            carrier("CA-R-14", "CAPRMEDIO <+ MODEL <+ (Node, Node.**)", body("Node scope."), form="Rule"),
            carrier("CA-R-15", "CAPRMEDIO <+ STRUCTURE <+ Projection//PROJECT_SCOPE_UNIT_GRAPH",
                    body("Projection context."), form="Rule"),
            carrier("CA-R-16", "CAPRMEDIO <+ STRUCTURE <+ Projection//PROJECT_SCOPE_UNIT_GRAPH",
                    body("Projection context."), form="Rule"),
            carrier("CA-R-17", "CAPRMEDIO <+ STRUCTURE <+ Named Selection//Extension Sources",
                    body("Selection context."), form="Rule"),
        ])

        entities = {row["target"]: row for row in graph["entities"]}
        components = {row["target"]: row for row in graph["components"]}
        relations = {row["target"]: row for row in graph["relations"]}
        self.assertEqual("exact", entities["Node"]["shared"][0]["binding"])
        self.assertEqual("CAPRMEDIO <+ MODEL <+ Node", entities["Node"]["shared"][0]["subject"])
        self.assertEqual("property", entities["Node.Status"]["kind"])
        self.assertEqual("instance", entities["Node//Example"]["kind"])
        self.assertEqual("component", components["Format"]["kind"])
        self.assertEqual("Project", entities["Project"]["shared"][0]["target"])
        self.assertEqual("scope_unit_declaration_context", entities["Project"]["shared"][0]["binding"])
        self.assertEqual("depends_on", relations["depends_on"]["target"])
        self.assertEqual("CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//depends_on",
                         relations["depends_on"]["shared"][0]["subject"])
        self.assertEqual(1, len(entities["Node"]["shared"]))
        self.assertEqual(2, len(entities["Projection"]["shared"]))
        self.assertEqual("known_instance_context", entities["Projection"]["shared"][0]["binding"])
        self.assertEqual("known_instance_context", entities["Named Selection"]["shared"][0]["binding"])
        self.assertEqual(2, graph["coverage"]["coverage_gaps"])

    def test_claim_scope_and_details_are_source_bound_context_before_claim(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Atom.Status", body("Status declaration.")),
            carrier("CA-R-2", "Atom.Status:Draft", """## Claim Scope

Only Draft Atom instances.

## Claim

Draft status rule.

## Details

Carrier-specific constraint.
""", form="Rule"),
        ])

        rendered = render_contract_graph(graph)
        rule = rendered[rendered.index("CA-R-2@1"):]
        self.assertLess(rule.index("Claim Scope:"), rule.index("Remaining Claim prose:"))
        self.assertIn("Only Draft Atom instances.", rendered)
        self.assertIn("Details (source-bound):", rendered)
        self.assertIn("Carrier-specific constraint.", rendered)

    def test_preserved_unsupported_cfel_is_partial_extraction_not_a_display_gap(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Node", body("```CFEL", "IF Node THEN Property", "```")),
        ])

        self.assertEqual("complete", graph["display_coverage"])
        self.assertEqual("partial", graph["structured_cfel"])
        self.assertEqual("complete", graph["outcome"])
        self.assertIn("IF Node THEN Property", render_contract_graph(graph))

    def test_relation_metadata_is_case_preserving_and_inverse_is_not_another_declaration(self):
        graph = compose_contract_graph([
            carrier(
                "CA-R-1", "CFEL <+ Relation//depends_on",
                body(
                    "```CFEL", "Step// {:1}((depends_on)){:1} Action//;",
                    "((depends_on)) ((HAS_INVERSE)) ((is_depended_on));",
                    "((depends_on)) ((IS_DERIVED_RELATION_OF)) ((is_depended_on));",
                    "((depends_on)) == <<;", "((depends_on)) >| Derivation == Direct;", "```",
                    semantics="Dependency direction.",
                ),
            ),
        ])

        relation = graph["relations"][0]
        self.assertEqual("depends_on", relation["target"])
        self.assertEqual(["is_depended_on"], [row["name"] for row in relation["inverses"]])
        self.assertEqual(["is_depended_on"], [row["name"] for row in relation["derivation_links"]])
        self.assertEqual({"notation", "derivation"}, {row["kind"] for row in relation["metadata"]})
        self.assertEqual(0, graph["coverage"]["missing_relation_semantics"])
        rendered = render_contract_graph(graph)
        self.assertIn("does not certify an undeclared inverse Relation", rendered)
        self.assertIn("Derivation interpretation gap", rendered)
        self.assertNotIn("((is_depended_on)) — declared Relation", rendered)

    def test_typed_relation_alias_and_inverse_are_source_bound_in_either_direction(self):
        def read(binding):
            return compose_contract_graph([
                carrier("CA-R-1", "CFEL <+ Relation//NARROWER_THAN", body(
                    "### Formal Claim", "```CFEL",
                    'alias(Relation//NARROWER_THAN) == "/";',
                    binding,
                    "Node ((NARROWER_THAN)) Node;", "```")),
            ])["relations"][0]

        forward = read("Relation//NARROWER_THAN ((HAS_INVERSE)) Relation//BROADER_THAN;")
        reverse = read("Relation//BROADER_THAN <((HAS_INVERSE)) Relation//NARROWER_THAN;")
        glyph = read("Relation//NARROWER_THAN <--> Relation//BROADER_THAN;")
        self.assertEqual(["BROADER_THAN"], [row["name"] for row in forward["inverses"]])
        self.assertEqual(forward["inverses"], reverse["inverses"])
        self.assertEqual(forward["inverses"], glyph["inverses"])
        self.assertEqual(["/"], [row["value"] for row in forward["metadata"]])
        self.assertEqual(["Node"], [row["source_selector"] for row in forward["host_target"]])
        self.assertEqual(1, len(forward["host_target"]))

        graph = compose_contract_graph([carrier("CA-R-2", "CFEL <+ Relation//CONTAINS", body(
            "### Formal Claim", "```CFEL", 'alias(Relation//CONTAINS) == "<+";', "```"))])
        self.assertEqual([], graph["entities"])
        self.assertEqual([], graph["relations"][0]["host_target"])
        self.assertEqual("<+", graph["relations"][0]["metadata"][0]["value"])

    def test_preserves_unlabelled_claim_blocks_and_reports_unbound_source(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Node", body("Node declaration.")),
            carrier("CA-R-2", "Node/Missing", body("Legacy formal evidence:", "```", "Node/Missing: [string]{:1}", "```"), form="Rule"),
        ])

        gap = graph["coverage_gaps"][0]
        self.assertEqual("", gap["blocks"][0]["label"])
        self.assertIn("Node/Missing", gap["blocks"][0]["block"])
        rendered = render_contract_graph(graph)
        self.assertIn("Unbound source evidence", rendered)
        self.assertIn("```\nNode/Missing", rendered)

    def test_renders_blank_outside_scope_prose_lines_without_trailing_whitespace(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Node", body("Node declaration.")),
            carrier("CA-R-2", "Unknown", body("First outside line.", "", "Second outside line."), form="Rule"),
        ])

        rendered = render_contract_graph(graph)
        self.assertIn("    First outside line.\n\n    Second outside line.", rendered)
        self.assertFalse(any(line.endswith(" ") for line in rendered.splitlines()))

    def test_declared_derived_relation_keeps_its_own_metadata(self):
        graph = compose_contract_graph([
            carrier(
                "CA-R-1", "CFEL <+ Relation//is_depended_on",
                body("```CFEL", "((is_depended_on)) >| Derivation == Derived;", "```", semantics="Reverse dependency."),
            ),
        ])

        relation = graph["relations"][0]
        self.assertEqual("is_depended_on", relation["target"])
        self.assertEqual(["Derived"], [row["value"] for row in relation["metadata"]])
        self.assertIn("`((is_depended_on))` — declared Relation", render_contract_graph(graph))

    def test_duplicate_declaration_and_missing_relation_semantics_are_coverage_failures(self):
        graph = compose_contract_graph([
            carrier("CA-R-1", "Node", body("One.")),
            carrier("CA-R-2", "Node", body("Two.")),
            carrier("CA-R-3", "CFEL <+ Relation//RUN", body("```CFEL", "((RUN)) == >>;", "```")),
        ])

        self.assertEqual(1, graph["coverage"]["duplicate_declarations"])
        self.assertEqual(1, graph["coverage"]["missing_relation_semantics"])
        self.assertEqual("incomplete", graph["outcome"])

