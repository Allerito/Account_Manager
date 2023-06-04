import json
import re

from .build import gui


__version__ = "0.1.0"

def read_data()-> None:
    """Read JSON data and upload data on temp_account"""
    temp_accounts=[]
    filename = "accounts.json"
    try:
        with open("accounts.json","r", encoding="utf-8") as a:
            temp_accounts = json.load(a)
    except FileNotFoundError:
        with open(filename, "w", encoding="utf-8") as a:
            a.write("[]")
    except json.JSONDecodeError:
        with open(filename, "r", encoding="utf-8") as a:
            if a.read() == "":
                answer = tk.messagebox.askokcancel(title="Empty file", message="Your file is empty. Are you sure to overwrite the file?", icon="warning")

                if not answer:
                    tk.messagebox.showinfo(title="Empty file", message="Your file wasn't modified", icon="info")
                    return
    return temp_accounts

def check_data()-> None:
    """Check data that the user insert"""
    temp_accounts = read_data()
    site, username, email, password = form_generator()
    site_regex = re.compile(r"[A-Za-z]+\.[A-Za-z]+", re.IGNORECASE)
    email_regex= re.compile(r"([A-Za-z0-9]+(\.[A-Za-z0-9]+)+)@[A-Za-z]+\.[A-Za-z]+", re.IGNORECASE) #fix

    if len(site) > 0 and len(username) > 0 and len(email) > 0 and len(password) > 0:
        if site_regex.match(site) and email_regex.match(email):
            site = site.strip()
            username = username.strip()
            email = email.strip()
            password = password.strip()
            save_data(site, username, email, password, temp_accounts)
        else:
            tk.messagebox.showinfo(title="Information error", message="Your site or email doesn't conform to a normal one", icon="error")
            return
    else:
        tk.messagebox.showinfo(title="Information error", message="Your information aren't correct, check if you insert all the info", icon="error")
        return

def save_data(site: str, username: str, email: str, password: str, temp_accounts: list)-> None:
    """Save data inside JSON file

    :param site: Account site
    :type site: string
    :param username: Account username
    :type username: string
    :param email: Account email
    :type email: string
    :param password: Account password
    :type password: string
    :param temp_accounts: Temporal account manager
    :type temp_accounts: list
    """
    account_dict = {
        "site":site,
        "username":username,
        "email":email,
        "password":password
    }
    for account in temp_accounts:
        if account_dict == account:
            answer = tk.messagebox.askokcancel(title="Another account exist", message="There is another account associated to this site, do you want to create another account?", icon="warning")
            if not answer:
                tk.messagebox.showinfo(title="Another account exist", message="The account wasn't create", icon="info")
                return

    temp_accounts.append(account_dict)
    json_object = json.dumps(temp_accounts, indent=4)
    with open("accounts.json", "w", encoding='utf-8') as outfile:
        outfile.write(json_object)

def dialog_manager():
    back_button = tk.Button(win, text="back", command=step_calculator)
    back_button.pack()

    next_button = tk.Button(win, text="next", command=step_calculator)
    next_button.pack()

def step_calculator():
    step_functions=[read_data, choose_filepath, form_generator, save_data]
    if next_button == True


if __name__=="__main__":

