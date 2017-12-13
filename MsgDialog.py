from PyQt5.QtWidgets import QMessageBox

class MsgDialog(QMessageBox):
    def __init__(self, title, text, info = ""):
        super(MsgDialog, self).__init__()
        msg = QMessageBox()
        #msg.setFixedSize(800,  60)
        msg .setWindowTitle(title)
        msg.setText(text);
        msg.setInformativeText(info);
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.exec()

    def showEvent(self, event):
        self.showEvent(event);
        self.setFixedSize(640, 480);

    def __del__(self):
        pass

class ErrorDialog(QMessageBox):
    def __init__(self, text, error):
        super(ErrorDialog, self).__init__()
        msg = QMessageBox()
        msg .setWindowTitle('Error')
        #msg.setFixedSize(80, 60);
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text);
        msg.setInformativeText(error);
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.exec();

    def __del__(self):
        pass
