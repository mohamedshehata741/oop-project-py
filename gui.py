from cProfile import label
from tkinter import *
from tkinter import messagebox

class Book :
  def __init__(self,title,author,genre,publication_year):
    self.title=title
    self.author=author
    self.genre=genre
    self.publication_year=publication_year
  def __eq__(self, other):
    return (
        self.title.lower() == other.title.lower()
        and self.author.lower() == other.author.lower()
        and self.publication_year == other.publication_year
    )

class Library:
  def __init__(self):
    self.Books=[]
    self.load_file()

  def save_file(self):
        with open("Library.txt", "w", encoding="utf-8") as file:
            for book in self.Books:
                l = f"{book.title},{book.author},{book.genre},{book.publication_year}\n"
                file.write(l)

  def load_file(self):
        try:
            with open("Library.txt", "r", encoding="utf-8") as file:
                for l in file:  # file : introduction to java,Y.daniel,Programming,2013
                    title, author, genre, publication_year = l.strip().split(
                        ",")  # [introduction to java,Y.daniel,Programming,2013]
                    book = Book(title, author, genre, publication_year)
                    self.Books.append(book)

        except FileNotFoundError:
            print("\n=========================================")
            print("No previous library data found,Starting.")
            print("=========================================")




library=Library()

def add_book_gui():
    new_book=Toplevel()
    new_book.title("Add Book")
    new_book.geometry("200x200")
    #title=.......
    Label(new_book, text="Title").pack()
    title_entry=Entry(new_book)
    title_entry.pack()
    # author=.......
    Label(new_book, text="Author").pack()
    author_entry = Entry(new_book)
    author_entry.pack()
    # genre=.......
    Label(new_book, text="Genre").pack()
    genre_entry = Entry(new_book)
    genre_entry.pack()
    # publication_year=.......
    Label(new_book, text="Publication Year").pack()
    publication_year_entry=Entry(new_book)
    publication_year_entry.pack()

    def save_book():
      title = title_entry.get().strip()
      author = author_entry.get().strip()
      genre = genre_entry.get().strip()
      publication_year = publication_year_entry.get().strip()

      if title and author and genre and publication_year:
        try:
            publication_year=int(publication_year)
            newbook=Book(title,author,genre,publication_year)
            if newbook not in library.Books:
                library.Books.append(newbook)
                library.save_file()
                messagebox.showinfo("Success",f"book '{newbook.title}' added to the library.")
                new_book.destroy()
            else:
                messagebox.showinfo("Duplicate",f"book '{newbook.title}' already added to the library before.")

        except ValueError:
            messagebox.showerror("Error", "Year must be a number.")


      else:
          messagebox.showerror("Error", "Please fill all fields.")

    Button(new_book, text="Add", command=save_book).pack(pady=10)


def remove_book_gui():
    remove_book=Toplevel()
    remove_book.title("Remove Book")
    remove_book.geometry("200x200")

    label=Label(remove_book, text="Title").pack()
    title_entry=Entry(remove_book)
    title_entry.pack()

    def remove_Book():
        title=title_entry.get().strip()

        found=False
        for i in library.Books:
          if title.lower()==i.title.lower():
            library.Books.remove(i)
            library.save_file()
            found =True
            messagebox.showinfo("Success",f"book '{i.title}' removed from the library.")
            remove_book.destroy()
            break
        if not found:
            messagebox.showerror("Error", "Book not found.")


    Button(remove_book, text="Remove", command=remove_Book).pack(pady=10)



def display_books_gui():
    display_win = Toplevel()
    display_win.title("Library Books")

    if not library.Books:
        Label(display_win, text="Library is empty.").pack()
    else:
        for i, book in enumerate(library.Books, start=1):
            Label(display_win, text=f"Book {i}:").pack()
            Label(display_win, text=f"Title: {book.title}").pack()
            Label(display_win, text=f"Author: {book.author}").pack()
            Label(display_win, text=f"Genre: {book.genre}").pack()
            Label(display_win, text=f"Year: {book.publication_year}").pack()
            Label(display_win, text="====================").pack()

def is_found_gui():
    found_book=Toplevel()
    found_book.title("Is Found")
    found_book.geometry("200x200")

    label=Label(found_book, text="Title").pack()
    title_entry=Entry(found_book)
    title_entry.pack()
    def is_found():
      title = title_entry.get().strip()
      found=False
      for i in library.Books:
        if title.lower()==i.title.lower():
            found =True
            messagebox.showinfo("YES",f"book '{title}' is found.")
            found_book.destroy()
            break
      if not found:
        messagebox.showinfo("NO",f"book'{title}'not found.")

    Button(found_book, text="Is Found", command=is_found).pack(pady=10)




def main_window():
  window = Tk()
  window.title("Library")
  window.geometry("400x400")
  lb=Label(window,text=" Welcome to the Library",font=("Arial", 14))
  lb.pack(pady=10)
  b1=Button(window,text="Add Book",width="20",command=add_book_gui)
  b1.pack(pady=5)
  b2 = Button(window, text="Remove Book", width="20", command=remove_book_gui)
  b2.pack(pady=5)
  b3=Button(window, text="Is Found", width="20", command=is_found_gui)
  b3.pack(pady=5)
  b4 = Button(window, text="Displays Book", width="20", command=display_books_gui)
  b4.pack(pady=5)
  b5 = Button(window, text="Exit", width="20", command=window.destroy)
  b5.pack(pady=5)

  window.mainloop()

main_window()
