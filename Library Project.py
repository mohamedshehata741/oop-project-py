
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

  def add_book(self):
     title = input("Enter the book title: ")
     author = input("Enter the book author: ")
     genre = input("Enter the book genre: ")
     publication_year = int(input("Enter the book publication year: "))
     newbook=Book(title,author,genre,publication_year)
     if newbook not in self.Books:
      self.Books.append(newbook)
      self.save_file()
      print(f"book '{newbook.title}' added to the library.")
     else:
      print(f"book '{newbook.title}' already added to the library before.")



  def remove_book(self,title):

      found=False
      for i in self.Books:
        if title.lower()==i.title.lower():
          self.Books.remove(i)
          self.save_file()
          found =True
          print(f"book '{i.title}' removed from the library.")
          break
      if not found:
        print(f"Error Book '{title}' not found.")


  def is_found(self,title):
    found=False
    for i in self.Books:
        if title.lower()==i.title.lower():
            found =True
            print(f"book '{title}' is found.")
            break
    if not found:
      print(f"book'{title}'not found.")
  def display(self):
    if not self.Books:
        print("Library is empty.")
    else:
        j=1  #book counter
        for i in self.Books:
            print(f"Book'{j}'")
            j+=1
            print("Title: ",i.title)
            print("Author: ",i.author)
            print("Genre: ",i.genre)
            print("Publication year: ",i.publication_year)
            print("==============")
  def save_file(self):
    with open("Library.txt", "w", encoding="utf-8") as file:
      for book in self.Books:
        l=f"{book.title},{book.author},{book.genre},{book.publication_year}\n"
        file.write(l)

  def load_file(self):
      try:
        with open("Library.txt", "r", encoding="utf-8") as file:
          for l in file:  #file : introduction to java,Y.daniel,Programming,2013
             title, author, genre, publication_year=l.strip().split(",")  #[introduction to java,Y.daniel,Programming,2013]
             book=Book(title,author,genre,publication_year)
             self.Books.append(book)

      except FileNotFoundError:
        print("\n=========================================")
        print("No previous library data found,Starting.")
        print("=========================================")


def menu():
  library=Library()

  while True:
      print("\n========== Personal Library Menu ==========\n")
      print("1. Add Book")
      print("2. Remove Book")
      print("3. Search for a Book")
      print("4. Display Library")
      print("5. Exit")
      print("\n===========================================")
      choice = input("Enter your choice (1-5): ")

      if choice == "1":
            library.add_book()

      elif choice == "2":
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)

      elif choice == "3":
            title = input("Enter the title of the book to search for: ")
            library.is_found(title)

      elif choice == "4":
            library.display()

      elif choice == "5":
            print("Goodbye!")
            break

      else:
         print("Invalid choice. Please enter a number between 1 and 5.")


menu()
