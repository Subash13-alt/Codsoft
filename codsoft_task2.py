import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("350x420")
root.configure(bg="#1f1f2e")

def calculate():
    try:
        a_text = entry1.get().strip()
        b_text = entry2.get().strip()
        a = float(a_text)
        b = float(b_text)
        op = operator.get()

        if op == "+":
            value = a + b
        elif op == "-":
            value = a - b
        elif op == "*":
            value = a * b
        elif op == "/":
            value = a / b
        elif op == "%":
            value = a % b
        elif op == "^":
            value = a ** b
        else:
            result.set("Unknown op")
            return

        # show integer when possible
        if value == int(value):
            result.set(str(int(value)))
        else:
            result.set(str(round(value, 10)).rstrip('0').rstrip('.'))

    except ZeroDivisionError:
        result.set("Division by 0")
    except ValueError:
        result.set("Invalid number")
    except Exception:
        result.set("Error")

def clear_all():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.set("")

tk.Label(root, text="CALCULATOR", bg="#1f1f2e",
         fg="white", font=("Segoe UI", 16, "bold")).pack(pady=10)

entry1 = tk.Entry(root, font=("Segoe UI", 12))
entry1.pack(pady=5)

entry2 = tk.Entry(root, font=("Segoe UI", 12))
entry2.pack(pady=5)

operator = tk.StringVar()
operator.set("+")

tk.OptionMenu(root, operator, "+", "-", "*", "/", "%", "^").pack(pady=5)

btn_frame = tk.Frame(root, bg="#1f1f2e")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Calculate", bg="#2196F3",
          fg="white", width=12, command=calculate).pack(side=tk.LEFT, padx=5)

tk.Button(btn_frame, text="Clear", bg="#f44336",
          fg="white", width=8, command=clear_all).pack(side=tk.LEFT, padx=5)

result = tk.StringVar()
tk.Label(root, textvariable=result,
         bg="#1f1f2e", fg="#4CAF50",
         font=("Segoe UI", 14)).pack(pady=20)

root.mainloop()
