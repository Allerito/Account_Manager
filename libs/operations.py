import json
import os
import tkinter as tk
from tkinter import messagebox, filedialog

DOCS_FOLDER = os.path.expanduser(r"~\Documenti\accounts.json")
ACCOUNTS_PATH = DOCS_FOLDER

def file_path():
    # folder_selected = filedialog.askdirectory()
    # if folder_selected != DOCS_FOLDER:
    #     ACCOUNTS_PATH = folder_selected
    # ACCOUNTS_PATH += r"\accounts.json"
    return

def read_json_data()-> list[dict] or None:
    """Read JSON data and upload data on temp_account"""
    local_accounts=[]
    try:
        with open(ACCOUNTS_PATH,"r", encoding="utf-8") as a:
            local_accounts = json.load(a)
    except FileNotFoundError:
        file_path()
        with open(ACCOUNTS_PATH, "w", encoding="utf-8") as a:
            a.write("[]")
    except json.JSONDecodeError:
        with open(ACCOUNTS_PATH, "r", encoding="utf-8") as a:
            if a.read() == "":
                answer = tk.messagebox.askokcancel(title="Empty file", message="Your file is empty. Are you sure to overwrite the file?", icon="warning")

                if not answer:
                    tk.messagebox.showinfo(title="Empty file", message="Your file wasn't modified", icon="info")
                    return
    return local_accounts

def save_data(site: str, username: str, email: str, password: str)-> None:
    """Save data inside JSON file

    :param site: Account site
    :type site: string
    :param username: Account username
    :type username: string
    :param email: Account email
    :type email: string
    :param password: Account password
    :type password: string
    """
    local_accounts = read_json_data()
    temp_account = {
        "site":site,
        "username":username,
        "email":email,
        "password":password
    }
    for account in local_accounts:
        if temp_account == account:
            answer = tk.messagebox.askokcancel(title="Another account exist", message="There is another account associated to this site, do you want to create another account?", icon="warning")
            if not answer:
                tk.messagebox.showinfo(title="Another account exist", message="The account wasn't create", icon="info")
                return

    local_accounts.append(temp_account)
    json_object = json.dumps(local_accounts, indent=4)
    with open(ACCOUNTS_PATH, "w", encoding='utf-8') as outfile:
        outfile.write(json_object)

if __name__=="__main__":
    read_json_data()
