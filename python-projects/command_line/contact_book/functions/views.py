from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from .model import ContactsModel


class Window(QMainWindow):
    """Main Window."""
    def __init__(self,parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Contact Book")
        self.resize(550,250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        
        self.contactsModel = ContactsModel()
        self.setupUI()

    def setupUI(self):
        """Setup the main window's GUI."""
        #Create the table view widget
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        #Create buttons
        self.addButton = QPushButton("Add...")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete")
        self.clearAllButton = QPushButton("Clear All")
        #Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def openAddDialog(self):
        """Open the Add Contact dialog."""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.contactsModel.addContact(dialog.data)
            self.table.resizeColumnsToContents()


class AddDialog(QDialog):
    """Add Contact dialog."""
    def __init__(self, parent = None):
        """Initializer."""
        super().__init__(parent=parent)
        self.setWindowTitle("Add Contact")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        """Setup the Add Contact dialog's GUI."""
        #Create line edits for data fields
        self.first_nameField = QLineEdit()
        self.first_nameField.setObjectName("first_name")
        self.last_nameField = QLineEdit()
        self.last_nameField.setObjectName("last_name")
        self.phone_numberField = QLineEdit()
        self.phone_numberField.setObjectName("phone_number")
        self.emailField = QLineEdit()
        self.emailField.setObjectName("email")
        self.street_addressField = QLineEdit()
        self.street_addressField.setObjectName("street_address")
        #Lay out the data fields
        layout = QFormLayout()
        layout.addRow("First Name:", self.first_nameField)
        layout.addRow("Last Name:", self.last_nameField)
        layout.addRow("Phone Number:", self.phone_numberField)
        layout.addRow("Email:", self.emailField)
        layout.addRow("Street Address:", self.street_addressField)
        self.layout.addLayout(layout)
        #Add standard buttons to the dialog and connect them
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)

        def accept(self):
            """accept the data provied through the dialog."""
            self.data = []
            for field in (self.first_nameField, self.last_nameField, self.phone_numberField, self.emailField, self.street_addressField):
                if not field.text():
                    QMessageBox.critical(
                        self,
                        "Error!",
                        f"You must provide a contact's {field.objectName()}",
                    )
                    self.data = None # Reset .data
                    return

                self.data.append(field.text())

            if not self.data:
                return

            super().accept()
                    
        
