#!  /usr/bin/env python3

# Creating empty list to store values in
tasks = []

def add_to_tasks(input):
    tasks.append(input)
    print(f'Added {input} to you task list.')

def remove_from_list(input):
    if input in tasks:
        tasks.remove(input)
        print(f'Removed {input} from your task list.')
    else:
        print(f'{input} was not found in your task list.')

def view_list():
    if not tasks:
        print(f'There are currently no tasks in your list.')
    else:
        print('Task list:')
        for task in tasks:
            print(f'f- {task}')




