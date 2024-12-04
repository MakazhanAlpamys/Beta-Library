STYLE_SHEET = """
QWidget {
    font-family: Arial;
    background-color: white;
}

QLineEdit {
    padding: 8px;
    border: 2px solid #e0e0e0;
    border-radius: 20px;
    font-size: 14px;
    min-width: 300px;
    margin: 5px;
}

QPushButton {
    background-color: #33B5FF;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 20px;
    font-size: 14px;
    min-width: 100px;
    margin: 5px;
}

QPushButton:hover {
    background-color: #2E9FE3;
}

QPushButton#linkButton {
    background-color: transparent;
    color: #33B5FF;
    text-decoration: underline;
    border: none;
}

QPushButton#linkButton:hover {
    color: #2E9FE3;
}

QLabel {
    font-size: 14px;
    color: #333;
}

QLabel#titleLabel {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}
"""