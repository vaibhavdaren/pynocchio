# -*- coding: UTF-8 -*-
from PySide import QtCore, QtGui
from comic import Comic


class Model(QtCore.QObject):

    def __init__(self, parent=None):

        QtCore.QObject.__init__(self, parent)

        self.comic = None
        self.original_pixmap = QtGui.QPixmap()

        self.adjustType = '&Horizontal Adjust'
        self.screenSize = 0
        self.rotateAngle = 0

    def open(self):

        # fname, filt = QtGui.QFileDialog.getOpenFileName(
        #     self.parent(), 'Open comic file', QtCore.QDir.currentPath(),
        #     'All supported files (*.zip *.cbz *.rar *.cbr)\
        #     ;;Zip Files (*.zip *.cbz);;Rar Files (*.rar *.cbr)\
        #     ;;All files (*)')

        fname = '../quadrinhos/_scansPROJECT_Hoshigami_no_Satsuki.zip'

        if fname is not None:

            self.comic = Comic()

            if self.comic.load(fname):
                print u"Comic Loaded"
                return self.get_current_page(), self.comic.name

        return None

    def next_page(self):
        self.comic.go_next_page()
        return self.get_current_page()

    def previous_page(self):
        self.comic.go_previous_page()
        return self.get_current_page()

    def first_page(self):
        self.comic.go_first_page()
        return self.get_current_page()

    def last_page(self):
        self.comic.go_last_page()
        return self.get_current_page()

    def rotate_left(self):
        self.rotateAngle = (self.rotateAngle - 90) % 360
        return self.get_current_page()

    def rotate_right(self):
        self.rotateAngle = (self.rotateAngle + 90) % 360
        return self.get_current_page()

    def get_current_page(self):
        return self._load_pixmap_from_data()

    def set_current_page_index(self, idx):
        self.comic.set_current_page_index(idx)

    def get_current_page_index(self):
        return self.comic.current_page_index

    def _load_pixmap_from_data(self):

        page = self.comic.get_current_page()
        self.original_pixmap.loadFromData(page)

        return self.update_content()

    def update_content(self):

        pix_map = self.original_pixmap

        pix_map = self._rotate_page(pix_map)
        pix_map = self._resize_page(pix_map)

        return pix_map

    def _rotate_page(self, pix_map):

        if self.rotateAngle != 0:

            trans = QtGui.QTransform().rotate(self.rotateAngle)
            pix_map = QtGui.QPixmap(pix_map.transformed(trans))

        return pix_map

    def _resize_page(self, pix_map):

        if self.adjustType == '&Vertical Adjust':
            pix_map = pix_map.scaledToHeight(self.screenSize.height(), QtCore.Qt.SmoothTransformation)

        elif self.adjustType == '&Horizontal Adjust':
            pix_map = pix_map.scaledToWidth(self.screenSize.width(), QtCore.Qt.SmoothTransformation)

        elif self.adjustType == '&Best Fit':
            pix_map = pix_map.scaledToWidth(self.screenSize.width() * 0.8, QtCore.Qt.SmoothTransformation)

        return pix_map

    def set_size(self, new_size):
        self.screenSize = new_size

    def set_adjust_type(self, adjust_type):
        self.adjustType = adjust_type