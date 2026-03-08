import tkinter as tk
from tkinter import messagebox
import random
import string
import secrets
try:
    import pyperclip
except Exception:
    pyperclip = None

root = tk.Tk()
root.title("Password Generator")
root.geometry("450x450")
root.configure(bg="#1f1f2e")
root.resizable(False, False)

# Title
tk.Label(root, text="PASSWORD GENERATOR",
         bg="#1f1f2e", fg="white",
         font=("Segoe UI", 18, "bold")).pack(pady=15)

# Password Length Frame
length_frame = tk.Frame(root, bg="#1f1f2e")
length_frame.pack(pady=10)

tk.Label(length_frame, text="Password Length:",
         bg="#1f1f2e", fg="white",
         font=("Segoe UI", 11)).pack(side=tk.LEFT, padx=5)

entry = tk.Entry(length_frame, font=("Segoe UI", 11), width=10)
entry.pack(side=tk.LEFT, padx=5)
entry.insert(0, "12")

# Character Options Frame
options_frame = tk.Frame(root, bg="#1f1f2e")
options_frame.pack(pady=10)

tk.Label(options_frame, text="Character Types:",
         bg="#1f1f2e", fg="white",
         font=("Segoe UI", 10)).pack(anchor=tk.W, padx=20)

include_lowercase = tk.BooleanVar(value=True)
include_uppercase = tk.BooleanVar(value=True)
include_digits = tk.BooleanVar(value=True)
include_special = tk.BooleanVar(value=True)

tk.Checkbutton(options_frame, text="Lowercase (a-z)",
               variable=include_lowercase, bg="#1f1f2e",
               fg="white", selectcolor="#1f1f2e",
               font=("Segoe UI", 9)).pack(anchor=tk.W, padx=40)

tk.Checkbutton(options_frame, text="Uppercase (A-Z)",
               variable=include_uppercase, bg="#1f1f2e",
               fg="white", selectcolor="#1f1f2e",
               font=("Segoe UI", 9)).pack(anchor=tk.W, padx=40)

tk.Checkbutton(options_frame, text="Digits (0-9)",
               variable=include_digits, bg="#1f1f2e",
               fg="white", selectcolor="#1f1f2e",
               font=("Segoe UI", 9)).pack(anchor=tk.W, padx=40)

tk.Checkbutton(options_frame, text="Special (!@#$%...)",
               variable=include_special, bg="#1f1f2e",
               fg="white", selectcolor="#1f1f2e",
               font=("Segoe UI", 9)).pack(anchor=tk.W, padx=40)

def generate():
    try:
        length = int(entry.get())
        
        if length < 4:
            messagebox.showwarning("Invalid Length", "Password length must be at least 4 characters")
            return
        
        if length > 128:
            messagebox.showwarning("Invalid Length", "Password length cannot exceed 128 characters")
            return
        
        pools = []
        if include_lowercase.get():
            pools.append(string.ascii_lowercase)
        if include_uppercase.get():
            pools.append(string.ascii_uppercase)
        if include_digits.get():
            pools.append(string.digits)
        if include_special.get():
            pools.append(string.punctuation)

        if not pools:
            messagebox.showwarning("No Options", "Please select at least one character type")
            return

        # Ensure at least one char from each selected pool
        password_chars = [secrets.choice(pool) for pool in pools]

        remaining = length - len(password_chars)
        all_chars = ''.join(pools)
        for _ in range(remaining):
            password_chars.append(secrets.choice(all_chars))

        # shuffle securely
        sysrnd = random.SystemRandom()
        sysrnd.shuffle(password_chars)
        password = ''.join(password_chars)
        result.set(password)
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length")

def copy_password():
    password = result.get()
    if password and password != "Click Generate to create a password":
        try:
            if pyperclip is None:
                raise RuntimeError
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        except:
            messagebox.showerror("Error", "Could not copy to clipboard. Install 'pyperclip' or copy manually.")
    else:
        messagebox.showwarning("No Password", "Please generate a password first")

# Buttons Frame
button_frame = tk.Frame(root, bg="#1f1f2e")
button_frame.pack(pady=15)

tk.Button(button_frame, text="Generate Password",
          bg="#9C27B0", fg="white", activebackground="#7B1FA2",
          font=("Segoe UI", 11, "bold"), width=18,
          command=generate).pack(side=tk.LEFT, padx=5)

tk.Button(button_frame, text="Copy",
          bg="#4CAF50", fg="white", activebackground="#388E3C",
          font=("Segoe UI", 11, "bold"), width=8,
          command=copy_password).pack(side=tk.LEFT, padx=5)

# Result Display
result = tk.StringVar(value="Click Generate to create a password")
result_label = tk.Label(root, textvariable=result,
                        bg="#2a2a3e", fg="#4CAF50",
                        wraplength=400, justify=tk.CENTER,
                        font=("Courier New", 11), relief=tk.SUNKEN,
                        padx=10, pady=15)
result_label.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

root.mainloop()
