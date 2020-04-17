from tkinter import *
import bookstoreBKD

def get_selected_row(event):
    global selected_tuple
    index=l.curselection()[0]
    selected_tuple=l.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])


def view_b():
    l.delete(0,END)
    for row in bookstoreBKD.view():
        l.insert(END,row)

def search_b():
    l.delete(0,END)
    for row in bookstoreBKD.search(title_val.get(),author_val.get(),year_val.get(),isbn_val.get()):
            l.insert(END,row)

def add_b():
    bookstoreBKD.insert(title_val.get(),author_val.get(),year_val.get(),isbn_val.get())    
    l.delete(0,END)  
    l.insert(END,(title_val.get(),author_val.get(),year_val.get(),isbn_val.get()))

def del_b():
    bookstoreBKD.delete(selected_tuple[0])
    
def update_b():
        bookstoreBKD.update(selected_tuple[0],title_val.get(),author_val.get(),year_val.get(),isbn_val.get())
        print(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4])

app=Tk()

app.title('BookStore')

l1=Label(app, text='Title')
l1.grid(row=0,column=0)
l2=Label(app, text='Author')
l2.grid(row=0,column=2)
l3=Label(app, text="Year")
l3.grid(row=1,column=0)
l4=Label(app, text='ISBN')
l4.grid(row=1,column=2)

title_val=StringVar()
e1=Entry(app,textvariable=title_val)
e1.grid(row=0,column=1)

author_val=StringVar()
e2=Entry(app,textvariable=author_val)
e2.grid(row=0,column=3)

year_val=StringVar()
e3=Entry(app,textvariable=year_val)
e3.grid(row=1,column=1)

isbn_val=StringVar()
e4=Entry(app,textvariable=isbn_val)
e4.grid(row=1,column=3)

l=Listbox(app,height=10, width=50)
l.grid(row=2, column=0, rowspan=6, columnspan=2)

sb=Scrollbar(app)
sb.grid(row=2,column=2,rowspan=6)

l.configure(yscrollcommand=sb.set)
sb.configure(command=l.yview)

l.bind('<<ListBoxSelect>>',get_selected_row)
b1=Button(app,text='View All', width=12,command=view_b)
b1.grid(row=2, column=3)

b2=Button(app,text='Search Entry',width=12,command=search_b)
b2.grid(row=3, column=3)

b3=Button(app,text='Add Entry' ,width=12,command=add_b)
b3.grid(row=4, column=3)

b4=Button(app,text='Update Selected',width=12, command=update_b)
b4.grid(row=5, column=3)

b5=Button(app,text='Delete Selected',width=12,command=del_b)
b5.grid(row=6, column=3)

b6=Button(app,text='Close',width=12,command=app.destroy)
b6.grid(row=7, column=3)


app.mainloop()

