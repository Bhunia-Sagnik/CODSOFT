import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("500x400")

        self.tasks = []

        # Entry for adding tasks
        self.taskEntry = tk.Entry(root, width=40)
        self.taskEntry.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky='ew')

        # Button to add a task
        self.addButton = tk.Button(root, text="Add Task", command=self.addTask, bg="#66c2ff", fg="white")
        self.addButton.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky='ew')

        # Listbox to display tasks
        self.taskListbox = tk.Listbox(root, width=40, height=10)
        self.taskListbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

        # Button to mark a task as completed
        self.completeButton = tk.Button(root, text="Mark Completed", command=self.markCompleted, bg="#99ff99", fg="black")
        self.completeButton.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

        # Button to update a task
        self.updateButton = tk.Button(root, text="Update Task", command=self.updateTask, bg="#ffcc66", fg="black")
        self.updateButton.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

        # Button to delete a task
        self.deleteButton = tk.Button(root, text="Delete Task", command=self.deleteTask, bg="#ff6666", fg="white")
        self.deleteButton.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky='ew')

        for child in root.winfo_children():
            child.grid_configure(pady=5)

        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(2, weight=1)

    def addTask(self):
        task = self.taskEntry.get()
        if task:
            self.tasks.append({'text': task, 'completed': False})
            self.taskListbox.insert(tk.END, task)
            self.taskEntry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def markCompleted(self):
        selected_index = self.taskListbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            if not task['completed']:
                task['completed'] = True
                self.taskListbox.itemconfig(index, {'bg': '#cccccc', 'fg': 'green'})
                completed_task_text = f"\u2713 {task['text']}"
                self.taskListbox.delete(index)
                self.taskListbox.insert(index, completed_task_text)
                messagebox.showinfo("Task Completed", f'Task "{task["text"]}" marked as completed.')
            else:
                messagebox.showinfo("Info", "Task already marked as completed.")
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def updateTask(self):
        selected_index = self.taskListbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            updated_task = self.taskEntry.get()
            if updated_task:
                task['text'] = updated_task
                self.taskListbox.delete(index)
                self.taskListbox.insert(index, task['text'])
                self.taskEntry.delete(0, tk.END)
                messagebox.showinfo("Task Updated", f'Task updated successfully.')
            else:
                messagebox.showwarning("Warning", "Please enter a new task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def deleteTask(self):
        selected_index = self.taskListbox.curselection()
        if selected_index:
            index = selected_index[0]
            deleted_task = self.tasks.pop(index)
            self.taskListbox.delete(index)
            messagebox.showinfo("Task Deleted", f'Task "{deleted_task["text"]}" deleted successfully.')
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
