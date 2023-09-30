import tkinter as tk

root = tk.Tk()
root.title("Welcome  To My To do list")
root.geometry('400x300')


frame = tk.Frame(root)

frame.pack(padx=15,pady=15)
for i in range(2):
    frame.columnconfigure(i,pad=10)

for i in range(4):
    frame.rowconfigure(i, pad=10)
def add():
    task = enter.get()
    if task:
        listbox.insert(tk.END,task)
        enter.delete(0,tk.END)
def remove():
    select = listbox.curselection()
    if select:
        listbox.delete(select)
enter = tk.Entry(frame,width=30)
enter.grid(row=0,column=0)

add_b = tk.Button(frame,text="Add Task",command=add)
add_b.grid(row=0,column=1)

remove_b = tk.Button(frame,text="Remove Task",command=remove)
remove_b.grid(row=0,column=2)

listbox = tk.Listbox(frame,selectmode=tk.SINGLE,width=30,height=8)
listbox.grid(row=2,column=0,columnspan=3)

label = tk.Label(frame, text="Select any task for remove")
label.grid(row=1,column=0,columnspan=3)

root.mainloop()