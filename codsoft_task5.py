import tkinter as tk
from tkinter import messagebox
import json
import os

root = tk.Tk()
root.title("Contact Book")
root.geometry("520x520")
root.configure(bg="#1f1f2e")

CONTACTS_FILE = "contacts.json"
contacts = {}

def load_contacts():
    global contacts
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
                contacts = json.load(f)
        except Exception:
            contacts = {}
    else:
        contacts = {}

def save_contacts():
    try:
        with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=2)
    except Exception:
        messagebox.showerror("Error", "Could not save contacts")

def refresh_listbox(filter_text=""):
    listbox.delete(0, tk.END)
    for name in sorted(contacts.keys(), key=str.lower):
        if filter_text.lower() in name.lower():
            listbox.insert(tk.END, name)

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    mobile = mobile_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Warning", "Name and Phone required")
        return

    contacts[name] = {"phone": phone, "email": email, "mobile": mobile}
    save_contacts()
    refresh_listbox(search_entry.get())
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)

def view_contact():
    try:
        selected = listbox.curselection()[0]
        name = listbox.get(selected)
        info = contacts.get(name, {})
        phone = info.get("phone", "")
        email = info.get("email", "")
        mobile = info.get("mobile", "")
        messagebox.showinfo("Contact Info", f"Name: {name}\nPhone: {phone}\nMobile: {mobile}\nEmail: {email}")
    except Exception:
        messagebox.showwarning("Warning", "Select a contact")

def delete_contact():
    try:
        selected = listbox.curselection()[0]
        name = listbox.get(selected)
        if messagebox.askyesno("Delete", f"Delete contact '{name}'?"):
            contacts.pop(name, None)
            save_contacts()
            refresh_listbox(search_entry.get())
    except Exception:
        messagebox.showwarning("Warning", "Select a contact")

def edit_contact():
    try:
        selected = listbox.curselection()[0]
        name = listbox.get(selected)
        info = contacts.get(name, {})
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, info.get("phone", ""))
        email_entry.delete(0, tk.END)
        email_entry.insert(0, info.get("email", ""))
        mobile_entry.delete(0, tk.END)
        mobile_entry.insert(0, info.get("mobile", ""))
        # remove old key on save if name changed
        def save_edit():
            new_name = name_entry.get().strip()
            new_phone = phone_entry.get().strip()
            new_email = email_entry.get().strip()
            new_mobile = mobile_entry.get().strip()
            if not new_name or not new_phone:
                messagebox.showwarning("Warning", "Name and Phone required")
                return
            if new_name != name:
                contacts.pop(name, None)
            contacts[new_name] = {"phone": new_phone, "email": new_email, "mobile": new_mobile}
            save_contacts()
            refresh_listbox(search_entry.get())
            save_btn.destroy()

        save_btn = tk.Button(root, text="Save Edit", bg="#FFA000", fg="white", width=12, command=save_edit)
        save_btn.pack(pady=5)
    except Exception:
        messagebox.showwarning("Warning", "Select a contact")

def on_search_change(*_):
    refresh_listbox(search_entry.get())

tk.Label(root, text="CONTACT BOOK",
         bg="#1f1f2e", fg="white",
         font=("Segoe UI", 16, "bold")).pack(pady=10)

search_frame = tk.Frame(root, bg="#1f1f2e")
search_frame.pack(pady=5)
tk.Label(search_frame, text="Search:", bg="#1f1f2e", fg="white").pack(side=tk.LEFT, padx=5)
search_entry = tk.Entry(search_frame, font=("Segoe UI", 11))
search_entry.pack(side=tk.LEFT, padx=5)
search_entry.bind("<KeyRelease>", on_search_change)

form_frame = tk.Frame(root, bg="#1f1f2e")
form_frame.pack(pady=8)

name_entry = tk.Entry(form_frame, font=("Segoe UI", 11), width=30)
name_entry.grid(row=0, column=0, padx=5, pady=3)

phone_entry = tk.Entry(form_frame, font=("Segoe UI", 11), width=30)
phone_entry.grid(row=1, column=0, padx=5, pady=3)

mobile_entry = tk.Entry(form_frame, font=("Segoe UI", 11), width=30)
mobile_entry.grid(row=2, column=0, padx=5, pady=3)

email_entry = tk.Entry(form_frame, font=("Segoe UI", 11), width=30)
email_entry.grid(row=3, column=0, padx=5, pady=3)

buttons_frame = tk.Frame(root, bg="#1f1f2e")
buttons_frame.pack(pady=5)

tk.Button(buttons_frame, text="Add Contact",
          bg="#4CAF50", fg="white",
          width=12, command=add_contact).pack(side=tk.LEFT, padx=4)

tk.Button(buttons_frame, text="View",
          bg="#2196F3", fg="white",
          width=8, command=view_contact).pack(side=tk.LEFT, padx=4)

tk.Button(buttons_frame, text="Edit",
          bg="#FFA000", fg="white",
          width=8, command=edit_contact).pack(side=tk.LEFT, padx=4)

tk.Button(buttons_frame, text="Delete",
          bg="#f44336", fg="white",
          width=8, command=delete_contact).pack(side=tk.LEFT, padx=4)

listbox = tk.Listbox(root, font=("Segoe UI", 11),
                     bg="#2e2e40", fg="white",
                     width=50, height=12)
listbox.pack(pady=12)

load_contacts()
refresh_listbox()

root.mainloop()
