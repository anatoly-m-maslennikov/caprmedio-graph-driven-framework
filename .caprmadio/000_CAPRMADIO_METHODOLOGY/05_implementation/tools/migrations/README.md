# DSET migration tools

This directory contains reusable migration safety mechanisms and bounded
migration recipes. Run an active recipe from a repository checkout; do not copy
completed migrations into the active toolchain.

## Run the active META/GOV carrier migration

The active recipe converts the historical root META/GOV methodology carriers
to their canonical formats.

### 1. Preview

From this repository:

```bash
python3 15_layer_implementation/tools/migrations/migrate_meta_gov_carriers.py
```

For another checkout or replay fixture:

```bash
python3 15_layer_implementation/tools/migrations/migrate_meta_gov_carriers.py \
  /path/to/repository
```

Preview is the default and does not change files. It prints every planned
operation and a stable `plan-digest`.

### 2. Apply the reviewed plan

Copy the digest from the preview and bind the application to it:

```bash
python3 15_layer_implementation/tools/migrations/migrate_meta_gov_carriers.py \
  /path/to/repository \
  --apply \
  --expect-plan-digest PLAN_DIGEST
```

The tool rebuilds the plan immediately before applying it. If any planned path,
preimage, output byte, or reason changed, the digest differs and application
stops.

### 3. Verify

```bash
python3 15_layer_implementation/tools/migrations/migrate_meta_gov_carriers.py \
  /path/to/repository \
  --check
```

After successful application, another preview must report:

```text
writes: 0
deletes: 0
```

The legacy entry point remains available:

```bash
python3 scripts/migrate_meta_gov_carriers.py --check
```

It is only a compatibility launcher and delegates to the active recipe.

## Run the CAPRMADIO identity-prefix migration

The identity recipe performs one whole-repository cutover from the retired
project identity prefix to `CAPRMADIO-`. Its inventory is limited to tracked Git
files, and it migrates both carrier content and path names.

Preview and copy the reported plan digest:

```bash
python3 \
  15_layer_implementation/tools/migrations/migrate_identity_prefix_to_caprmadio.py
```

Apply only that exact plan:

```bash
python3 \
  15_layer_implementation/tools/migrations/migrate_identity_prefix_to_caprmadio.py \
  --apply \
  --expect-plan-digest PLAN_DIGEST
```

Verify the cutover or replay a completed migration:

```bash
python3 \
  15_layer_implementation/tools/migrations/migrate_identity_prefix_to_caprmadio.py \
  --check
```

A successful second preview reports zero writes and deletes.

## Run the CAPRMADIO repository-directory migration

This recipe renames the governed and runtime top-level directories, the
installed methodology directory, and the project-settings stem while
preserving ignored runtime state and rewriting every tracked text reference.
Preview the complete tracked-carrier plan:

```bash
python3 \
  15_layer_implementation/tools/migrations/migrate_repository_directories_to_caprmadio.py
```

Apply only the reviewed plan digest:

```bash
python3 \
  15_layer_implementation/tools/migrations/migrate_repository_directories_to_caprmadio.py \
  --apply \
  --expect-plan-digest PLAN_DIGEST
```

Verify the current repository tree:

```bash
python3 \
  15_layer_implementation/tools/migrations/migrate_repository_directories_to_caprmadio.py \
  --check
```

## Safety behavior

The shared runtime:

- rejects unknown carriers, path and symlink escape, duplicate targets, and
  write/delete collisions;
- binds every operation to its exact preimage;
- stages candidate bytes under `.caprmadio_runtime/migrations`;
- validates staged carriers before replacing live files;
- verifies the complete result after replacement;
- restores every touched byte if staging, replacement, or verification fails;
  and
- keeps Python bytecode and temporary fixtures outside the governed source
  tree.

A blocked operation exits non-zero and begins its diagnostic with `BLOCKED:`.
Resolve the cause and run preview again; do not bypass the safeguard.

## Completed historical tools

The `completed/` directory preserves two bounded tools for historical replay:

- `dset_migrate_meta_gov_atomics.py` migrates the exact 319-atom META/GOV
  dataset for which it was created.
- `dset_verify_meta_gov_migration.py` proves that the replay preserved paths,
  IDs, relations, and body content.

They are not active general-purpose commands. Use them only with a matching
historical fixture or when reproducing that completed migration:

```bash
python3 \
  15_layer_implementation/tools/migrations/completed/dset_migrate_meta_gov_atomics.py \
  /path/to/replay \
  --check

python3 \
  15_layer_implementation/tools/migrations/completed/dset_verify_meta_gov_migration.py \
  /path/to/replay
```

## Add a future migration

Create one bounded recipe beside `migrate_meta_gov_carriers.py`. Keep
classification and rewriting rules inside the recipe, and reuse:

- `dset_migration_tools.models` for immutable operations, plans, summaries, and
  plan digests;
- `dset_migration_tools.safety` for root containment, collision, regular-file,
  and preimage checks; and
- `dset_migration_tools.transaction` for staging, staged validation,
  replacement, rollback, cleanup, and final verification.

The recipe must provide:

1. a deterministic, mutation-free plan builder;
2. semantic validation for every staged output;
3. complete post-application verification; and
4. a second-run zero-operation result.

Call the shared transaction boundary as:

```python
apply_transaction(plan, validate_staged, verify)
```

Do not add a generic migration DSL or public migration CLI until at least two
active recipes share a proven semantic contract. Move a completed,
schema-specific recipe to `completed/` rather than leaving it discoverable as
an active migration.
