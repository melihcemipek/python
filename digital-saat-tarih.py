from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title("Saat & Tarih")
window.geometry("400x160")
window.configure(bg="green")
window.resizable(False, False)

clock_label = Label(window, bg="black", fg="cyan", font=("Arial", 60, "bold"), relief="flat")
clock_label.place(x=20, y=20)

def update_label():
    current_time = strftime("%H: %M: %S\n %d-%m-%Y ")
    clock_label.configure(text=current_time)
    clock_label.after(160, update_label)
    clock_label.pack(anchor="center")

update_label()
window.mainloop()