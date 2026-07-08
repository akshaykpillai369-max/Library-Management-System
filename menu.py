import streamlit as st


class Menu:

    def __init__(self, db):
        self.db = db

    
    def show_sidebar(self):

        st.sidebar.header("Inventory")
        decision = st.sidebar.radio("--Select-- ",["View Books", "Add Book", "Borrow Book", "Delete Book", "Return Book"], index = None)
        return decision
    

    def show_all_books(self):

        st.subheader("Available Books")

        results = self.db.view_all_books()

        if results:
            pass

        else:

            st.warning("No Books Were Added")
        

        for result in results:
            st.write(f" ID : {result[0]} {result[1]} by {result[2]}  Status : {"Borrowed 🔴" if result[3] == 1  else "Available 🟢"}")   

    def add_book(self):

        st.subheader("Add A New Book")
        with st.form("Add a book"):

            title = st.text_input("Enter The Name of the Book")
            author = st.text_input("Enter The Name of the Author")

            submit = st.form_submit_button("Submit")

            if submit:
                if title and author :

                    
                    self.db.add_book(title, author)
                    st.success("Book added successfully")
                 
                    
                
                else:
                    st.error("Please fill the fields")

                    




    def borrow_book(self):

        st.subheader("Borrow a book")
        self.show_all_books()
        sl_no= st.number_input("Enter the id of the book you want to borrow", min_value=0, step=1)
        submit = st.button("Submit")
        
        if submit :

            result = self.db.borrow_book(sl_no)

            if "successfully" in result:
                st.toast("Book Borrowed Successfully")
                st.rerun()
            else:
                st.error(result)   

    def delete_book(self):

        st.subheader("Delete book")

        self.show_all_books()

        sl_no= st.number_input("Enter the id of the book you want to delete", min_value=1, step=1)

        submit = st.button("Submit")

        if submit:
            if sl_no:


                self.db.delete_book(sl_no)
                st.toast("Book Borrowed Successfully")
                st.rerun() 
                
            else:
                st.error("Please fill the fields")

        
                

    def return_book(self):

        st.subheader("Return a Borrowed Book")

        self.show_all_books()

        sl_no= st.number_input("Enter the id of the book you want to return", min_value=1, step=1)

        submit = st.button("Submit")

        if submit:
            result = self.db.return_book(sl_no)
            # FIX: Handle success or error validation properly before rerunning
            if "Successfully" in result:
                st.toast("Book Borrowed Successfully")
                st.rerun()
            else:
                st.error(result)

