# Codespaces-first workflow

1. Create a Codespace from this repository.
2. Run `./scripts/setup.sh`.
3. Run `./scripts/test.sh`.
4. Run `cd frontend && flutter analyze && flutter test`.
5. Build with `cd frontend && flutter build apk --release`.

No Termux-specific paths are required. The repository is designed to use the Flutter/Dart version configured by the Codespace image/CI.
