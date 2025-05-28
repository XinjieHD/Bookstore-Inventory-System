from pymongo import MongoClient

# Connect to MongoDB (local or MongoDB Atlas)
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI if using Atlas
db = client["bookstore"]
collection = db["books"]

# Create
def add_book(title, author, year):
    book = {"title": title, "author": author, "year": year}
    result = collection.insert_one(book)
    print(f"Book added with _id: {result.inserted_id}")

# Read
def list_books():
    for book in collection.find():
        print(book)

# Update
def update_book(title, new_author):
    result = collection.update_one({"title": title}, {"$set": {"author": new_author}})
    if result.modified_count:
        print(f"Book '{title}' updated.")
    else:
        print("No matching book found.")

# Delete
def delete_book(title):
    result = collection.delete_one({"title": title})
    if result.deleted_count:
        print(f"Book '{title}' deleted.")
    else:
        print("No matching book found.")

# Demo
if __name__ == "__main__":
    add_book("1984", "George Orwell", 1949)
    add_book("To Kill a Mockingbird", "Harper Lee", 1960)

    print("\nAll Books:")
    list_books()

    print("\nUpdating author of '1984'...")
    update_book("1984", "Eric Arthur Blair")

    print("\nBooks after update:")
    list_books()

    print("\nDeleting 'To Kill a Mockingbird'...")
    delete_book("To Kill a Mockingbird")

    print("\nBooks after deletion:")
    list_books()
