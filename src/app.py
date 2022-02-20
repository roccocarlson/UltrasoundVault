# Winter Wonderhack 2022
# Feb 18-20
# Rocco Carlson

from vault import vault
import tkinter as tk

# Create mainWindow
mainWindow = tk.Tk()
mainWindow.title("Vault")
mainWindow.geometry("575x500")

# Create heading
heading = tk.Label(mainWindow, text="Welcome to Vault",font="none 24 bold").grid(row=0, column=0, columnspan=3)


# Create text entry and button for creating or unlocking vault
label_vault = tk.Label(mainWindow, text="Enter name of vault below and click button to open/create vault")
label_vault.grid(row=1, column=0, columnspan=3)
entry_vault = tk.Entry(mainWindow, width=20)
entry_vault.grid(row=2, column=0, columnspan=3)

# function to execute when button is clicked
def button_vault_clicked():
    label_vault_debug.config(text="Listening for passkey...")
    mainWindow.update()
    global myVault
    myVault = vault(entry_vault.get())
    label_vault_debug.config(text="Passkey received, vault opened")

# button assignment and debug label
button_vault = tk.Button(mainWindow, text="Create or Unlock Vault", fg="blue", command=button_vault_clicked)
button_vault.grid(row=3, column=0, columnspan=3)
label_vault_debug = tk.Label(mainWindow)
label_vault_debug.grid(row=4,column=0, columnspan=3)

# widgets for new entry
label_newEntry = tk.Label(mainWindow, text="Enter website, username, and password and click button to add entry")
label_newEntry.grid(row=6, column=0, columnspan=3)
entry_website = tk.Entry(mainWindow, width=20)
entry_website.grid(row=8, column=0)
entry_username = tk.Entry(mainWindow, width=20)
entry_username.grid(row=8, column=1)
entry_password = tk.Entry(mainWindow, width=20, show="*")
entry_password.grid(row=8, column=2)
label_website = tk.Label(mainWindow, text="Website", font="none 12 bold").grid(row=7, column=0)
label_username = tk.Label(mainWindow, text="Username", font="none 12 bold").grid(row=7, column=1)
label_password = tk.Label(mainWindow, text="Password", font="none 12 bold").grid(row=7, column=2)

def button_newEntry_clicked():
    myVault.newEntry(entry_website.get(),entry_username.get(),entry_password.get())
    entry_website.delete(0,tk.END)
    entry_username.delete(0,tk.END)
    entry_password.delete(0,tk.END)
    label_newEntry_debug.config(text="New data entered")
    
button_newEntry = tk.Button(mainWindow, fg="blue", text="Add entry", command=button_newEntry_clicked).grid(row=9, column=0, columnspan=3)
label_newEntry_debug = tk.Label(mainWindow)
label_newEntry_debug.grid(row=10, column=0, columnspan=3)

# widgets for displaying entries
label_display = tk.Label(mainWindow, text="Click button to display contents of vault")
label_display.grid(row=11, column=0, columnspan=3)
text_display = tk.Text(mainWindow, height=10, width=60, bg="#ffedbd")
text_display.grid(row=12, column=0, columnspan=3)

def button_display_clicked():
    text_display.delete("1.0", tk.END)
    contents = myVault.printEntries()
    text_display.insert(tk.END, contents)

button_display = tk.Button(text="Display Entries", fg="blue",command=button_display_clicked)
button_display.grid(row=13, column=0, columnspan=3)

# widgets for locking vault
mainWindow.rowconfigure(14, minsize=20)
label_lock = tk.Label(mainWindow)
label_lock.grid(row=16, column=0, columnspan=3)

def button_lock_clicked():
    text_display.delete("1.0", tk.END)
    myVault.lockVault()
    label_lock.config(text="Vault successfully locked")

button_lock = tk.Button(mainWindow, text="LOCK VAULT", fg="blue", command=button_lock_clicked)
button_lock.grid(row=15, column=0, columnspan=3)

mainWindow.mainloop()