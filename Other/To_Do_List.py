import sys

todo_list = []

def show_help():
    print("\nCommands:")
    print("  add <task>     → Add a task")
    print("  list           → Show all tasks")
    print("  remove <index> → Remove a task by index")
    print("  help           → Show commands")
    print("  exit           → Exit the app")

def add_task(task):
    todo_list.append(task)
    print(f"✅ Task added: {task}")

def list_tasks():
    if not todo_list:
        print("📝 No tasks yet!")
    else:
        for i, task in enumerate(todo_list):
            print(f"{i + 1}. {task}")

def remove_task(index):
    try:
        task = todo_list.pop(index - 1)
        print(f"❌ Task removed: {task}")
    except IndexError:
        print("⚠️ Invalid task number.")

# Run the CLI loop
if __name__ == "__main__":
    print("🛠️ Simple To-Do CLI App")
    show_help()
    
    while True:
        command = input("\n> ").strip().split()
        
        if not command:
            continue

        cmd = command[0]
        
        if cmd == "add":
            task = " ".join(command[1:])
            if task:
                add_task(task)
            else:
                print("⚠️ Please enter a task.")
        elif cmd == "list":
            list_tasks()
        elif cmd == "remove":
            if len(command) > 1 and command[1].isdigit():
                remove_task(int(command[1]))
            else:
                print("⚠️ Please provide a valid index.")
        elif cmd == "help":
            show_help()
        elif cmd == "exit":
            print("👋 Exiting. Bye!")
            sys.exit()
        else:
            print("❓ Unknown command. Type 'help' to see commands.")

