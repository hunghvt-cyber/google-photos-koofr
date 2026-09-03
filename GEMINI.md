# Google Photos Sync Operating Rules

This file supplements the Global `GEMINI.md` with rules specific to the Google Photos to Koofr sync engine.

## 1. Workflow Sequence
Adhere strictly to the established sync steps:
1. `scan`: Inventory Google Photos.
2. `manifest`: Build local manifest.
3. `compare` & `plan`: Identify differences.
4. `safety`: Run `SafetyGuardrail` validation.
5. `sync` & `state`: Execute transfers and update state.

## 2. Safety & Data Protection
- **Safety Guardrail**: Never bypass or ignore `SafetyGuardrail` failures. If it triggers, STOP and investigate.
- **Dry Run**: Always use `--dry-run` when testing changes to the planner or downloader logic.
- **Source Integrity**: Do not perform any operation that could delete or modify original data on Google Photos.

## 3. Credentials
- OAuth tokens and Koofr credentials must be handled securely via the configuration system.
- Do not expose tokens in logs or error reports.

## 4. Implementation
- The project is built in Python. Follow the modular structure in `src/`.
