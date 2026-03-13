import tkinter as tk
from tkinter import scrolledtext
from nova_assistant import ask_ai


def show_cute_popup(initial_message):

    root = tk.Tk()
    root.title("CodeBuddy 🤖")
    root.geometry("520x420")
    root.configure(bg="#eef5ff")

    # Title
    title = tk.Label(
        root,
        text="🤖 CodeBuddy",
        font=("Segoe UI", 16, "bold"),
        bg="#eef5ff",
        fg="#2c3e50"
    )
    title.pack(pady=(10, 2))

    subtitle = tk.Label(
        root,
        text="Your AI Debug Companion",
        font=("Segoe UI", 10),
        bg="#eef5ff",
        fg="#5a6a7a"
    )
    subtitle.pack(pady=(0, 10))

    # Chat box
    chat_box = scrolledtext.ScrolledText(
        root,
        height=14,
        width=60,
        wrap="word",
        font=("Segoe UI", 10),
        bg="white",
        fg="#2c3e50",
        bd=1
    )

    chat_box.pack(padx=15, pady=5)
    chat_box.insert(tk.END, "CodeBuddy 🤖:\n" + initial_message + "\n\n")
    chat_box.config(state="disabled")

    # Input frame
    input_frame = tk.Frame(root, bg="#eef5ff")
    input_frame.pack(pady=10)

    user_input = tk.Entry(
        input_frame,
        width=40,
        font=("Segoe UI", 10)
    )
    user_input.pack(side=tk.LEFT, padx=5)

    def send_message():

        question = user_input.get().strip()

        if question == "":
            return

        chat_box.config(state="normal")

        chat_box.insert(tk.END, "You: " + question + "\n")

        response = ask_ai(question)

        chat_box.insert(tk.END, "CodeBuddy 🤖: " + response + "\n\n")

        chat_box.see(tk.END)
        chat_box.config(state="disabled")

        user_input.delete(0, tk.END)

    user_input.bind("<Return>", lambda event: send_message())

    send_button = tk.Button(
        input_frame,
        text="Send",
        command=send_message,
        bg="#4da6ff",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        padx=10
    )

    send_button.pack(side=tk.LEFT)

    close_button = tk.Button(
        root,
        text="Close",
        command=root.destroy,
        font=("Segoe UI", 9),
        bg="#d9e6ff"
    )

    close_button.pack(pady=5)

    root.mainloop()