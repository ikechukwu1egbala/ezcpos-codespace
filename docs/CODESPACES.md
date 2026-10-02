# Codespaces setup

1. Open GitHub → repository → **Code → Codespaces → Create codespace on main**.
2. Wait for the container to finish provisioning.
3. Open the terminal in VS Code (Terminal → New Terminal). **All commands in this document are run there.**
4. From the project root run:

```bash
pwd
./scripts/setup.sh
./scripts/test.sh
```

The setup script creates the Python virtual environment, installs backend dependencies, migrates the development database and installs Flutter packages.

### Backend

```bash
./scripts/run_backend.sh
```

The API is then available at `http://127.0.0.1:8000/`.

### Flutter web preview

Use another terminal:
```bash
cd frontend
flutter run -d chrome --web-port 8080
```

Codespaces will offer to forward port 8080.

### Android

Codespaces is the build machine; a physical Android device is not required for compiling. Use:
```bash
cd frontend
flutter build apk --release
```
The APK will be at `build/app/outputs/flutter-apk/app-release.apk`.

### Development API URL
For Chrome, `http://127.0.0.1:8000` works when the browser and Django run in the same Codespace. For an Android emulator/device, set `EZC_API_BASE_URL` to the reachable forwarded/public API URL or configure the emulator networking appropriately.
