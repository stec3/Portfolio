#!/usr/bin/env python3

def print_menu() -> None:
    print("\n=== Todo Manager ===")
    print("1) Add task")
    print("2) List tasks")
    print("3) Remove task")
    print("4) Exit")

def add_task(tasks: list[dict]) -> None:
    title = input("Task title: ").strip()
    if not title:
        print("Empty title. Nothing added.")
        return
    tasks.append({"title": title, "done": False})
    print("Task added.")

def list_tasks(tasks: list[dict]) -> None:
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "✓" if t["done"] else " "
        print(f"{i}. [{status}] {t['title']}")

def remove_task(tasks: list[dict]) -> None:
    if not tasks:
        print("No tasks to remove.")
        return
    list_tasks(tasks)
    raw = input("Number to remove: ").strip()
    if not raw.isdigit():
        print("Please enter a number.")
        return
    idx = int(raw)
    if idx < 1 or idx > len(tasks):
        print("Invalid number.")
        return
    removed = tasks.pop(idx - 1)
    print(f"Removed: {removed['title']}")

def main() -> None:
    tasks: list[dict] = []
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
