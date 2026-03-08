import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("420x460")
root.configure(bg="#1f1f2e")

user_score = 0
computer_score = 0

def play(user):
    global user_score, computer_score
    choices = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choices)

    if user == computer:
        outcome = "It's a Tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        outcome = "You Win!"
        user_score += 1
    else:
        outcome = "You Lose!"
        computer_score += 1

    result.set(f"Computer: {computer}\n{outcome}\n\nScore — You: {user_score}  Computer: {computer_score}")

def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result.set("Scores reset. Play again!")

tk.Label(root, text="ROCK PAPER SCISSORS",
         bg="#1f1f2e", fg="white",
         font=("Segoe UI", 16, "bold")).pack(pady=20)

btn_frame = tk.Frame(root, bg="#1f1f2e")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Rock",
          bg="#2196F3", fg="white",
          width=15, command=lambda: play("Rock")).pack(pady=5)

tk.Button(btn_frame, text="Paper",
          bg="#4CAF50", fg="white",
          width=15, command=lambda: play("Paper")).pack(pady=5)

tk.Button(btn_frame, text="Scissors",
          bg="#f44336", fg="white",
          width=15, command=lambda: play("Scissors")).pack(pady=5)

result = tk.StringVar()
tk.Label(root, textvariable=result,
         bg="#1f1f2e", fg="#FFD700",
         font=("Segoe UI", 12)).pack(pady=20)

tk.Button(root, text="Reset Scores", bg="#9E9E9E", fg="white", width=15, command=reset_scores).pack(pady=6)

root.mainloop()
