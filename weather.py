
import sys

from weather_base.style import Ui_Form
from weather_base import Form, app

if __name__ == "__main__":
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
