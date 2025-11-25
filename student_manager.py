"""
Simple CLI utility to store and read student records from `students.txt`.

Features:
- Adds new student records collected from user input.
- Displays all stored student records.
- Handles common file I/O errors gracefully.
"""

from typing import List, Tuple

STORAGE_FILE = "students.txt"


def gather_student_data() -> List[Tuple[str, str]]:
    """Collect student details from the user until they choose to stop."""
    records: List[Tuple[str, str]] = []
    print("Enter student details. Leave the name blank to finish.\n")
    while True:
        name = input("Student name: ").strip()
        if not name:
            break
        roll = input("Roll number: ").strip()
        if not roll:
            print("Roll number cannot be empty. Try again.")
            continue
        records.append((name, roll))
        print("Record added.\n")
    return records


def write_students(records: List[Tuple[str, str]]) -> None:
    """Append student records to the storage file."""
    if not records:
        print("No records to save.")
        return
    try:
        with open(STORAGE_FILE, "a", encoding="utf-8") as file:
            for name, roll in records:
                file.write(f"{name} | {roll}\n")
        print(f"Saved {len(records)} record(s) to {STORAGE_FILE}.\n")
    except OSError as exc:
        print(f"Unable to write to {STORAGE_FILE}: {exc}")


def read_students() -> None:
    """Display all student records stored in the file."""
    try:
        with open(STORAGE_FILE, "r", encoding="utf-8") as file:
            contents = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"No data found. {STORAGE_FILE} does not exist yet.\n")
        return
    except OSError as exc:
        print(f"Unable to read {STORAGE_FILE}: {exc}\n")
        return

    if not contents:
        print("Student list is empty.\n")
        return

    print(f"\nStored Students ({len(contents)} record(s)):")
    print("-" * 40)
    for idx, record in enumerate(contents, start=1):
        try:
            name, roll = [part.strip() for part in record.split("|", maxsplit=1)]
        except ValueError:
            # Skip malformed lines but continue processing others.
            print(f"{idx}. [Malformed record skipped]")
            continue
        print(f"{idx}. Name: {name} | Roll: {roll}")
    print()


def main() -> None:
    """Offer a simple menu to write/read student data."""
    while True:
        print("Student Data Manager")
        print("1. Add student records")
        print("2. View student records")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()
        print()
        if choice == "1":
            records = gather_student_data()
            write_students(records)
        elif choice == "2":
            read_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")


if __name__ == "__main__":
    main()

