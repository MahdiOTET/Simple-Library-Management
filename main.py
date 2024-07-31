from tkinter import *
import backend
rootWindow = Tk()

rootWindow.title("Library management")
rootWindow.resizable(width=False, height=False)
# rootWindow.geometry("500x300")
# =================== entries and labels ===================
title_label = Label(rootWindow, text="Title")
title_label.grid(row=0, column=0, padx=5, pady=2)

title_entry = Entry(rootWindow)
title_entry.grid(row=0, column=1, padx=5, pady=2)

year_label = Label(rootWindow, text="Year")
year_label.grid(row=1, column=0, padx=5, pady=2)

year_entry = Entry(rootWindow)
year_entry.grid(row=1, column=1, padx=5, pady=2)

author_label = Label(rootWindow, text="Author")
author_label.grid(row=0, column=2, padx=5, pady=2)

author_entry = Entry(rootWindow)
author_entry.grid(row=0, column=3, padx=5, pady=2)

isbn_label = Label(rootWindow, text="ISBN")
isbn_label.grid(row=1, column=2, padx=5, pady=2)

isbn_entry = Entry(rootWindow)
isbn_entry.grid(row=1, column=3, padx=5, pady=2)
# =================== list boxes and scroll bars ===================
list_box = Listbox(rootWindow, width=40, height=10)
list_box.grid(row=2, column=1, rowspan=6, columnspan=2, padx=10, pady=10)

# scroll = Scrollbar(rootWindow)
# scroll.grid(row=2, column=3, rowspan=6)

# list_box.configure(yscrollcommand=scroll.set)
# scroll.configure(command=list_box.yview)
# =================== functions ===================
def clear_list():
    list_box.delete(first=0, last=END)

def fill_list(books):
    for book in books:
        list_box.insert(END, book)

def view_all():
    clear_list()
    books = backend.view()
    fill_list(books)

def search():
    clear_list()
    books = backend.search(title=title_entry.get(), author=author_entry.get(), year=year_entry.get(), isbn=isbn_entry.get())
    fill_list(books)

def add():
    backend.insert(title=title_entry.get(), author=author_entry.get(), year=year_entry.get(), isbn=isbn_entry.get())
    view_all()

def get_book(event):
    global selected_book
    if len(list_box.curselection()) > 0:
        index = list_box.curselection()[0]
        selected_book = list_box.get(index)
   
        title_entry.delete(0, END)
        title_entry.insert(END, selected_book[1])
        
        author_entry.delete(0, END)
        author_entry.insert(END, selected_book[2])

        year_entry.delete(0, END)
        year_entry.insert(END, selected_book[3])
        
        isbn_entry.delete(0, END)
        isbn_entry.insert(END, selected_book[4])
    
    
list_box.bind("<<ListboxSelect>>", get_book)

def delete():
    backend.delete(selected_book[0])
    view_all()

def update():
    backend.update(id=selected_book[0], title=title_entry.get(), author=author_entry.get(), year=year_entry.get(), isbn=isbn_entry.get())
    view_all()

# =================== buttons ===================
view_all_button = Button(rootWindow, width=12, text="View All", command=view_all)
view_all_button.grid(row=2, column=3)

search_entry_button = Button(rootWindow, width=12, text="Search Entry",command=search)
search_entry_button.grid(row=3, column=3)

add_button = Button(rootWindow, width=12, text="Add Entry", command=add)
add_button.grid(row=4, column=3)

update_button = Button(rootWindow, width=12, text="Update Selected", command=update)
update_button.grid(row=5, column=3)

delete_button = Button(rootWindow, width=12, text="Delete Selected", command=delete)
delete_button.grid(row=6, column=3)

exit_button = Button(rootWindow, width=12, text="Exit", command=rootWindow.destroy)
exit_button.grid(row=7, column=3)

view_all()
rootWindow.mainloop()