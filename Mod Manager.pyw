import shutil
from tkinter import *
import os
window = Tk()
window.title("Mod Manager")
window.geometry("300x300")
#change background color for all elements
window.configure(background="black")

#add text to the window
title = Label(window, text="Mod Organizer",background="black", foreground="white")
title.pack(pady=10)

description = Label(window, text="select wich modpack you want",background="black", foreground="white")
description.pack(pady=10)

#create the mods and modpack folders if not present
if not os.path.exists("mods"):
    os.mkdir("mods")
if not os.path.exists("modpacks"):
    os.mkdir("modpacks")

options = ["Option 1", "Option 2", "Option 3"]
# Specify the directory path
directory = "modpacks"
# Get the list of folders in the directory
folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]
# Create a StringVar to store the selected option
selected_option = StringVar()
# Set the initial value of the dropdown menu
selected_option.set(folders[0] if folders else "")
# Create the dropdown menu
dropdown = OptionMenu(window, selected_option, *folders)
#scale the dropdown
dropdown.config(width=30,background="black",foreground="white")
#change dropdown color
dropdown.pack(pady=10)


#add a button
mods_folder = "mods"
def change_modpack():
    modpack_folder = selected_option.get()
    #asign mods from the modpack folder to the mods list
    modpack = os.listdir(os.path.join(directory, modpack_folder))
    print(modpack)
    #delete the content of the mods folder
    for file in os.listdir(mods_folder):
        os.remove(os.path.join(mods_folder, file))
    for mod in modpack:
        print(mod)
        shutil.copy2(os.path.join(directory, modpack_folder, mod), os.path.join(mods_folder, mod))
button = Button(window, text="Change Modpack", background="black", foreground="white", command=change_modpack)
#make the button lighten on hover
button.bind("<Enter>", lambda event: button.config(background="white",foreground="black"))
button.bind("<Leave>", lambda event: button.config(background="black",foreground="white"))

button.pack(pady=30)

new_modpack_text = Label(window, text="to create a new modpack,\ncreate a new folder in the /modpacks directory",background="black", foreground="white")
new_modpack_text.pack()

window.mainloop()
