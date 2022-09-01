from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def _createContactsTable():
    """Create the contacts table in the database."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            first_name VARCHAR(40) NOT NULL,
            last_name VARCHAR(40) NOT NULL,
            phone_number BIGINT NOT NULL,
            email VARCHAR(40) NOT NULL,
            street_address VARCHAR(80) NOT NULL
        )
        """
    )

def createConnection(contacts):
    """Create and open a database connection."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(contacts)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Contact Book",
            f"Database Error: {connection.lastError().text()}",
        )
        return False
    _createContactsTable()
    return True


