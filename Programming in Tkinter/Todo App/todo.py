import tkinter as tk


class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("NYEYA To-Do List")
        self.root.resizable(False,False)
        self.bgcolor = "lightgrey"
        self.root.configure(bg=self.bgcolor)

    def createApp(self):
        # create a label for the task field
        self.task_lbl = tk.Label(root, text="Task:",bg=self.bgcolor)
        self.task_lbl.grid(row=0, column=0, padx=10, pady=10)

        # create an entry field for the task
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)

        # create a button to add the task
        self.add_button = tk.Button(root, text="Add Task",bg="green",fg="white", command=self.add_task)
        self.add_button.grid(row=1, column=0,columnspan=2, sticky=tk.EW,padx=10, pady=10)

        # create a label for the task list
        self.list_lbl = tk.Label(root, text="List of Task:",bg=self.bgcolor)
        self.list_lbl.grid(row=2, column=0, padx=10, pady=10)

        # create a listbox to display the task list
        self.task_list = tk.Listbox(root, width=30, height=10)
        self.task_list.grid(row=3, column=0, columnspan=2, sticky=tk.EW,padx=10, pady=10)

        # create a button to remove the selected task
        self.remove_button = tk.Button(root, text="Remove Task", bg="red",fg="white", command=self.remove_task)
        self.remove_button.grid(row=4, column=1, padx=10, pady=10,sticky="e")

        # initialize instance variable
        self.tasks = []

    def add_task(self):
        task = self.task_entry.get()
        if task!="":
            self.tasks.append(task)
            self.update_list()
            self.clear_fields()

    def update_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)

    def clear_fields(self):
        self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            index = int(selected_task[0])
            del self.tasks[index]
            self.update_list()


# create the main window
root = tk.Tk()

# Instantiate the todo list app
todo_list = Todo(root)
todo_list.createApp()

# run the main event loop
root.mainloop()
