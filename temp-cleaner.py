import os
import shutil
import tempfile
from pathlib import Path

def is_file_locked(path: Path) -> bool:
    try:
        with open(path, 'a'):
            return False
    except:
        return True

def clean_temp_dir():
    temp_dir = Path(tempfile.gettempdir())
    deleted = 0
    skipped = []

    print(f"🧹 Cleaning Temp Folder: {temp_dir}\n")

    for item in temp_dir.iterdir():
        try:
            if item.is_file() or item.is_symlink():
                if not is_file_locked(item):
                    item.unlink()
                    print(f"✅ Deleted file: {item.name}")
                    deleted += 1
                else:
                    skipped.append((item.name, "In use or locked"))
            elif item.is_dir():
                try:
                    shutil.rmtree(item)
                    print(f"✅ Deleted folder: {item.name}")
                    deleted += 1
                except Exception as e:
                    skipped.append((item.name, str(e)))
        except Exception as e:
            skipped.append((item.name, str(e)))

    print(f"\n🗑️ Deleted: {deleted} items")
    print(f"🚫 Skipped: {len(skipped)} items")

    if skipped:
        print("\n⚠️ Skipped items:")
        for name, reason in skipped:
            print(f" - {name}: {reason}")

if __name__ == "__main__":
    clean_temp_dir()
