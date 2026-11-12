# Generated from the admitted Workflow Formal Claim.

WORKFLOW_BINDING = {'workflow': 'CA-O-10011@4', 'step': 'CA-O-10010@1', 'action': 'CA-O-10007@1'}
SOURCE_SHA256 = {
    'CA-O-10011@4': 'e86a64552bfa47ad162b58adf64aaa919fc6ade7b69a277fc98c2bb4adc49c37',
    'CA-O-10010@1': '6eaa0d360e322a82fdfad60ff4399bd9d32c67f0f6483c16dfa440709cd70272',
    'CA-O-10007@1': 'adfc8492bcc26e21935496ebcb382fef99b373578fd91206953937deb8aeac3f',
}


def change_current_status(*, invocation, engine):
    tree = engine.read_status_tree()
    requested_status = invocation.target_status.casefold()
    parent_status = tree.parent.status.casefold()
    terminal = {"done", "canceled"}
    entering_backlog = tree.is_plan and tree.shared_backlog and requested_status == "backlog"
    reopening = tree.is_plan and (
        (parent_status in terminal and requested_status not in terminal | {"draft", "archived"})
        or (parent_status == "backlog" and requested_status == "active")
    )
    parent_first = entering_backlog or reopening
    ordered_atoms = reversed(tree.child_first) if parent_first else tree.child_first
    closing = tree.is_plan and requested_status in terminal
    actions = []
    for atom in ordered_atoms:
        closing_child = closing and atom.atom_id != tree.parent.atom_id
        if closing_child and atom.status.casefold() in terminal:
            continue
        actions.append((atom.atom_id, "Canceled" if closing_child else invocation.target_status))
    engine.preflight(actions=actions, parent_first=parent_first,
                     entering_backlog=entering_backlog, reopening=reopening)
    for atom_id, selected_status in actions:
        if not engine.invoke(step="CA-O-10010@1", action="CA-O-10007@1",
                             atom_id=atom_id, target_status=selected_status):
            return
