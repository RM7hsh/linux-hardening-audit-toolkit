import argparse
from pathlib import Path

from lhat.runner import run_all_checks, to_json, to_markdown


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Linux hardening audit toolkit")
    parser.add_argument("--root", default="/", help="Root directory to inspect")
    parser.add_argument("--format", choices=["json", "markdown"], default="markdown")
    parser.add_argument("--output", help="Write report to file")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    results = run_all_checks(root=Path(args.root))
    output = to_json(results) if args.format == "json" else to_markdown(results)
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        print(output)


if __name__ == "__main__":
    main()
