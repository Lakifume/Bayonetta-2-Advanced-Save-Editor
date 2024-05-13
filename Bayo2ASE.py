import Manager

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import os
import sys
import time
import traceback

script_name = os.path.splitext(os.path.basename(__file__))[0]

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class DragDropButton(QPushButton):
    def __init__(self, text, window):
        super(DragDropButton, self).__init__(text)
        self.text = text
        self.window = window
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, event):
        md = event.mimeData()
        if md.hasUrls():
            if len(md.urls()) == 1:
                if os.path.splitext(md.urls()[0].toLocalFile())[1] == ".sav":
                    event.accept()
                    self.setText("Drop File")
    
    def dragLeaveEvent(self, event):
        self.setText(self.text)
    
    def dropEvent(self, event):
        md = event.mimeData()
        self.window.open_save_file(md.urls()[0].toLocalFile().replace("/", "\\"))
        self.setText(self.text)

class MainWindow(QGraphicsView):
    def __init__(self):
        super().__init__()
        sys.excepthook = self.exception_hook
        self.initUI()

    def initUI(self):
        self.save_file_path = ""
        
        self.setStyleSheet("QWidget{background: transparent; color: #ffffff; font-family: Cambria; font-size: 18px}"
        + "QGraphicsView{background-color: #1a1a1a}"
        + "QComboBox{background-color: #262626; selection-background-color: #320288ff}"
        + "QComboBox QAbstractItemView{border: 1px solid #262626}"
        + "QScrollBar::add-page{background-color: #202020}"
        + "QScrollBar::sub-page{background-color: #202020}"
        + "QMessageBox{background-color: #262626}"
        + "QPushButton{background-color: #262626}"
        + "QSpinBox{background-color: #262626; selection-background-color: #320288ff}")
        
        #Main layout
        
        main_window_layout = QVBoxLayout()
        main_window_layout.setSpacing(10)
        self.setLayout(main_window_layout)
        
        hbox_1_layout = QHBoxLayout()
        main_window_layout.addLayout(hbox_1_layout)
        
        hbox_2_layout = QHBoxLayout()
        main_window_layout.addLayout(hbox_2_layout)
        
        hbox_3_layout = QHBoxLayout()
        main_window_layout.addLayout(hbox_3_layout)
        
        hbox_4_layout = QHBoxLayout()
        main_window_layout.addLayout(hbox_4_layout)
        
        hbox_5_layout = QHBoxLayout()
        main_window_layout.addLayout(hbox_5_layout)

        #Groupboxes

        box_1_layout = QVBoxLayout()
        box_1 = QGroupBox("Character")
        box_1.setLayout(box_1_layout)
        hbox_1_layout.addWidget(box_1)

        box_2_layout = QVBoxLayout()
        box_2 = QGroupBox("Costume")
        box_2.setLayout(box_2_layout)
        hbox_1_layout.addWidget(box_2)

        box_3_layout = QVBoxLayout()
        box_3 = QGroupBox("Weapons")
        box_3.setLayout(box_3_layout)
        hbox_2_layout.addWidget(box_3)

        box_4_layout = QVBoxLayout()
        box_4 = QGroupBox("Accessories")
        box_4.setLayout(box_4_layout)
        hbox_2_layout.addWidget(box_4)

        box_5_layout = QVBoxLayout()
        box_5 = QGroupBox("Chapter")
        box_5.setLayout(box_5_layout)
        hbox_3_layout.addWidget(box_5)

        box_6_layout = QVBoxLayout()
        box_6 = QGroupBox("Checkpoint")
        box_6.setLayout(box_6_layout)
        hbox_3_layout.addWidget(box_6)

        box_7_layout = QHBoxLayout()
        box_7 = QGroupBox("Items")
        box_7.setLayout(box_7_layout)
        hbox_4_layout.addWidget(box_7)
        
        #Drop down lists
        
        self.character_drop_down = QComboBox()
        self.character_drop_down.currentTextChanged.connect(self.character_drop_down_changed)
        box_1_layout.addWidget(self.character_drop_down)
        
        self.costume_drop_down = QComboBox()
        box_2_layout.addWidget(self.costume_drop_down)
        
        self.weapon_drop_down_1 = QComboBox()
        box_3_layout.addWidget(self.weapon_drop_down_1)
        
        self.weapon_drop_down_2 = QComboBox()
        box_3_layout.addWidget(self.weapon_drop_down_2)
        
        self.weapon_drop_down_3 = QComboBox()
        box_3_layout.addWidget(self.weapon_drop_down_3)
        
        self.weapon_drop_down_4 = QComboBox()
        box_3_layout.addWidget(self.weapon_drop_down_4)
        
        self.accessory_drop_down_1 = QComboBox()
        box_4_layout.addWidget(self.accessory_drop_down_1)
        
        self.accessory_drop_down_2 = QComboBox()
        box_4_layout.addWidget(self.accessory_drop_down_2)
        
        self.accessory_drop_down_3 = QComboBox()
        box_4_layout.addWidget(self.accessory_drop_down_3)
        
        self.chapter_drop_down = QComboBox()
        self.chapter_drop_down.currentTextChanged.connect(self.chapter_drop_down_changed)
        box_5_layout.addWidget(self.chapter_drop_down)
        
        self.checkpoint_drop_down = QComboBox()
        box_6_layout.addWidget(self.checkpoint_drop_down)
        
        self.item_drop_down = QComboBox()
        self.item_drop_down.currentTextChanged.connect(self.item_drop_down_changed)
        box_7_layout.addWidget(self.item_drop_down)
        
        #SpinBoxes
        
        self.item_quantity_field = QSpinBox()
        self.item_quantity_field.valueChanged.connect(self.item_quantity_field_changed)
        box_7_layout.addWidget(self.item_quantity_field)

        #Buttons
        
        self.button_1 = DragDropButton("Open", self)
        self.button_1.clicked.connect(self.button_1_clicked)
        hbox_5_layout.addWidget(self.button_1)
        
        self.button_2 = QPushButton("Save")
        self.button_2.clicked.connect(self.button_2_clicked)
        hbox_5_layout.addWidget(self.button_2)
        
        #Window
        
        self.setFixedSize(666, 500)
        self.setWindowTitle(script_name)
        self.setWindowIcon(QIcon(resource_path("Bayo2.ico")))
        self.show()
        
        #Position
        
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())
        
        self.set_widgets_enabled(False)
        QApplication.processEvents()
    
    def set_widgets_enabled(self, enabled):
        for i in self.children():
            if i != self.button_1:
                i.setEnabled(enabled)
    
    def open_save_file(self, save_path):
        Manager.init()
        Manager.read_from_save_file(save_path)
        if not self.save_file_path:
            self.reset_drop_down_lists()
        self.save_file_path = save_path
        self.read_from_config()
        self.setWindowTitle(f"{script_name} ({save_path[-70:]})")
        self.set_widgets_enabled(True)
    
    def button_1_clicked(self):
        file = QFileDialog.getOpenFileName(parent=self, caption="File", filter="*.sav")[0]
        if file:
            self.open_save_file(file.replace("/", "\\"))
    
    def button_2_clicked(self):
        self.write_to_config()
        Manager.write_to_save_file(self.save_file_path)
        self.button_2.setText("File Saved")
        QApplication.processEvents()
        time.sleep(1.5)
        self.button_2.setText("Save")
    
    def read_from_config(self):
        self.character_drop_down.setCurrentText(Manager.status_config["Character"])
        self.costume_drop_down.setCurrentText(Manager.status_config["Costume"])
        self.weapon_drop_down_1.setCurrentText(Manager.status_config["Weapon 1"])
        self.weapon_drop_down_2.setCurrentText(Manager.status_config["Weapon 2"])
        self.weapon_drop_down_3.setCurrentText(Manager.status_config["Weapon 3"])
        self.weapon_drop_down_4.setCurrentText(Manager.status_config["Weapon 4"])
        self.accessory_drop_down_1.setCurrentText(Manager.status_config["Accessory 1"])
        self.accessory_drop_down_2.setCurrentText(Manager.status_config["Accessory 2"])
        self.accessory_drop_down_3.setCurrentText(Manager.status_config["Accessory 3"])
        self.chapter_drop_down.setCurrentText(Manager.status_config["Chapter"])
        self.checkpoint_drop_down.setCurrentText(Manager.status_config["Checkpoint"])
        self.item_drop_down_changed(self.item_drop_down.currentText())
    
    def write_to_config(self):
        Manager.status_config["Character"] = self.character_drop_down.currentText()
        Manager.status_config["Costume"] = self.costume_drop_down.currentText()
        Manager.status_config["Weapon 1"] = self.weapon_drop_down_1.currentText()
        Manager.status_config["Weapon 2"] = self.weapon_drop_down_2.currentText()
        Manager.status_config["Weapon 3"] = self.weapon_drop_down_3.currentText()
        Manager.status_config["Weapon 4"] = self.weapon_drop_down_4.currentText()
        Manager.status_config["Accessory 1"] = self.accessory_drop_down_1.currentText()
        Manager.status_config["Accessory 2"] = self.accessory_drop_down_2.currentText()
        Manager.status_config["Accessory 3"] = self.accessory_drop_down_3.currentText()
        Manager.status_config["Chapter"] = self.chapter_drop_down.currentText()
        Manager.status_config["Checkpoint"] = self.checkpoint_drop_down.currentText()
    
    def reset_drop_down_lists(self):
        self.reset_character_drop_down()
        self.reset_costume_drop_down()
        self.reset_weapon_drop_down()
        self.reset_accessory_drop_down()
        self.reset_chapter_drop_down()
        self.reset_checkpoint_drop_down()
        self.reset_item_drop_down()
    
    def reset_character_drop_down(self):
        self.character_drop_down.clear()
        for item in Manager.character_to_id:
            self.character_drop_down.addItem(item)
    
    def reset_costume_drop_down(self):
        self.costume_drop_down.clear()
        character = self.character_drop_down.currentText()
        for item in Manager.costume_to_id[character]:
            self.costume_drop_down.addItem(item)
    
    def reset_weapon_drop_down(self):
        self.weapon_drop_down_1.clear()
        self.weapon_drop_down_2.clear()
        self.weapon_drop_down_3.clear()
        self.weapon_drop_down_4.clear()
        character = self.character_drop_down.currentText()
        for item in Manager.weapon_to_id[character]:
            self.weapon_drop_down_1.addItem(item)
            self.weapon_drop_down_2.addItem(item)
            self.weapon_drop_down_3.addItem(item)
            self.weapon_drop_down_4.addItem(item)
    
    def reset_accessory_drop_down(self):
        self.accessory_drop_down_1.clear()
        self.accessory_drop_down_2.clear()
        self.accessory_drop_down_3.clear()
        for item in Manager.accessory_to_id:
            self.accessory_drop_down_1.addItem(item)
            self.accessory_drop_down_2.addItem(item)
            self.accessory_drop_down_3.addItem(item)
    
    def reset_chapter_drop_down(self):
        self.chapter_drop_down.clear()
        for item in Manager.chapter_to_id:
            self.chapter_drop_down.addItem(item)
    
    def reset_checkpoint_drop_down(self):
        self.checkpoint_drop_down.clear()
        self.checkpoint_drop_down.addItem("None")
        chapter = self.chapter_drop_down.currentText()
        if chapter in Manager.checkpoint_to_id:
            for item in Manager.checkpoint_to_id[chapter]:
                self.checkpoint_drop_down.addItem(item)
    
    def reset_item_drop_down(self):
        self.item_drop_down.clear()
        for item in Manager.item_to_offset:
            self.item_drop_down.addItem(item)
    
    def character_drop_down_changed(self, text):
        self.reset_costume_drop_down()
        self.reset_weapon_drop_down()
    
    def chapter_drop_down_changed(self, text):
        self.reset_checkpoint_drop_down()
    
    def item_drop_down_changed(self, text):
        self.item_quantity_field.setRange(0, 99999999)
        self.item_quantity_field.setValue(Manager.item_config[text])
        self.item_quantity_field.setRange(Manager.item_to_range[text][0], Manager.item_to_range[text][1])
    
    def item_quantity_field_changed(self, value):
        Manager.item_config[self.item_drop_down.currentText()] = value
    
    def exception_hook(self, exc_type, exc_value, exc_traceback):
        box = QMessageBox(self)
        box.setWindowTitle("Error")
        box.setIcon(QMessageBox.Critical)
        box.setText("An error has occured")
        traceback_format = traceback.format_exception(exc_type, exc_value, exc_traceback)
        traceback_string = "".join(traceback_format)
        box.setInformativeText(traceback_string)
        box.exec()

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()