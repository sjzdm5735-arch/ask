from pathlib import Path

SKILL_TEMPLATE = """---
name: {name}
description: "TODO: describe when to use this skill"
version: 0.1.0
metadata:
  hermes:
    tags: [{name}]
---

# {title}

## Trigger
Describe when this skill should be used.

## Steps
1. First step
2. Second step
3. Third step

## Pitfalls
- Add known pitfalls here

## Verification
Describe how to validate success.
"""

INIT_FILES = {
    "skills/.gitkeep": "",
    "templates/.gitkeep": "",
    "pitfalls/.gitkeep": "",
}


def init_project(root: Path):
    for rel, content in INIT_FILES.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    print(f"Initialized ASK project in {root}")


def create_skill(root: Path, name: str):
    skills = root / "skills" / name
    skills.mkdir(parents=True, exist_ok=True)
    md = skills / "SKILL.md"
    if not md.exists():
        md.write_text(
            SKILL_TEMPLATE.format(name=name, title=name.replace("-", " ").title()),
            encoding="utf-8",
        )
    print(f"Created skill scaffold: {skills}")


def check_skill(root: Path, name: str):
    md = root / "skills" / name / "SKILL.md"
    if not md.exists():
        raise FileNotFoundError(f"Skill not found: {md}")
    text = md.read_text(encoding="utf-8")
    issues = []
    if "## Steps" not in text:
        issues.append("Missing Steps section")
    if "## Pitfalls" not in text:
        issues.append("Missing Pitfalls section")
    if "## Verification" not in text:
        issues.append("Missing Verification section")
    if "TODO" in text:
        issues.append("Contains TODO placeholder")
    if issues:
        print("Issues found:")
        for i in issues:
            print(f"- {i}")
    else:
        print("Skill looks structurally valid.")


def export_skill(root: Path, name: str):
    md = root / "skills" / name / "SKILL.md"
    if not md.exists():
        raise FileNotFoundError(f"Skill not found: {md}")
    export = root / "dist" / f"{name}.skill-summary.md"
    export.parent.mkdir(parents=True, exist_ok=True)
    export.write_text(md.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Exported summary to {export}")
