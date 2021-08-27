
def submit():
    food = []
    for index in lBox.curselection():
        food.insert(index,lBox.get(index))
    print("You have ordered: ")
    for index in food:
        print(index)
    #print(lBox.get(lBox.curselection()))

def add():
    lBox.insert(lBox.size(), entry.get())
    lBox.config(height=lBox.size())

def delete():
    for index in reversed(lBox.curselection()):
        lBox.delete(index)
    #lBox.delete(lBox.curselection())
    lBox.config(height=lBox.size())

window = Tk()

lBox = Listbox(window,
                bg="#f7ffde",
                font=("Constantia",35),
                width=12,
                selectmode=MULTIPLE,
                )
lBox.pack()

lBox.insert(1,"Pizza")
lBox.insert(2,"Garlic Bread")
lBox.insert(3,"Spaghetti")
lBox.insert(4,"Chocolate Mousse")
lBox.insert(5,"Calzone")
lBox.insert(6,"Panini")
lBox.insert(7,"Ravioli")
lBox.config(height=lBox.size())


entry = Entry(window)
entry.pack()


submit = Button(window,
                text="Submit",
                command=submit)
submit.pack()

addB = Button(window,
                text="add",
                command=add)
addB.pack()

delete = Button(window,
                text="delete",
                command=delete)
delete.pack()

window.mainloop() 
