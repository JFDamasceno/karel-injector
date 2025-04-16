# 🦾 Karel Injection Tool

A simple command-line utility to **compile** and **inject Karel programs** into a FANUC robot controller via FTP. Optionally, it can also **trigger unit tests** using [KUNIT](https://github.com/onerobotics/KUnit) framework.

---

## 📦 Features

- ✅ Compiles `.kl` source files using `ktrans`
- ✅ Uploads `.pc` files to a robot controller over FTP
- ✅ Supports local or remote robot IPs (default: `127.0.0.1`)
- ✅ Optional KUnit test execution via browser
- ✅ Built-in error handling for compilation issues

---

## 🚀 Usage

### Command Syntax

```bash
inject <filename> [-i IP_ADDRESS] [-t]
```

### Parameters

| Argument         | Description                                        |
|------------------|----------------------------------------------------|
| `filename`       | Required. Base name of the `.kl` file (without extension). |
| `-i`, `--ip`     | Optional. IP address of the robot controller. Default is `127.0.0.1`. |
| `-t`, `--test`   | Optional. Triggers a unit test using KUnit after injection. |

---

### Example Commands

```bash
# Compile and transfer MYFILE.kl to local controller
inject MYFILE

# Compile, transfer and run unit test MYFILE.kl to local controller
inject MYFILE -t

# Compile and transfer to remote controller
inject MYFILE -i 192.168.1.1


```

---

## 🛠 Requirements

- Python 3.7+
- `ktrans` must be installed and available in your system PATH
- FTP access to the controller must be enabled
- Web browser for KUnit test interface

---

## 📦 Build as Executable (Windows)

To generate a standalone `.exe`:

```bash
pip install pyinstaller
pyinstaller --onefile inject.py
```

Find the `.exe` in the `dist/` folder. Now you can run:

```bash
inject.exe MYFILE -i 192.168.0.5 -t
```

---

## 📁 File Structure

```
project/
├── inject.py          # Main script
├── README.md          # This file
├── MYFILE.kl          # Sample Karel source file
└── dist/
    └── inject.exe     # (After building with PyInstaller)
```

---

## 🧪 KUnit Integration

If `-t` is used, the tool opens the following URL in your default browser:

```
http://<ip>:9001/KAREL/kunit?filenames=<filename>
```

Ensure the robot controller is active and reachable.

---

## Contributions
 1. Fork
 2. Create feature branch
 3. Commit changes
 4. Push to the branch
 5. Create new Pull Request

---

## 📄 License

MIT License. Do what you want, but at your own risk 🤖

---
