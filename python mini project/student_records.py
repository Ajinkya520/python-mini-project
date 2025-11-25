"""Simple student record manager using basic file handling."""

from pathlib import Path

DATA_FILE = Path("students.txt")


def save_student(name: str, roll_number: str) -> None:
    """Append a single student entry to the data file."""
    with DATA_FILE.open("a", encoding="utf-8") as file:
        file.write(f"{name},{roll_number}\n")


def read_students() -> list[tuple[str, str]]:
    """Read all student entries from the data file."""
    if not DATA_FILE.exists():
        return []

    students: list[tuple[str, str]] = []
    with DATA_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            name, roll = line.strip().split(",", maxsplit=1)
            students.append((name, roll))
    return students


def main() -> None:
    print("Student Record Manager")
    print("----------------------")
    while True:
        name = input("Enter student name (leave blank to stop): ").strip()
        if not name:
            break
        roll = input("Enter roll number: ").strip()
        save_student(name, roll)
        print("Saved!\n")

    print("\nAll saved students:")
    records = read_students()
    if not records:
        print("No records found yet.")
    else:
        for idx, (name, roll) in enumerate(records, start=1):
            print(f"{idx}. {name} - Roll No: {roll}")


if __name__ == "__main__":
    main()

