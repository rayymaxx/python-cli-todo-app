# This file runs the CLI and handles user commands

import argparse
from datetime import date
from task import Task
from utils import load_tasks, save_tasks, generate_task_id

def add_task(title, description, due_date=None):
    tasks = load_tasks()
    new_id = generate_task_id(tasks)
    task = Task(new_id, title, description, due_date, completed=False)
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added!")

def list_tasks(today_only=False):
    tasks = load_tasks()
    if today_only:
        today = str(date.today())
        tasks = [task for task in tasks if task.due_date == today]
    for task in tasks:
        print(task)

def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            task.mark_complete()
            save_tasks(tasks)
            print(f"Task {task_id} marked as complete.")
            return
    print(f"No task with ID {task_id} found.")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task.id != task_id]
    save_tasks(new_tasks)
    print(f"Task {task_id} deleted.")

def main():
    parser = argparse.ArgumentParser(
        description="CLI for the todo list app"
        )
    subparsers = parser.add_subparsers(dest="command")

    parser_add = subparsers.add_parser("add")
    parser_add.add_argument("title")
    parser_add.add_argument("description")
    parser_add.add_argument("--due", dest="due_date")

    parser_list = subparsers.add_parser("list")
    parser_list.add_argument("--today", action="store_true")

    parser_complete = subparsers.add_parser("complete")
    parser_complete.add_argument("id", type=int)

    parser_delete = subparsers.add_parser("delete")
    parser_delete.add_argument("id", type=int)

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title, args.description, args.due_date)
    elif args.command == "list":
        list_tasks(args.today)
    elif args.command == "complete":
        complete_task(args.id)
    elif args.command == "delete":
        delete_task(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

