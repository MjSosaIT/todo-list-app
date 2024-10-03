import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("To-Do List")
window.configure(bg="lightblue")

tasks = []

def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_task_list()
    task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_task_list()
    except IndexError:
        pass

def edit_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task = tasks[selected_task_index]
        task_entry.delete(0, tk.END)
        task_entry.insert(0, task)
        tasks.pop(selected_task_index)
        update_task_list()
    except IndexError:
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
        update_task_list()
    except FileNotFoundError:
        pass

def update_task_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Create Widgets
task_entry = tk.Entry(window, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(window, text="Add Task", command=add_task, bg="green", fg="white")
add_button.pack()

delete_button = tk.Button(window, text="Delete Task", command=delete_task, bg="red", fg="white")
delete_button.pack()

edit_button = tk.Button(window, text="Edit Task", command=edit_task, bg="yellow", fg="black")
edit_button.pack()

save_button = tk.Button(window, text="Save Tasks", command=save_tasks, bg="blue", fg="white")
save_button.pack()

listbox = tk.Listbox(window, height=10, width=45, bg="white", fg="black", font=("Arial", 12))
listbox.pack(pady=10)

load_tasks()
window.mainloop()
