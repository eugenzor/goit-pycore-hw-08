import pickle

from colorama import init

from commands import (
    CommandError,
    add_birthday,
    add_contact,
    birthdays,
    change_contact,
    parse_input,
    show_all,
    show_birthday,
    show_phone,
)
from models import AddressBook
from utils import green, red

DATA_FILE = "addressbook.pkl"


def save_data(book: AddressBook, filename: str = DATA_FILE) -> None:
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename: str = DATA_FILE) -> AddressBook:
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main() -> None:
    init(autoreset=True)
    book = load_data()
    print(green("Welcome to the assistant bot!"))
    try:
        while True:
            try:
                user_input = input("Enter a command: ")
            except (EOFError, KeyboardInterrupt):
                print()
                print(green("Good bye!"))
                break

            command, *args = parse_input(user_input)

            try:
                match command:
                    case "close" | "exit":
                        print(green("Good bye!"))
                        break
                    case "":
                        print(red("Please enter a command."))
                        continue
                    case "hello":
                        print(green("How can I help you?"))
                    case "add":
                        print(green(add_contact(args, book)))
                    case "change":
                        print(green(change_contact(args, book)))
                    case "phone":
                        print(green(show_phone(args, book)))
                    case "all":
                        print(green(show_all(args, book)))
                    case "add-birthday":
                        print(green(add_birthday(args, book)))
                    case "show-birthday":
                        print(green(show_birthday(args, book)))
                    case "birthdays":
                        print(green(birthdays(args, book)))
                    case _:
                        print(red("Invalid command."))
            except CommandError as exc:
                print(red(str(exc)))
    finally:
        save_data(book)


if __name__ == "__main__":
    main()
