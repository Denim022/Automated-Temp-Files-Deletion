# 🧹 Windows Temp Cleaner (Python)

A smart, scriptable Windows temp file cleaner that **deletes everything that can be safely removed**, while automatically skipping files currently in use or locked by the system — just like File Explorer’s “Do this for all → Skip” option.

---

## ⚙️ Features

- Deletes files and folders in `%TEMP%` and optionally `C:\Windows\Temp`
- Gracefully skips locked/in-use files without crashing
- Logs skipped files with reasons (WinError codes, file lock status, etc.)
- Lightweight, no dependencies except Python standard library
- Console summary: files deleted vs skipped
- Optional logging to a text file

---

## 🛠️ How It Works

1. Iterates through all files and folders in the temp directory
2. Attempts to open each file to check if it's locked
3. Deletes unlocked files and folders
4. Skips everything else and logs the reason
5. Reports a cleanup summary

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Denim022/Automated-Temp-Files-Deletion.git
