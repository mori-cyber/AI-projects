# This Python file uses the following encoding: utf-8



import urllib.request
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox ,QDialog
from PySide6.QtUiTools import QUiLoader
import sys
class Downloder(QDialog):
    def __init__(self):
        super(Downloder, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('form.ui')
        self.ui.show()

        self.ui.Download.clicked.connect(self.download)
        self.ui.Browser.clicked.connect(self.browser)
    def browser(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Save File As")

        self.ui.txt_dest.setText(save_file[0])
    def download(self):

        url = self.ui.txt_url.text()
        # url.setPlaceholderText("URL")
        save_location = self.ui.txt_dis.text()

        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "The download failed!")
            return

        QMessageBox.information(self,  "complete")
        self.ui.progressBar.setValue(0)
        self.ui.txt_url.setText('')
        self.ui.txt_dis.setText('')

    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize

        if totalsize > 0:
            percent = readsofar * 100 / totalsize
            self.ui.progressBar.setValue(int(percent))





if __name__ == "__main__":
    app = QApplication([])
    widget = Downloder()
    widget.show()
    sys.exit(app.exec_())