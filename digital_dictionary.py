
class Dictionary:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function
    def hash_function(self, word):
        return sum(ord(char) for char in word.lower()) % self.size

    # Add a word and its meaning
    def add_word(self, word, meaning):
        index = self.hash_function(word)

        # Update meaning if word already exists
        for entry in self.table[index]:
            if entry[0] == word.lower():
                entry[1] = meaning
                print("Meaning updated successfully!")
                return

        self.table[index].append([word.lower(), meaning])
        print("Word added successfully!")

    # Search for a word
    def search_word(self, word):
        index = self.hash_function(word)

        for entry in self.table[index]:
            if entry[0] == word.lower():
                print(f"Meaning of {word}: {entry[1]}")
                return

        print("Word not found in dictionary.")

    # Delete a word
    def delete_word(self, word):
        index = self.hash_function(word)

        for entry in self.table[index]:
            if entry[0] == word.lower():
                self.table[index].remove(entry)
                print("Word deleted successfully!")
                return

        print("Word not found in dictionary.")

    # Display all words
    def display_dictionary(self):
        print("\n--- Dictionary Contents ---")
        found = False

        for index, bucket in enumerate(self.table):
            for word, meaning in bucket:
                print(f"{word}: {meaning}")
                found = True

        if not found:
            print("Dictionary is empty.")


# Main program
dictionary = Dictionary()

while True:
    print("\n===== Dictionary Application =====")
    print("1. Add Word")
    print("2. Search Word")
    print("3. Delete Word")
    print("4. Display Dictionary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        word = input("Enter word: ").strip()
        meaning = input("Enter meaning: ").strip()

        if word and meaning:
            dictionary.add_word(word, meaning)
        else:
            print("Word and meaning cannot be empty.")

    elif choice == "2":
        word = input("Enter word to search: ").strip()
        dictionary.search_word(word)

    elif choice == "3":
        word = input("Enter word to delete: ").strip()
        dictionary.delete_word(word)

    elif choice == "4":
        dictionary.display_dictionary()

    elif choice == "5":
        print("Thank you for using the Dictionary Application!")
        break

    else:
        print("Invalid choice. Please try again.")
