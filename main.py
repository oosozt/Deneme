import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--add', help='Add an item to the to-do list')
parser.add_argument('--remove', help='Remove an item from the to-do list')
parser.add_argument('--list', help='name of the list')
parser.add_argument('--view', action='store_true', help='View the current to-do list')
parser.add_argument('--sort', choices=['priority', 'alphabetical'], help='Sort the to-do list by priority or alphabetically')
parser.add_argument('--complete', help='Item is marked completed')
parser.add_argument('--list_completed', help='List is marked completed')

args = parser.parse_args()
list_name = args.list

if not list_name:
    list_name = "todolo"

if args.add:
    with open(f"{list_name}.txt", 'a') as f:
        f.write(args.add + '\n')

if args.remove:
    try:
        with open(f"{list_name}.txt", 'r') as f:
            lines = f.readlines()
        if args.remove+'\n' not in lines:
            raise ValueError
        lines = [line for line in lines if line.strip() != args.remove]
    except FileNotFoundError:
        print(f"{list_name} not found.")
        exit()
    except ValueError:
        print(f"{args.remove} not found in the list")
        exit()
    with open(f"{list_name}.txt", 'w') as f:
        f.writelines(lines)

if args.view:
    try:
        with open(f"{list_name}.txt", 'r') as f:
            todo_list = f.read()
    except FileNotFoundError:
        print(f"{list_name} not found.")
        exit()
    print(todo_list)
if args.sort:
    try:
        with open(f"{list_name}.txt", 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"{list_name} not found.")
        exit()

    sorted_lines = sorted(lines, key=lambda x: x.lower())

    with open(f"{list_name}.txt", 'w') as f:
        f.writelines(sorted_lines)
if args.complete:
    try:
        with open(f"{list_name}.txt", 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"{list_name} not found.")
        exit()
    for i,line in enumerate(lines):
        if line.strip().split('|')[0] == args.complete:
            lines[i] = f"{line.strip()}|completed\n"
    with open(f"{list_name}.txt", 'w') as f:
        f.writelines(lines)
if args.list_completed:
    try:
        with open(f"{list_name}.txt", 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"{list_name} not found.")
        exit()
    completed_tasks = [line for line in lines if "completed" in line]
    for task in completed_tasks:
        print(task)
