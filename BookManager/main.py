# წიგნების მართვის კონსოლ აპლიკაცია

# შექმენით კონსოლ აპლიკაცია C# / Python-ში, რომელიც მომხმარებლებს საშუალებას აძლევს მართონ წიგნების სია. 
# თითოეულ წიგნს აქვს სათაური, ავტორი და გამოცემის წელი. მომხმარებელს უნდა შეეძლოს წიგნის დამატება, 
# წიგნების სიის ნახვა და წიგნის სათაურის მოძიება. 

import os
 
# BOOK კლასი – წიგნის ატრიბუტები და მეთოდები
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
 
    def __str__(self):
        return f"სათაური: {self.title}, ავტორი: {self.author}, წელი: {self.year}"
   
# BOOKMANAGER კლასი – წიგნების მართვა (დამატება, ჩვენება, ძიება, შენახვა)
class BookManager:
    def __init__(self, filename: str="library.txt"):
        self.books = []
        self.filename = filename
        if os.path.exists(self.filename):
            self.load_from_file()  
 
 
    # წიგნის დამატების მეთოდი
    def add_book(self, book):
        for b in self.books:
           if b.title.lower() == book.title.lower() and b.author.lower() == book.author.lower() and b.year == book.year:
               print(f"წიგნი: {book}, უკვე არსებობს ბიბლიოთეკაში")
               return
        self.books.append(book)
        print(f"წიგნი: {book}, წარმატებით დაემატა ბიბლიოთეკაში")
        self.save_file(self.filename) 
 
    # ყველა წიგნის ჩვენების მეთოდი
    def all_book(self):
        if not self.books:
            print("\nბიბლიოთეკაში წიგნები ჯერ არ არის.\n")
            return
 
        print("\n წიგნების სია ")
        for book in self.books:  
            print(book)
        print()
 
 
    # წიგნის ძიება სათაურით
    def search_title(self, title):
        results = []
        for book in self.books:
            if book.title.lower() == title.lower():  
                results.append(book)
        return results
 
 
    # ფაილში შენახვა
    def save_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for book in self.books:
                line = f"{book.title}|{book.author}|{book.year}\n"
                file.write(line)
 
    # ფაილიდან ჩატვირთვა
    def load_from_file(self):
        if not os.path.exists(self.filename):
            return
 
        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                title, author, year = line.strip().split("|")
                book = Book(title, author, year)
                self.books.append(book)

# გამოცემის წელის შემომოწმების ფუნქცია

def valid_year():
    while True:
        year = input("შეიყვანეთ გამოცემის წელი: ")
        if year.isdigit() and 2025 >= int(year):
            return int(year)
        print(" არასწორი წელი! შეიყვანეთ რიცხვი, არამომავლის.")


# მთავარი ფუნქცია
def main():
    manager = BookManager()
 
    while True:
        print("\nმენიუ:")
        print("1. წიგნის დამატება")
        print("2. ყველა წიგნის ჩვენება")
        print("3. წიგნის ძიება სათაურით")
        print("4. გამოსვლა")
 
        choice = input("აირჩიეთ (1-4): ")
 
        if choice == "1":
            title = input("შეიყვანეთ წიგნის სათაური: ")
            author = input("შეიყვანეთ ავტორი: ")
            year = valid_year()
            newbook = Book(title, author, year)
            manager.add_book(newbook)
 
        elif choice == "2":
            # manager.all_book()
            print("\nწიგნების სია:\n")
            print("="*70)
            print(f"{'სათაური':<25} {'ავტორი':<30} {'წელი':<5}")
            print("="*70)  
            for book in manager.books:
                print(f"{book.title:<25} {book.author:<30} {book.year:<5}")
                print("-"*70)  
 
        elif choice == "3":
            if not manager.books:
                print("ბიბლიოთეკაში ჯერ არ არის წიგნები. გთხოვთ, დაამატეთ წიგნები ძიებამდე.\n")
                continue
            title = input("შეიყვანეთ წიგნის სათაური ძიებისთვის: ")
            results = manager.search_title(title)
            if results:
                print("\nმოძებნილი წიგნი:\n")
                print("="*70)
                print(f"{'სათაური':<25} {'ავტორი':<30} {'წელი':<5}")
                print("="*70)  
                for book in results:
                    print(f"{book.title:<25} {book.author:<30} {book.year:<5}")
                    print("-"*70) 
            else:
                print("წიგნი ვერ მოიძებნა.")
 
        elif choice == "4":
            print("გამოსვლა პროგრამიდან.")
            break
 
        else:
            print("მენიუ შედგება მხოლოდ ოთხი მოქმედებისგან. სცადეთ თავიდან. \n")
 
if __name__ == "__main__":  
    main()