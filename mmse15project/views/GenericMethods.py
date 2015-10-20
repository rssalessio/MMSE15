import tkinter.ttk as ttk


def get_header(master, b_text, cmd):
    user_info = "%s, %s — %s" % (master.acc_team, master.acc_type, master.user)
    ttk.Label(master, text=user_info).grid(row=0, column=0)
    b1 = ttk.Button(master, text=b_text,
                       command=cmd)
    b1.grid(row=0, column=1, sticky="E")