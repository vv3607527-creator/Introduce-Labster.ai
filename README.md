# Lobster AI

This repository currently contains a product and architecture specification for a planned, self-hosted assistant. It does **not** yet contain an executable service, installer, integrations, model configuration, database schema, or deployment definition.

## Current status

- The source specification is in [`Labster ai`](./Labster%20ai).
- No runtime or production credentials are required to run the repository checks.
- The repository check validates that the specification retains its required architecture and safety-oriented sections; it does not claim that the planned system is implemented.

## Local check

From the repository root, run:

```bash
python3 -m unittest discover -s tests -v
```

The check uses only the Python standard library and reads the local specification. It makes no network calls, does not contact production systems, and does not execute the installer command described in the specification.

## Implementation prerequisites

Before this can be considered an executable project, a future change should add, at minimum:

1. A pinned dependency manifest and reproducible development setup.
2. A local-only runtime with explicit authentication, authorization, secret handling, input validation, rate limits, and safe tool execution.
3. Unit, integration, and end-to-end tests using local fakes/fixtures for every supported chat and voice adapter.
4. CI that runs the checks without production credentials.
5. Operational documentation covering backups, migrations, upgrades, failure recovery, and threat modeling.
