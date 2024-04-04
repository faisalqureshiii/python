import tkinter as tk
from tkinter import messagebox

def show_custom_dialog():
    messagebox.showinfo("Custom Dialog", "This is a custom dialog box.")

def submit():
    name = name_entry.get()
    gender = gender_var.get()
    age = age_entry.get()
    selected_hobbies = [hobby for hobby, var in zip(hobbies, hobbies_vars) if var.get()]
    
    info = f"Name: {name}\nGender: {gender}\nAge: {age}\nHobbies: {', '.join(selected_hobbies)}"
    messagebox.showinfo("Submitted Information", info)

root = tk.Tk()
root.title("GUI Example")


tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w")
tk.Label(root, text="Gender:").grid(row=1, column=0, sticky="w")
tk.Label(root, text="Age:").grid(row=2, column=0, sticky="w")
tk.Label(root, text="Hobbies:").grid(row=3, column=0, sticky="w")


name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1)


gender_var = tk.StringVar()
gender_var.set("Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=1, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=1, column=1, sticky="e")

hobbies = ["Reading", "Writing", "Coding"]
hobbies_vars = [tk.BooleanVar() for _ in range(len(hobbies))]
for i, hobby in enumerate(hobbies):
    tk.Checkbutton(root, text=hobby, variable=hobbies_vars[i]).grid(row=3, column=i+1, sticky="w")


tk.Button(root, text="Submit", command=submit).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="Show Dialog", command=show_custom_dialog).grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
