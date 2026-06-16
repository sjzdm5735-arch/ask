import argparse
from pathlib import Path
from ask.commands import init_project, create_skill, check_skill, export_skill


def main():
    parser = argparse.ArgumentParser(prog="ask", description="Agent Skill Lifecycle Kit")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("init", help="Initialize project scaffolding")

    p_new = sub.add_parser("new", help="Create a new skill scaffold")
    p_new.add_argument("name", help="Skill name")

    p_check = sub.add_parser("check", help="Check a skill for quality issues")
    p_check.add_argument("name", help="Skill directory or path")

    p_export = sub.add_parser("export", help="Export a skill bundle summary")
    p_export.add_argument("name", help="Skill directory or path")

    args = parser.parse_args()
    cwd = Path.cwd()

    if args.command == "init":
        init_project(cwd)
    elif args.command == "new":
        create_skill(cwd, args.name)
    elif args.command == "check":
        check_skill(cwd, args.name)
    elif args.command == "export":
        export_skill(cwd, args.name)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
