import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="BORDEL DE MERDE !")
button = tk.Button(root, text="Quitter", command=root.quit)
button["fg"] = "red"
label.pack()
button.pack()
root.mainloop()
print("C'est fini !")
