import json
import sys
from pathlib import Path


def validate(payload):
    errors = []
    tasks = payload.get("tasks")

    if not isinstance(tasks, list):
        errors.append("tasks must be a list")
        return errors

    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            errors.append(f"tasks[{index}] must be an object")
            continue

        title = task.get("title")
        if not isinstance(title, str) or not title.strip():
            errors.append(f"tasks[{index}].title must be a non-empty string")

        if not isinstance(task.get("done"), bool):
            errors.append(f"tasks[{index}].done must be a boolean")

    return errors


def main(argv):
    if len(argv) != 2:
        print(json.dumps({"ok": False, "errors": ["usage: python validate_todo.py <todo.json>"]}, sort_keys=True))
        return 1

    todo_path = Path(argv[1])
    try:
        payload = json.loads(todo_path.read_text(encoding="utf-8"))
    except OSError as error:
        print(json.dumps({"ok": False, "errors": [f"cannot read file: {error}"]}, sort_keys=True))
        return 1
    except json.JSONDecodeError as error:
        print(json.dumps({"ok": False, "errors": [f"invalid json: {error.msg}"]}, sort_keys=True))
        return 1

    errors = validate(payload)
    print(json.dumps({"ok": not errors, "errors": errors}, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))