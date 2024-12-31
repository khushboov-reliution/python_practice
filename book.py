class Book:
    def __init__(self, title, author, isbn, price, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Price: ${self.price:.2f}, Quantity: {self.quantity}"

# # obj1.category1()
# print("Categories:")
# for category in [obj1, obj2, obj3]:
#     print(category)
#
# cat_list = [(obj1.code, obj1.name, obj1.no_of_product), (obj2.code, obj2.name, obj2.no_of_product),
#             (obj3.code, obj3.name, obj3.no_of_product)]
# cat1_list = [obj1.code, obj2.code, obj3.code]
#
#
# def sorting(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 # # temp = arr[j]             other methood
#                 # arr[j] =arr[j+1]
#                 # arr[j+1]=temp
#
#
# sorting(cat_list)
# print('Ascending order:', cat_list)
#
#
# def dsorting(array):
#     for i in range(len(array)):
#         for j in range(len(array) - 1):
#             if array[j] < array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# dsorting(cat_list)
# print('Descending order :', cat_list)
#
# search_code = int(input('enter code:'))
# for i in cat1_list:
#     if i == search_code:
#         print('code is exist')
#         break
# else:
#     print('code is not exist')
#
# product_list = [(product_obj1.price, product_obj1.name), (product_obj2.price, product_obj2.name),
#                 (product_obj3.price, product_obj3.name), (product_obj4.price, product_obj4.name),
#                 (product_obj5.price, product_obj5.name),
#                 (product_obj6.price, product_obj6.name), (product_obj7.price, product_obj7.name),
#                 (product_obj8.price, product_obj8.name), (product_obj9.price, product_obj9.name),
#                 (product_obj10.price, product_obj10.name)]
#
#
# def asendinglist(array):
#     for i in range(len(array)):
#         for j in range(len(array) - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# asendinglist(product_list)
# print('Ascending order:', product_list)
#
# # mylist=[20,11,13,13,19,18,13]
# # value = int(input('enter num'))
# # count=0
# # for i in mylist:
# #     if i == value:
# #         count=count+1
# # print(count)
#
# # class Teacher(object):
# #     def __str__(self):
# #         return 'hello'
# # class Student(Teacher):
# #     def __new__(cls):
# #         return Teacher()
# #
# #     def __init__(self):
# #         print('good evening')
# #
# # obj1 =Teacher
#

class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the bookstore.")
            return

        print("\n--- Available Books ---")
        for i, book in enumerate(self.books):
            print(f"{i + 1}. {book}")
        print("-----------------------\n")

    def search_book(self, search_term):
        results = []
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower() or search_term in book.isbn:
                results.append(book)
        return results

    def sell_book(self, book_index, quantity):
        if 0 <= book_index < len(self.books):
            selected_book = self.books[book_index]
            if selected_book.quantity >= quantity:
                selected_book.quantity -= quantity
                print(f"Sold {quantity} copies of '{selected_book.title}'.")
                if selected_book.quantity == 0:
                    self.books.pop(book_index)  # Remove if quantity is zero
                return True
            else:
                print(f"Not enough copies of '{selected_book.title}' in stock.")
                return False
        else:
            print("Invalid book index.")
            return False


def main():
    bookstore = Bookstore()

    # Sample books (you can expand this)
    bookstore.add_book(Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "978-0345391803", 7.99, 5))
    bookstore.add_book(Book("Pride and Prejudice", "Jane Austen", "978-0141439518", 6.50, 3))
    bookstore.add_book(Book("To Kill a Mockingbird", "Harper Lee", "978-0060935467", 9.99, 2))

    while True:
        print("\n--- Bookstore Menu ---")
        print("1. Display Books")
        print("2. Search Book")
        print("3. Sell Book")
        print("4. Add Book")  # Added Feature
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            bookstore.display_books()
        elif choice == '2':
            search_term = input("Enter search term (title, author, or ISBN): ")
            search_results = bookstore.search_book(search_term)
            if search_results:
                print("\n--- Search Results ---")
                for i, book in enumerate(search_results):
                    print(f"{i + 1}. {book}")
                print("----------------------\n")
            else:
                print("No books found matching your search.")
        elif choice == '3':
            bookstore.display_books()
            if bookstore.books:  # Check if books exists before asking for index
                try:
                    book_index = int(input("Enter the number of the book to sell: ")) - 1
                    quantity = int(input("Enter the quantity to sell: "))
                    bookstore.sell_book(book_index, quantity)
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == '4':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            try:
                price = float(input("Enter the price of the book: "))
                quantity = int(input("Enter the quantity of the book: "))
                new_book = Book(title, author, isbn, price, quantity)
                bookstore.add_book(new_book)
                print(f"Book '{title}' added successfully.")
            except ValueError:
                print("Invalid input for price or quantity. Please enter numbers.")
        elif choice == '5':
            print("Exiting the bookstore application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()