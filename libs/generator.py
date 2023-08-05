import random
import string
import tkinter as tk
import pyperclip

__VERSION__= "2.0.2"  # major version . minor version . patch version

def generate_password() -> None:
    """Password generator Function"""

    chars = ""
    password_length = int(length_spinbox.get())

    if include_lower_var.get():
        chars += string.ascii_lowercase
    if include_upper_var.get():
        chars += string.ascii_uppercase
    if include_digits_var.get():
        chars += string.digits
    if include_symbols_var.get():
        chars += string.punctuation
    if chars:
        if password_length == 8 or password_length > 8 and password_length < 64 or password_length == 64:
            password = ''.join(random.choice(chars) for i in range(password_length))
            password_output.configure(text=password)
            copied_label.configure(text="Password copied in clipboard")
            pyperclip.copy(password)
        else:
            password_output.configure(text="Password length need to be between 8 and 64")
    else:
        password_output.configure(text="No characters selected")

if __name__ == "__main__":
    win = tk.Tk()
    win.title(f"Password Generator {__VERSION__}")

    length_label = tk.Label(win, text="Password length:")
    length_label.pack()

    length_spinbox = tk.Spinbox(win, from_=8, to=64, increment=1)
    length_spinbox.pack()

    include_lower_var = tk.BooleanVar()
    include_lower_chk = tk.Checkbutton(win, text="Include lowercase", variable=include_lower_var)
    include_lower_chk.pack()

    include_upper_var = tk.BooleanVar()
    include_upper_chk = tk.Checkbutton(win, text="Include uppercase", variable=include_upper_var)
    include_upper_chk.pack()

    include_digits_var = tk.BooleanVar()
    include_digits_chk = tk.Checkbutton(win, text="Include digits", variable=include_digits_var)
    include_digits_chk.pack()

    include_symbols_var = tk.BooleanVar()
    include_symbols_chk = tk.Checkbutton(win, text="Include symbols", variable=include_symbols_var)
    include_symbols_chk.pack()

    generate_button = tk.Button(win, text="Generate password", command=generate_password)
    generate_button.pack()

    password_output_label = tk.Label(win, text="Password:")
    password_output_label.pack()

    password_output = tk.Label(win, text="")
    password_output.pack()

    copied_label = tk.Label(win, text="")
    copied_label.pack()
    win.mainloop()
