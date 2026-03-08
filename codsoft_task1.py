import tkinter as tk
from tkinter import messagebox
import json
import os

root = tk.Tk()
root.title("To-Do List")
root.geometry("420x520")
root.configure(bg="#1f1f2e")

TODO_FILE = "todo.json"
tasks = []

def load_tasks():
    global tasks
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, "r", encoding="utf-8") as f:
                tasks = json.load(f)
        except Exception:
            tasks = []
    else:
        tasks = []

def save_tasks():
    try:
        with open(TODO_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2)
    except Exception:
        messagebox.showerror("Error", "Could not save tasks")

def refresh_listbox():
    listbox.delete(0, tk.END)
    for t in tasks:
        prefix = "[x] " if t.get("done") else "[ ] "
        listbox.insert(tk.END, prefix + t.get("text", ""))

def add_task():
    text = entry.get().strip()
    if text:
        tasks.append({"text": text, "done": False})
        entry.delete(0, tk.END)
        save_tasks()
        refresh_listbox()
    else:
        messagebox.showwarning("Warning", "Enter a task")

def delete_task():
    try:
        idx = listbox.curselection()[0]
        tasks.pop(idx)
        save_tasks()
        refresh_listbox()
    except Exception:
        messagebox.showwarning("Warning", "Select a task")

def toggle_task(event=None):
    try:
        idx = listbox.curselection()[0]
        tasks[idx]["done"] = not tasks[idx].get("done", False)
        save_tasks()
        refresh_listbox()
    except Exception:
        pass

def edit_task():
    try:
        idx = listbox.curselection()[0]
        current = tasks[idx]
        entry.delete(0, tk.END)
        entry.insert(0, current.get("text", ""))

        def save_edit():
            new_text = entry.get().strip()
            if not new_text:
                messagebox.showwarning("Warning", "Task cannot be empty")
                return
            tasks[idx]["text"] = new_text
            save_tasks()
            refresh_listbox()
            save_btn.destroy()

        save_btn = tk.Button(root, text="Save Edit", bg="#FFA000", fg="white", width=12, command=save_edit)
        save_btn.pack(pady=5)
    except Exception:
        messagebox.showwarning("Warning", "Select a task")

def clear_all():
    if messagebox.askyesno("Clear All", "Delete all tasks?"):
        tasks.clear()
        save_tasks()
        refresh_listbox()

tk.Label(root, text="TO-DO LIST", bg="#1f1f2e",
         fg="white", font=("Segoe UI", 16, "bold")).pack(pady=10)

entry = tk.Entry(root, font=("Segoe UI", 12), width=30)
entry.pack(pady=10)

buttons_frame = tk.Frame(root, bg="#1f1f2e")
buttons_frame.pack(pady=5)

tk.Button(buttons_frame, text="Add Task", bg="#4CAF50",
          fg="white", width=12, command=add_task).pack(side=tk.LEFT, padx=6)

tk.Button(buttons_frame, text="Edit Task", bg="#FFA000",
          fg="white", width=10, command=edit_task).pack(side=tk.LEFT, padx=6)

tk.Button(buttons_frame, text="Delete Task", bg="#f44336",
          fg="white", width=12, command=delete_task).pack(side=tk.LEFT, padx=6)

listbox = tk.Listbox(root, font=("Segoe UI", 12),
                     bg="#2e2e40", fg="white",
                     width=40, height=12)
listbox.pack(pady=12)
listbox.bind('<Double-Button-1>', toggle_task)

tk.Button(root, text="Clear All", bg="#9E9E9E", fg="white", width=12, command=clear_all).pack(pady=6)

load_tasks()
refresh_listbox()

root.mainloop()
