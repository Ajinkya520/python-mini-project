"""Menu-driven program that demonstrates basic file handling operations."""

from pathlib import Path

STUDENTS_FILE = Path("students.txt")
DATA_FILE = Path("data.txt")
NOTES_FILE = Path("notes.txt")
SOURCE_FILE = Path("source.txt")
DEST_FILE = Path("destination.txt")


def write_student() -> None:
    """Prompt for student info and append it to students.txt."""
    name = input("Enter student name: ").strip()
    roll = input("Enter roll number: ").strip()
    if not name or not roll:
        print("Both name and roll number are required.")
        return
    try:
        with STUDENTS_FILE.open("a", encoding="utf-8") as file:
            file.write(f"{name},{roll}\n")
        print("Student saved successfully.")
    except OSError as exc:
        print(f"Error writing student data: {exc}")


def read_students() -> None:
    """Display all students stored in students.txt."""
    if not STUDENTS_FILE.exists():
        print("No student records found.")
        return
    try:
        with STUDENTS_FILE.open("r", encoding="utf-8") as file:
            lines = [line.strip() for line in file if line.strip()]
    except OSError as exc:
        print(f"Error reading student data: {exc}")
        return

    if not lines:
        print("No student records found.")
        return

    print("\nSaved Students:")
    for idx, line in enumerate(lines, start=1):
        name, roll = line.split(",", maxsplit=1)
        print(f"{idx}. {name} - Roll No: {roll}")
    print()


def count_words_in_data() -> None:
    """Count words in data.txt and display the result."""
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            contents = file.read()
    except FileNotFoundError:
        print("data.txt not found.")
        return
    except OSError as exc:
        print(f"Error reading data.txt: {exc}")
        return

    total_words = len(contents.split())
    print(f"Total words in data.txt: {total_words}")


def copy_source_to_destination() -> None:
    """Copy the contents of source.txt into destination.txt."""
    try:
        contents = SOURCE_FILE.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("source.txt not found.")
        return
    except OSError as exc:
        print(f"Error reading source.txt: {exc}")
        return

    try:
        DEST_FILE.write_text(contents, encoding="utf-8")
    except OSError as exc:
        print(f"Error writing destination.txt: {exc}")
        return

    print("File copied successfully.")


def append_to_notes() -> None:
    """Append user-provided text to notes.txt."""
    text = input("Enter text to append: ").strip()
    if not text:
        print("No text entered.")
        return
    try:
        with NOTES_FILE.open("a", encoding="utf-8") as file:
            file.write(text + "\n")
        print("Text appended to notes.txt.")
    except OSError as exc:
        print(f"Error writing notes.txt: {exc}")


def search_word_in_data() -> None:
    """Search for a word inside data.txt."""
    word = input("Enter the word to search: ").strip()
    if not word:
        print("Please enter a valid word.")
        return

    try:
        contents = DATA_FILE.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("data.txt not found.")
        return
    except OSError as exc:
        print(f"Error reading data.txt: {exc}")
        return

    if word.lower() in contents.lower():
        print(f"'{word}' found in data.txt.")
    else:
        print(f"'{word}' not found in data.txt.")


def show_menu() -> None:
    print("\nFile Handling Menu")
    print("1. Write student data")
    print("2. Read student data")
    print("3. Count words in data.txt")
    print("4. Copy source.txt to destination.txt")
    print("5. Append text to notes.txt")
    print("6. Search word in data.txt")
    print("7. Exit")


def main() -> None:
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()
        if choice == "1":
            write_student()
        elif choice == "2":
            read_students()
        elif choice == "3":
            count_words_in_data()
        elif choice == "4":
            copy_source_to_destination()
        elif choice == "5":
            append_to_notes()
        elif choice == "6":
            search_word_in_data()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 7.")


if __name__ == "__main__":
    main()

