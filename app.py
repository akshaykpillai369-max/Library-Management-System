import streamlit as st
from menu1 import Menu
from database1 import Database


def main():

    db = Database()
    menu = Menu(db)
    st.title("Library Management System 📚📚")
    

    choice = menu.show_sidebar()

    if choice == "View Books" :

        menu.show_all_books()

    elif choice == "Add Book":

        menu.add_book()

    elif choice == "Borrow Book" :

        menu.borrow_book()

    elif choice == "Delete Book":

        menu.delete_book()

    elif choice == "Return Book":
        menu.return_book()

    else:
        pass

if __name__ == "__main__" :

    main()

