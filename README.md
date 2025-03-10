# Employee Management System

## Overview

The **Employee Management System** is a desktop application built using Python's `Tkinter` library for the graphical user interface (GUI) and `MySQL` for database management. This application allows users to perform CRUD (Create, Read, Update, Delete) operations on employee records. It is designed to manage employee information such as name, department, designation, email, address, marital status, date of birth, date of joining, ID proof, gender, phone number, country, and salary.

This project is an excellent example of integrating a GUI with a database, making it suitable for interview discussions to demonstrate your skills in Python, Tkinter, MySQL, and software development.

![image alt](https://github.com/saurabhsoljar/Employee-Management-System/blob/87e9e7571c24792e6ce328dff04ec6ff0a996bc7/emp.png)

---

## Features

1. **Add Employee Data**:

   - Users can add new employee records to the database.
   - Validates required fields before submission.

2. **Fetch Employee Data**:

   - Fetches all employee records from the database and displays them in a table.

3. **Update Employee Data**:

   - Allows users to update existing employee records.
   - Validates required fields before updating.

4. **Delete Employee Data**:

   - Deletes an employee record from the database based on the ID proof.

5. **Search Employee Data**:

   - Searches for employee records based on specific criteria (e.g., phone number or ID proof).
   - Displays matching records in the table.

6. **Reset Form**:

   - Clears all input fields in the form for new data entry.

7. **User-Friendly Interface**:
   - Intuitive and visually appealing GUI with proper alignment and design.

---

## Technologies Used

- **Python**: Primary programming language.
- **Tkinter**: Used for creating the graphical user interface (GUI).
- **MySQL**: Database management system for storing employee records.
- **PIL (Pillow)**: Used for handling and displaying images in the GUI.
- **mysql-connector-python**: Python library for connecting to and interacting with the MySQL database.

---

## Project Structure

### 1. **Frontend (Tkinter GUI)**:

- **Main Window**:
  - Displays the title and logo of the application.
  - Contains frames for employee information input, buttons for actions, and a table for displaying records.
- **Input Fields**:
  - Text fields, dropdowns, and comboboxes for entering employee details.
- **Buttons**:
  - Buttons for adding, updating, deleting, searching, and resetting data.
- **Table**:
  - Displays employee records in a tabular format with scrollbars.

### 2. **Backend (MySQL Database)**:

- **Database**:
  - A MySQL database named `employee` is used to store employee records.
- **Table**:
  - A table named `employees` is created with columns for all employee details.

### 3. **Functionality**:

- **Database Connection**:
  - Establishes a connection to the MySQL database using `mysql.connector`.
- **CRUD Operations**:
  - Functions to add, fetch, update, and delete employee records.
- **Search Functionality**:
  - Allows searching for records based on specific criteria.
- **Form Reset**:
  - Clears all input fields for new data entry.

---

## Code Explanation

### 1. **Database Connection**:

- The application connects to the MySQL database using the `mysql.connector` library.
- Connection details (host, user, password, database) are hardcoded for simplicity.

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="employee",
)
```

### 2. **Add Employee Data**:

- Validates required fields (department and email).
- Inserts a new record into the `employees` table.

```python
def add_data(self):
    if self.var_dep.get() == "" or self.var_email.get() == "":
        messagebox.showerror("Error", "All Fields are required")
    else:
        try:
            conn = mysql.connector.connect(...)
            my_cursor = conn.cursor()
            my_cursor.execute("insert into employees values(...)")
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("success", "Employee has been added!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)
```

### 3. **Fetch Employee Data**:

- Fetches all records from the `employees` table and displays them in the table widget.

```python
def fetch_data(self):
    conn = mysql.connector.connect(...)
    my_cursor = conn.cursor()
    my_cursor.execute("select * from employees")
    data = my_cursor.fetchall()
    if len(data) != 0:
        self.employee_table.delete(*self.employee_table.get_children())
        for i in data:
            self.employee_table.insert("", END, values=i)
    conn.close()
```

### 4. **Update Employee Data**:

- Updates an existing employee record based on the ID proof.

```python
def update_data(self):
    if self.var_dep.get() == "" or self.var_email.get() == "":
        messagebox.showerror("Error", "All Fields are required")
    else:
        try:
            update = messagebox.askyesno("Update", "Are you update employee data")
            if update > 0:
                conn = mysql.connector.connect(...)
                my_cursor = conn.cursor()
                my_cursor.execute("update employees set ... where id_proof=%s", (...))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success", "Employee Successfully Updated", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
```

### 5. **Delete Employee Data**:

- Deletes an employee record based on the ID proof.

```python
def delete_data(self):
    if self.var_idproof.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
    else:
        try:
            delete = messagebox.askyesno("Delete", "Are you Sure delete this message", parent=self.root)
            if delete > 0:
                conn = mysql.connector.connect(...)
                my_cursor = conn.cursor()
                sql = "delete from employees where id_proof=%s"
                value = (self.var_idproof.get(),)
                my_cursor.execute(sql, value)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete", "Employee Successfully Deleted", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
```

### 6. **Search Employee Data**:

- Searches for employee records based on a selected column (e.g., phone or ID proof) and a search term.

```python
def search_data(self):
    if self.var_com_search.get() == "" or self.var_search.get() == "":
        messagebox.showerror("Error", "Please select a search option and enter a search term.", parent=self.root)
    else:
        try:
            conn = mysql.connector.connect(...)
            my_cursor = conn.cursor()
            query = "SELECT * FROM employees WHERE " + str(self.var_com_search.get()) + " LIKE %s"
            value = ("%" + str(self.var_search.get()) + "%",)
            my_cursor.execute(query, value)
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.employee_table.delete(*self.employee_table.get_children())
                for row in rows:
                    self.employee_table.insert("", END, values=row)
            else:
                messagebox.showinfo("Info", "No matching records found.", parent=self.root)
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
```

---

## How to Run the Project

1. **Prerequisites**:

   - Install Python 3.x.
   - Install the required libraries:
     ```bash
     pip install mysql-connector-python pillow
     ```
   - Set up a MySQL database named `employee` and create a table `employees` with the required columns.

2. **Run the Application**:

   - Execute the Python script:
     ```bash
     python employee_management_system.py
     ```

3. **Database Setup**:
   - Create a MySQL database and table using the following SQL commands:
     ```sql
     CREATE DATABASE employee;
     USE employee;
     CREATE TABLE employees (
         Department VARCHAR(50),
         Name VARCHAR(50),
         Designition VARCHAR(50),
         Email VARCHAR(50),
         Address VARCHAR(100),
         Married_status VARCHAR(20),
         DOB VARCHAR(20),
         DOJ VARCHAR(20),
         id_proof_type VARCHAR(50),
         id_proof VARCHAR(50),
         gender VARCHAR(10),
         Phone VARCHAR(15),
         Country VARCHAR(50),
         Salary VARCHAR(20)
     );
     ```

---

## Screenshots

1. **Main Window**:
   ![Main Window](screenshots/main_window.png)

2. **Add Employee**:
   ![Add Employee](screenshots/add_employee.png)

3. **Search Employee**:
   ![Search Employee](screenshots/search_employee.png)

---

## Interview Discussion Points

1. **Why Tkinter?**

   - Tkinter is lightweight, easy to use, and comes pre-installed with Python, making it ideal for small desktop applications.

2. **Database Design**:

   - Explain the structure of the `employees` table and why certain data types were chosen.

3. **Error Handling**:

   - Discuss how exceptions are handled in the code to ensure robustness.

4. **Future Improvements**:

   - Suggest enhancements like user authentication, exporting data to Excel, or adding more search filters.

5. **Challenges Faced**:
   - Discuss any challenges faced during development, such as handling database connections or designing the GUI.

---

## the functions and their working:

This Python code implements an Employee Management System using the Tkinter GUI toolkit and a MySQL database. Here's a breakdown of the functions and their working:

**1. `__init__(self, root)`:**

* **Purpose:** This is the constructor of the `Employee` class. It initializes the GUI window, sets up the layout, and defines the variables used in the application.
* **Working:**
    * Sets the main window's geometry and title.
    * Initializes `StringVar` objects to hold the data entered by the user.
    * Creates and places labels, entry fields, combo boxes, buttons, and frames to form the GUI layout.
    * Loads and displays images for the logo and the employee profile.
    * Sets up the Treeview widget to display the employee data in a tabular format.
    * Calls `self.fetch_data()` to initially populate the Treeview with data from the database.
    * Bind the `<ButtonRelease>` event of the treeview to the get_cursor function.

**2. `add_data(self)`:**

* **Purpose:** Adds a new employee record to the MySQL database.
* **Working:**
    * Checks if the department and email fields are empty. If so, it displays an error message.
    * Establishes a connection to the MySQL database.
    * Executes an `INSERT` SQL query to add the employee's data to the `employees` table.
    * Commits the changes and closes the database connection.
    * Calls `self.fetch_data()` to update the Treeview with the new data.
    * Displays a success message or an error message if an exception occurs.

**3. `fetch_data(self)`:**

* **Purpose:** Retrieves all employee records from the MySQL database and displays them in the Treeview.
* **Working:**
    * Establishes a connection to the MySQL database.
    * Executes a `SELECT` SQL query to retrieve all records from the `employees` table.
    * Clears the existing data in the Treeview.
    * Iterates through the retrieved data and inserts each record as a row in the Treeview.
    * Commits the changes and closes the database connection.

**4. `get_cursor(self, event="")`:**

* **Purpose:** Retrieves the data from the selected row in the Treeview and populates the corresponding entry fields.
* **Working:**
    * Gets the currently focused row in the Treeview.
    * Retrieves the data from the selected row.
    * Sets the `StringVar` objects with the retrieved data, which updates the entry fields and combo boxes.

**5. `update_data(self)`:**

* **Purpose:** Updates an existing employee record in the MySQL database.
* **Working:**
    * Checks if the department and email fields are empty. If so, it displays an error message.
    * Asks the user to confirm the update action.
    * Establishes a connection to the MySQL database.
    * Executes an `UPDATE` SQL query to modify the employee's data in the `employees` table.
    * Commits the changes and closes the database connection.
    * Calls `self.fetch_data()` to update the Treeview with the modified data.
    * Displays a success message or an error message if an exception occurs.

**6. `delete_data(self)`:**

* **Purpose:** Deletes an employee record from the MySQL database.
* **Working:**
    * Checks if the ID proof field is empty. If so, it displays an error message.
    * Asks the user to confirm the delete action.
    * Establishes a connection to the MySQL database.
    * Executes a `DELETE` SQL query to remove the employee's record from the `employees` table.
    * Commits the changes and closes the database connection.
    * Calls `self.fetch_data()` to update the Treeview.
    * Displays a success message or an error message if an exception occurs.

**7. `reset_data(self)`:**

* **Purpose:** Clears all the entry fields and combo boxes.
* **Working:**
    * Sets all `StringVar` objects to their default values or empty strings.

**8. `search_data(self)`:**

* **Purpose:** Searches for employee records in the MySQL database based on the selected search criteria.
* **Working:**
    * Checks if the search option and search term are provided. If not, it displays an error message.
    * Establishes a connection to the MySQL database.
    * Constructs a `SELECT` SQL query with a `LIKE` clause to perform the search.
    * Executes the query with the search term.
    * Clears the existing data in the Treeview.
    * Inserts the matching records into the Treeview.
    * displays a message if no records are found.
    * Closes the database connection.
    * Displays an error message if an exception occurs.

**Key improvements and explanations:**

* **Parameterized Queries:** The `search_data` function now uses parameterized queries, which is crucial for preventing SQL injection vulnerabilities.
* **Error Handling:** The `try...except` blocks are used to handle potential exceptions during database operations, providing more robust error handling.
* **Clearer Messages:** The message boxes provide more informative messages to the user.
* **Code Clarity:** Added comments and explanations to improve code readability.
* **Scrollbars:** Scrollbars are added to the treeview, allowing the user to scroll through the data when there are many rows or columns.
* **Cursor binding:** the get_cursor function is now called when the user clicks on a row of data, making the function more user friendly.

## Conclusion

The **Employee Management System** is a practical application that demonstrates your ability to integrate a GUI with a database. It showcases your skills in Python, Tkinter, MySQL, and software development, making it an excellent project to discuss during interviews.
