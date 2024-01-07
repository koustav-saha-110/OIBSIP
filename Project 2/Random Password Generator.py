import string
import random
import tkinter as tk


def pass_generator(num):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(all_chars, num))
    return password


def generate_password():
    length = int(length_entry.get())
    password = pass_generator(length)
    password_label.config(text=f"Generated Password: {password}")


root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")
root.configure(bg="grey")
frame = tk.Frame(root, bg="#ffffff")
frame.pack(expand=True)

length_label = tk.Label(frame, text="Enter the length of the password: ", bg="#ffffff")
length_label.pack()

length_entry = tk.Entry(frame)
length_entry.pack()
generate_button = tk.Button(frame, text="Generate Password", command=generate_password, bg="#4caf50", fg="black")
generate_button.pack()
password_label = tk.Label(frame, text="Generated Password: ", bg="#ffffff")
password_label.pack()

root.mainloop()
