import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, 
    QVBoxLayout, QPushButton, QDialog, QLineEdit, QLabel, 
    QHBoxLayout, QMessageBox, QWidget, QHeaderView
)
from PyQt5.QtCore import Qt

class ContactManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contact Manager")
        self.setGeometry(100, 100, 900, 600)

        self.contacts = []  # List to store contact details

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Filter/Search Bar
        self.filter_input = QLineEdit()
        self.filter_input.setPlaceholderText("Search contacts...")
        self.filter_input.textChanged.connect(self.filter_contacts)
        layout.addWidget(self.filter_input)

        # Add Buttons
        button_layout = QHBoxLayout()
        add_button = QPushButton("Add Contact")
        add_button.clicked.connect(self.add_contact_dialog)
        button_layout.addWidget(add_button)

        delete_button = QPushButton("Delete Selected Contact")
        delete_button.clicked.connect(self.delete_contact)
        button_layout.addWidget(delete_button)

        layout.addLayout(button_layout)

        # Table to Display Contacts
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Phone", "Email", "Address"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSortingEnabled(True)  # Enable sorting
        self.table.cellDoubleClicked.connect(self.update_contact_dialog)
        layout.addWidget(self.table)

        # Main Widget
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def add_contact_dialog(self):
        dialog = ContactDialog()
        if dialog.exec_() == QDialog.Accepted:
            name, phone, email, address = dialog.get_contact_data()
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            self.refresh_table()

    def update_contact_dialog(self, row):
        contact = self.contacts[row]
        dialog = ContactDialog(contact)
        if dialog.exec_() == QDialog.Accepted:
            name, phone, email, address = dialog.get_contact_data()
            self.contacts[row] = {"name": name, "phone": phone, "email": email, "address": address}
            self.refresh_table()

    def delete_contact(self):
        selected_row = self.table.currentRow()
        if selected_row != -1:
            confirm = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this contact?",
                                           QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                del self.contacts[selected_row]
                self.refresh_table()

    def refresh_table(self):
        # Clear the table
        self.table.setRowCount(0)

        # Add contacts to the table
        for contact in self.contacts:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(contact["name"]))
            self.table.setItem(row_position, 1, QTableWidgetItem(contact["phone"]))
            self.table.setItem(row_position, 2, QTableWidgetItem(contact["email"]))
            self.table.setItem(row_position, 3, QTableWidgetItem(contact["address"]))

    def filter_contacts(self):
        # Get the text from the search bar
        filter_text = self.filter_input.text().lower()
        for row in range(self.table.rowCount()):
            # Check if any column contains the filter text
            match = any(filter_text in self.table.item(row, col).text().lower() for col in range(self.table.columnCount()))
            # Show or hide the row based on the match
            self.table.setRowHidden(row, not match)


class ContactDialog(QDialog):
    def __init__(self, contact=None):
        super().__init__()
        self.setWindowTitle("Contact Details")
        self.setGeometry(200, 200, 400, 300)

        self.name_field = QLineEdit()
        self.phone_field = QLineEdit()
        self.email_field = QLineEdit()
        self.address_field = QLineEdit()

        if contact:
            self.name_field.setText(contact["name"])
            self.phone_field.setText(contact["phone"])
            self.email_field.setText(contact["email"])
            self.address_field.setText(contact["address"])

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_field)
        layout.addWidget(QLabel("Phone:"))
        layout.addWidget(self.phone_field)
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_field)
        layout.addWidget(QLabel("Address:"))
        layout.addWidget(self.address_field)

        button_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.accept)
        button_layout.addWidget(save_button)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def get_contact_data(self):
        return (
            self.name_field.text(),
            self.phone_field.text(),
            self.email_field.text(),
            self.address_field.text(),
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContactManager()
    window.show()
    sys.exit(app.exec_())
