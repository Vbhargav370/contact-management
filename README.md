# contact-management
Project Summary: Development of a Contact Management System
This paper discusses a desktop application where users can save and manage dados such as names, phone numbers and addresses without stress. The said system enables users to;

In the first place create new contacts
Check and Look contacts by Names or Telephone Numbers
Modify already existing contacts
Remove contacts
View and Edit the contact in the List, sorting and filtering it over the data provided
Keep the contact details in a file, or a similar database, for a long time
This application is developed and created using a framework called PyQt5, a human-friendly application development library designed in Python to enhance the visual appearance of the project.

Used Libraries
1. PyQt5
Summary: PyQt5 is the Python interface for the well-known cross-platform application development framework known as the Qt framework. used primarily for developing graphical desktop applications.

Justification for Usage:

Graphical User Interface Elements: With PyQt5, one can have all the widgets such as buttons, texts, tables, and even dialog boxes needed to make an interface.
User Interaction: PyQt5 helps in receiving the action performed by the user like pressing a button or altering the text in a box and allows interaction within the application.
Model View Control: This was particularly used in the table widget for managing contacts information that is arranged in these tables including column sorting.

2. Python Standard Libraries

sys: which is for the system specific parameters and functions (included in the beginning to launch the program).
PyQt5.QtWidgets: this includes all the components which are required for creating the user interface of the application (for example QTableWidget, QPushButton, QLineEdit, QMessageBox).
PyQt5.QtCore: provides the ability to use basic functions and typical classes like how signals and slots are used to handle events and how text and widgets are laid out in Qt.
QMessageBox: For the pop-up boxes that require a Yes or No answer (e.g. when one deletes a contact).
