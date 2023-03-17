import tkinter as tk

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    #setters
    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    #getters
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

class BookShelf:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books

class BookShelfGUI: #input number of books in the main window, pop up window for each book input
    def __init__(self, master):
        self.master = master
        master.title("Bookshelf")

        self.label = tk.Label(master, text="Enter number of books")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Submit", command=self.submit)
        self.button.pack()

    def submit(self):
        self.num_books = int(self.entry.get())
        self.master.destroy()

        self.master = tk.Tk()
        self.master.title("Bookshelf")

        self.label = tk.Label(self.master, text="Enter book title")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.label2 = tk.Label(self.master, text="Enter author")
        self.label2.pack()

        self.entry2 = tk.Entry(self.master)
        self.entry2.pack()

        self.button = tk.Button(self.master, text="Submit", command=self.submit2)
        self.button.pack()

    def submit2(self):
        self.title = self.entry.get()
        self.author = self.entry2.get()
        self.master.destroy()

        self.master = tk.Tk()
        self.master.title("Bookshelf")

        self.label = tk.Label(self.master, text="Enter book title")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.label2 = tk.Label(self.master, text="Enter author")
        self.label2.pack()

        self.entry2 = tk.Entry(self.master)
        self.entry2.pack()

        self.button = tk.Button(self.master, text="Submit", command=self.submit2)
        self.button.pack()

        self.bookshelf = BookShelf()
        self.bookshelf.add_book(Book(self.title, self.author))

        print(self.bookshelf.get_books())

        self.master.mainloop()



if __name__ == "__main__":
    root = tk.Tk()
    my_gui = BookShelfGUI(root)
    root.mainloop()