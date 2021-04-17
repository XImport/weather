import sys

from weather import Form, app

if __name__ == "__main__":
    Form.show()
    sys.exit(app.exec_())
