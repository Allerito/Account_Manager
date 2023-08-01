import json
import os
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.simpledialog import askstring
from cryptography.fernet import Fernet

ACCOUNTS_PATH = os.path.expanduser(r"~\Documents\accounts.json")
READER=["notepad", "vscode", "notepad++"]
KEY = "admin"
FERNET = Fernet(KEY)

def encrypt_file(json_file: str)-> str:
    """Encrypt JSON file for protect your password

    :param json_object: data to encrypt
    :type json_object: str
    :return: encrypted data
    :rtype: str
    """
    with open(ACCOUNTS_PATH,"r", encoding="utf-8") as a:
        json_file = a.read()
    encrypt_json = FERNET.encrypt(json_file)
    return encrypt_json

def decrypt_file(json_file: str)-> str:
    """Decrypt JSON file

    :param accounts: data to decrypt
    :type accounts: str
    :return: decrypted data
    :rtype: str
    """
    key = askstring('Password', 'What is your password?')
    decrypt_json = FERNET.decrypt(json_file)
    return decrypt_json

def file_path()-> None:
    """Allow the user to choose accounts.json folder"""
    folder_selected = filedialog.askdirectory()
    if folder_selected is None:
        ACCOUNTS_PATH = os.path.expanduser(r"~\Documents\accounts.json")
    else:
        ACCOUNTS_PATH = folder_selected
    ACCOUNTS_PATH += r"\accounts.json"

def read_json_data()-> list[dict] or None:
    """Read JSON data and upload data on temp_account"""
    #file_path()
    local_accounts=[]
    try:
        with open(ACCOUNTS_PATH,"r", encoding="utf-8") as a:
            local_accounts = decrypt_file(a)
            local_accounts = json.load(local_accounts)
    except FileNotFoundError:
        #file_path()
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

def check_data(site: str, username: str, email: str, password: str):
    """Check account infos

    :param site: Account site
    :type site: str
    :param username: Account username
    :type username: str
    :param email: Account email
    :type email: str
    :param password: Account password
    :type password: str
    """
    #Strip all infos
    site = site.strip()
    username = username.strip()
    email = email.strip()
    password = password.strip()

    #Regex
    # site_regex = re.compile(r"[A-Za-z]+\.[A-Za-z]+", re.IGNORECASE)
    # email_regex= re.compile(r"[-A-Za-z0-9!#$%&'*+/=?^_`{|}~]+(?:\.[-A-Za-z0-9!#$%&'*+/=?^_`{|}~]+)*@(?:[A-Za-z0-9](?:[-A-Za-z0-9]*[A-Za-z0-9])?\.)+[A-Za-z0-9](?:[-A-Za-z0-9]*[A-Za-z0-9])?", re.IGNORECASE) #TODO: FIX

    #Check that all data is correct
    if len(site) > 0 and len(username) > 0 and len(email) > 0 and len(password) > 0:
        #if site_regex.match(site) and email_regex.match(email):
            save_data(site, username, email, password)
        # else:
        #     tk.messagebox.showinfo(title="Information error", message="Your site or email doesn't conform to a normal one", icon="error")
        #     return
    else:
        tk.messagebox.showinfo(title="Information error", message="Your information aren't correct, check if you insert all the info", icon="error")
        return

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
    enc_json = encrypt_file(json_object)
    with open(ACCOUNTS_PATH, "w", encoding='utf-8') as outfile:
        outfile.write(enc_json)
