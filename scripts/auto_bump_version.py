import re
from pathlib import Path
import subprocess

control_file = Path.home() / "automation_project/build_deb/DEBIAN/control"
readme_file = Path.home() / "automation_project/README.md"

def bump_version(version):
    major, minor, patch = map(int, version.split('.'))
    patch += 1
    return f"{major}.{minor}.{patch}"

# --- Update control file ---
text = control_file.read_text()
match = re.search(r"Version:\s*(\d+\.\d+\.\d+)", text)
if match:
    old_version = match.group(1)
    new_version = bump_version(old_version)
    control_file.write_text(re.sub(old_version, new_version, text))
    print(f"✅ Updated control version: {old_version} → {new_version}")
else:
    raise ValueError("Version field not found in control file.")

# --- Update README.md badge ---
readme_text = readme_file.read_text()
readme_new = re.sub(r"version-\d+\.\d+\.\d+", f"version-{new_version}", readme_text)
readme_file.write_text(readme_new)
print("✅ Updated README.md version badge")

# --- Commit & push ---
subprocess.run(["git", "add", "."], cwd=Path.home() / "automation_project")
subprocess.run(["git", "commit", "-m", f"🔼 Auto bump to v{new_version}"], cwd=Path.home() / "automation_project")
subprocess.run(["git", "push"], cwd=Path.home() / "automation_project")
