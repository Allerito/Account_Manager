from pathlib import Path
import os

import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

import libs.operations as op

__version__ = "2.1.0"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(os.path.expanduser(r"~\Documents\GitHub\Account_Manager\assets\frame0"))

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def form_data()-> None:
    """Take account infos"""
    site = str(entry_1.get())
    username = str(entry_3.get())
    email = str(entry_4.get())
    password = str(entry_2.get())
    op.check_data(site, username, email, password)

def run_pwd_generator() -> None:
    """Run password generator file"""
    with open("libs\generator.py", encoding='utf-8') as f:
        exec(f.read())

if __name__ == "__main__":
    op.read_json_data()

    window = Tk()
    window.title(f"Account Manager {__version__}")

    window.geometry("751x327")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 327,
        width = 751,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        51.0,
        86.0,
        anchor="nw",
        text="Username:",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        51.0,
        162.0,
        anchor="nw",
        text="Password:",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        77.0,
        124.0,
        anchor="nw",
        text="Email:",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        88.0,
        48.0,
        anchor="nw",
        text="Site:",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        216.0,
        56.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=126.0,
        y=45.0,
        width=180.0,
        height=21.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        216.0,
        169.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=126.0,
        y=158.0,
        width=180.0,
        height=21.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        216.0,
        93.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=126.0,
        y=82.0,
        width=180.0,
        height=21.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        216.0,
        131.5,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=126.0,
        y=120.0,
        width=180.0,
        height=21.0
    )

    #Save button
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=form_data,
        relief="flat"
    )
    button_1.place(
        x=17.0,
        y=221.0,
        width=293.0,
        height=60.0
    )

    #Password Generator
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=run_pwd_generator,
        relief="flat"
    )
    button_2.place(
        x=330.0,
        y=146.0,
        width=45.0,
        height=46.0
    )


    #Settings
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=617.0,
        y=143.0,
        width=76.0,
        height=75.0
    )

    #Accounts
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: os.system(op.ACCOUNTS_PATH),
        relief="flat"
    )
    button_4.place(
        x=617.0,
        y=45.0,
        width=76.0,
        height=75.0
    )
    window.resizable(False, False)
    window.mainloop()
