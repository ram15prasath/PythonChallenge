class Book:
    """
    A class to represent a book with a title, author, and availability status.
    """
    def __init__(self, title, author, isbn):
        # The constructor to initialize a new Book object
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False  # Default status is available

    def checkout(self):
        """Marks the book as checked out."""
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"'{self.title}' has been checked out."
        else:
            return f"'{self.title}' is already checked out."

    def return_book(self):
        """Marks the book as available."""
        if self.is_checked_out:
            self.is_checked_out = False
            return f"'{self.title}' has been returned."
        else:
            return f"'{self.title}' was never checked out."

    def get_status(self):
        """Returns the current availability status."""
        status = "Checked Out 🔒" if self.is_checked_out else "Available ✅"
        return f"**{self.title}** by {self.author} (ISBN: {self.isbn}) - **Status**: {status}"

# --- Main Program Execution ---

print("--- Simple Library Manager (OOP Demo) ---")

# 1. Create instances (objects) of the Book class
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "978-0345391803")
book2 = Book("Clean Code", "Robert C. Martin", "978-0132350884")
book3 = Book("Pride and Prejudice", "Jane Austen", "978-0141439518")

# 2. Store the books in a list (our "library")
library = [book1, book2, book3]

print("\n--- Initial Library Status ---")
for book in library:
    print(f"* {book.get_status()}")

# 3. Perform actions on the objects
print("\n--- Library Operations ---")
# Checkout book1 and book2
print(f"> Operation 1: {book1.checkout()}")
print(f"> Operation 2: {book2.checkout()}")
# Try to checkout book1 again
print(f"> Operation 3: {book1.checkout()}") 
# Return book2
print(f"> Operation 4: {book2.return_book()}")

# 4. Display the final status
print("\n--- Final Library Status ---")
for book in library:
    print(f"* {book.get_status()}")