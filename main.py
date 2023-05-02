import tkinter as tk
import json
__version__ = "0.1.0"

def saveData():
    site = tb_site.get()
    username = tb_username.get()
    email = tb_email.get()
    password = tb_password.get()

    account_dict ={
        "site":site,
        "username":username,
        "email":email,
        "password":password
    }
    json_object = json.dumps(account_dict, indent=4)
    with open("accounts.json", "w", encoding='utf-8') as outfile:
        outfile.write(json_object)

if __name__=="__main__":
    win = tk.Tk()
    win.title(f"Account Manager {__version__}")

    lb_site = tk.Label(win, text="Site:")
    lb_site.pack()

    tb_site = tk.Entry(win)
    tb_site.pack()

    lb_username = tk.Label(win, text="Username:")
    lb_username.pack()

    tb_username = tk.Entry(win)
    tb_username.pack()

    lb_email = tk.Label(win, text="Email:")
    lb_email.pack()

    tb_email = tk.Entry(win)
    tb_email.pack()

    lb_password = tk.Label(win, text="Password:")
    lb_password.pack()

    tb_password = tk.Entry(win)
    tb_password.pack()

    button = tk.Button(win, text="Save data", command=saveData)
    button.pack()

    win.mainloop()
