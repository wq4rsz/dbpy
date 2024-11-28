## Database
It is a simple Python application that uses PyQt5 and SQLite to manage users. The application allows you to add, delete and view users with their name, email address and password.

**Functionality**

- **Adding a user**: Users can be added to the database. When adding, it is checked that all fields are filled in and that the email address is unique.
- **Deleting a user**: Users can be deleted from the database with a simple click on an entry in the table.
- **User View**: All users are displayed in a table, which makes it easy to view information.

**Usage**

- Enter the name, email address and password to add a new user.
- Click the **Add User** button to add.
- To delete a user, select it in the table and click the **Delete User** button.

**Installation**

1. Make sure that you have Python installed (version 3.8 or higher).
2. Make sure that the PyQt5 library and sqlite3 are included in your Python installation.
3. Run the file using the command: `python main.py` or `python3 main.py` depending on your system.
