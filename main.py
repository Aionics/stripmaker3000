import sys
import code
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PIL import Image
from PIL.ImageQt import ImageQt
import threading
import time

import ui as ui_import

timer = None

def PILToQ(pilimage):
    imageq = ImageQt(pilimage)
    qimage = QImage(imageq)
    return qimage

def set_interval(func, sec):
    global timer
    def func_wrapper():
        set_interval(func, sec)
        func()
    timer = threading.Timer(sec, func_wrapper)
    timer.start()
    return timer

class Frame:
    def __init__(self, img, name):
        self.size = img.size
        self.pil_image = img
        self.preview_img = img
        self.name = name

    def preview_resize(self, direction):
        self.size = (self.size[0] * 2, self.size[1] * 2) if direction else (self.size[0] // 2, self.size[1] // 2)
        self.preview_img = self.preview_img.resize(self.size)

        return self.preview_img

class FrameList:
    def __init__(self, ui_list, ui_preview):
        def changedSelectedItem(current, previous):
            if current:
                self.selected_item = current

                self.ui_preview.hide()
                self.ui_preview.clear()
                pixel_map = QPixmap(PILToQ( self.frames[self.selected_item.f_id].preview_img ))
                self.ui_preview.setPixmap(pixel_map)
                self.ui_preview.show()

        self.ui_preview = ui_preview
        self.ui_list = ui_list
        self.ui_list_items = []
        self.ui_list.currentItemChanged.connect(changedSelectedItem)
        self.frames = []
        self.selected_item = None

    def __getitem__(self, index):
        return self.frames[index]
    def __len__(self):
        return len(self.frames)

    def add(self, frame):
        self.frames.append(frame)

    def nextFrame(self):
        new_id = 0 if self.selected_item.f_id == (len(self.frames) - 1) else self.selected_item.f_id + 1
        self.ui_list.setCurrentItem(self.ui_list_items[new_id])

    def moveItem(self, direction):
        if len(self.frames):
            current_id = self.selected_item.f_id
            next_id = current_id + 1 if direction else current_id - 1
            if next_id == len(self.frames): next_id = 0
            if next_id == -1: next_id = len(self.frames) - 1

            _frame = self.frames[next_id]
            self.frames[next_id] = self.frames[current_id]
            self.frames[current_id] = _frame
            self.redraw()

            self.ui_list.setCurrentItem(self.ui_list_items[next_id])

    def redraw(self):
        self.ui_list.clear()
        self.ui_list_items = []
        for i, frame in enumerate(self.frames):
            item = QListWidgetItem( frame.name )
            item.f_id = i
            self.ui_list.addItem(item)
            self.ui_list_items.append(item)
class Strip:
    def __init__(self, ui):
        self.ui = ui
        self.frames = FrameList(self.ui.list, self.ui.img_preview)
        self.path = None
        self.fps = float(self.ui.text_fps.toPlainText())
        self.loop_state = False

        self.setup()

    def setup(self):
        self.ui.group_left.hide()
        self.ui.group_right.hide()

        self.ui.actionOpen_gif.triggered.connect(self.openGif)
        self.ui.toggle_loop.stateChanged.connect(self.toggleLoop)
        self.ui.text_fps.textChanged.connect(self.changeFps)

        self.ui.btn_moveUp.clicked.connect(lambda x: self.frames.moveItem(0))
        self.ui.btn_moveDown.clicked.connect(lambda x: self.frames.moveItem(1))
        self.ui.btn_save.clicked.connect(lambda x: self.save())
        # self.ui.graphicsView

    def changeFps(self):
        if not self.loop_state:
            self.fps = min(60, max(1, float(self.ui.text_fps.toPlainText())))

    def toggleLoop(self, state):
        if state == 2:
            self.loop_state = True
            self.ui.text_fps.setEnabled(False)
            self.ui.text_fps.setPlainText(str(int(self.fps)))
            set_interval(self.frames.nextFrame, 1.0 / self.fps)
        if state == 0:
            self.loop_state = False
            self.ui.text_fps.setEnabled(True)
            timer.cancel()

    def openGif(self):
        self.path = str(QFileDialog.getOpenFileName())
        self.ui.label_source.setText(ui_import._translate("MainWindow", self.path, None))
        self.ui.group_left.show()
        self.ui.group_right.show()

        gif = Image.open(self.path)
        palette = gif.getpalette()
        try:
            i = 0
            while gif:
                gif.putpalette(palette)
                img = Image.new("RGBA", gif.size)
                img.paste(gif)
                self.frames.add( Frame(img, "frame_%s" % str(i).zfill(3)) )
                gif.seek(gif.tell() + 1)
                i+=1
        except Exception as e:
            pass

        self.frames.redraw()
        # self.frames.select(0)

    def save(self):
        filename = QFileDialog.getSaveFileName(self.ui.btn_save, "Save as strip", "strip.png", "PNG-strip (*.png)")
        width = self.frames[0].pil_image.size[0]
        height = self.frames[0].pil_image.size[1]
        strip_to_save = Image.new("RGBA", (width * len(self.frames), height))

        for i, frame in enumerate(self.frames):
            strip_to_save.paste(frame.pil_image, (i * width, 0))

        strip_to_save.save(str(filename))

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = ui_import.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
strip = Strip(ui)
sys.exit(app.exec_())
