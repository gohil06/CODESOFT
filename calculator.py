from tkinter import * 

# use event ..
# event.widget get button jena pr click thayu se
#.cget('text') return how to get digit to text

# eval means if our values is(2*5,2+4,2/2 then convert into 2*3=6)
def click(event):
    global my_value
    text = event.widget.cget('text')
    print(text)

    if text == 'C':
        my_value.set('')
        box.update()
        
    elif text == '=':
        if my_value.get().isdigit():
            dipesh = int(my_value.get)
        else:
            dipesh = eval(box.get())
        
        my_value.set(dipesh)
        my_value.update()
    else:
        my_value.set(my_value.get() + text)
        box.update()



root = Tk()
root.geometry('600x500')

# make a title
root.title('Calculator by Dipesh')

# icon


my_label = Label(text='Welcome to Use My Caclulator',bg='red')
my_label.pack()


# make  a box..
my_value = StringVar()
my_value.set('')
box = Entry(root, textvar=my_value,font='lucida 30 bold')
box.pack(padx=10,pady=10,fill=X)

# Make A Frmae in 3 columns
f=Frame(root,bg='gray')

b1 = Button(f,text='7',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='8',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)


b1 = Button(f,text='9',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='/',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

f.pack()


f=Frame(root,bg='gray')

b1 = Button(f,text='4',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='5',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='6',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='*',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

f.pack()

f=Frame(root,bg='gray')

b1 = Button(f,text='1',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='2',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='3',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='-',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

f.pack()

f=Frame(root,bg='gray')

b1 = Button(f,text='0',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=5,pady=10)

b1 = Button(f,text='C',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='=',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

b1 = Button(f,text='+',padx=10,pady=12,font='lucida 18 bold')
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=10,pady=10)

f.pack()
















root.mainloop()