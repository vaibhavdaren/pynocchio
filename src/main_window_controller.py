# coding=UTF-8
#
# Copyright (C) 2015  Michell Stuttgart

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt4 import QtGui, QtCore, uic
import main_window_view
import main_window_model


class MainWindowController():
    def __init__(self):
        self.main_window_view = main_window_view.MainWindowView(self)
        self.main_window_model = main_window_model.MainWindowModel(self)

    def open(self):
        print

    def save_image(self):
        print

    def online_comics(self):
        self.main_window_view.setCentralWidget(self.web_view)
        print

    def next_page(self):
        print

    def previous_page(self):
        print

    def first_page(self):
        print

    def last_page(self):
        print

    def go_to_page(self):
        print

    def next_comic(self):
        print

    def previous_comic(self):
        print

    def rotate_left(self):
        print

    def rotate_right(self):
        print

    def fullscreen(self):
        print

    def add_bookmark(self):
        print

    def remove_bookmark(self):
        print

    def bookmark_manager(self):
        print

    def show_toolbar(self):
        print

    def show_statusbar(self):
        print

    def preference_dialog(self):
        print

    def exit(self):
        print 'saindo'

    def show(self):
        self.main_window_view.show()

    def key_press_event(self, event):
        if event.key() == QtCore.Qt.Key_F:
            self.fullscreen()
            return True
        else:
            return False

    def mouse_double_click_event(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.controller.fullscreen()
            return True
        else:
            return False
