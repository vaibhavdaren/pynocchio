# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data/ui_files/main_window_view.ui'
#
# Created: Mon May  2 03:14:40 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindowView(object):
    def setupUi(self, MainWindowView):
        MainWindowView.setObjectName("MainWindowView")
        MainWindowView.resize(1048, 561)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindowView.sizePolicy().hasHeightForWidth())
        MainWindowView.setSizePolicy(sizePolicy)
        MainWindowView.setBaseSize(QtCore.QSize(0, 3))
        MainWindowView.setFocusPolicy(QtCore.Qt.WheelFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/pynocchio_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowView.setWindowIcon(icon)
        MainWindowView.setIconSize(QtCore.QSize(22, 22))
        MainWindowView.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindowView.setAnimated(False)
        MainWindowView.setDocumentMode(False)
        MainWindowView.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindowView.setDockNestingEnabled(False)
        MainWindowView.setUnifiedTitleAndToolBarOnMac(True)
        self.central_widget = QtGui.QWidget(MainWindowView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.central_widget.setAutoFillBackground(True)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.central_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.qscroll_area_viewer = QScrollAreaViewer(self.central_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qscroll_area_viewer.sizePolicy().hasHeightForWidth())
        self.qscroll_area_viewer.setSizePolicy(sizePolicy)
        self.qscroll_area_viewer.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.qscroll_area_viewer.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.qscroll_area_viewer.setAutoFillBackground(True)
        self.qscroll_area_viewer.setStyleSheet("background-color: rgb(5, 5, 5);")
        self.qscroll_area_viewer.setFrameShape(QtGui.QFrame.HLine)
        self.qscroll_area_viewer.setFrameShadow(QtGui.QFrame.Plain)
        self.qscroll_area_viewer.setLineWidth(0)
        self.qscroll_area_viewer.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.qscroll_area_viewer.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.qscroll_area_viewer.setWidgetResizable(True)
        self.qscroll_area_viewer.setAlignment(QtCore.Qt.AlignCenter)
        self.qscroll_area_viewer.setObjectName("qscroll_area_viewer")
        self.scroll_area_widget_contents = QtGui.QWidget()
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 1048, 486))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_area_widget_contents.sizePolicy().hasHeightForWidth())
        self.scroll_area_widget_contents.setSizePolicy(sizePolicy)
        self.scroll_area_widget_contents.setAutoFillBackground(False)
        self.scroll_area_widget_contents.setObjectName("scroll_area_widget_contents")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.scroll_area_widget_contents)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.scroll_area_widget_contents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMouseTracking(False)
        self.label.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setLineWidth(0)
        self.label.setMidLineWidth(0)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setPixmap(QtGui.QPixmap(":/icons/pynocchio_icon.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setMargin(0)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.qscroll_area_viewer.setWidget(self.scroll_area_widget_contents)
        self.horizontalLayout.addWidget(self.qscroll_area_viewer)
        MainWindowView.setCentralWidget(self.central_widget)
        self.menubar = QtGui.QMenuBar(MainWindowView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setAcceptDrops(False)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menu_file = QtGui.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_recent_files = QtGui.QMenu(self.menu_file)
        self.menu_recent_files.setEnabled(True)
        self.menu_recent_files.setTearOffEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/document-open-recent.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_recent_files.setIcon(icon1)
        self.menu_recent_files.setSeparatorsCollapsible(False)
        self.menu_recent_files.setObjectName("menu_recent_files")
        self.menu_view = QtGui.QMenu(self.menubar)
        self.menu_view.setObjectName("menu_view")
        self.menu_navegation = QtGui.QMenu(self.menubar)
        self.menu_navegation.setAcceptDrops(False)
        self.menu_navegation.setTearOffEnabled(False)
        self.menu_navegation.setObjectName("menu_navegation")
        self.menu_help = QtGui.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        self.menu_settings = QtGui.QMenu(self.menubar)
        self.menu_settings.setObjectName("menu_settings")
        self.menu_bookmarks = QtGui.QMenu(self.menubar)
        self.menu_bookmarks.setTearOffEnabled(False)
        self.menu_bookmarks.setSeparatorsCollapsible(True)
        self.menu_bookmarks.setObjectName("menu_bookmarks")
        self.menu_recent_bookmarks = QtGui.QMenu(self.menu_bookmarks)
        self.menu_recent_bookmarks.setIcon(icon1)
        self.menu_recent_bookmarks.setObjectName("menu_recent_bookmarks")
        MainWindowView.setMenuBar(self.menubar)
        self.toolbar = QtGui.QToolBar(MainWindowView)
        self.toolbar.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbar.sizePolicy().hasHeightForWidth())
        self.toolbar.setSizePolicy(sizePolicy)
        self.toolbar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.toolbar.setAcceptDrops(True)
        self.toolbar.setAutoFillBackground(True)
        self.toolbar.setMovable(False)
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolbar.setFloatable(False)
        self.toolbar.setObjectName("toolbar")
        MainWindowView.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar)
        self.statusbar = StatusBar(MainWindowView)
        self.statusbar.setObjectName("statusbar")
        MainWindowView.setStatusBar(self.statusbar)
        self.action_about = QtGui.QAction(MainWindowView)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/help-info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about.setIcon(icon2)
        self.action_about.setObjectName("action_about")
        self.action_about_qt = QtGui.QAction(MainWindowView)
        self.action_about_qt.setObjectName("action_about_qt")
        self.action_exit = QtGui.QAction(MainWindowView)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/application-exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_exit.setIcon(icon3)
        self.action_exit.setObjectName("action_exit")
        self.action_next_page = QtGui.QAction(MainWindowView)
        self.action_next_page.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/go-next.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_next_page.setIcon(icon4)
        self.action_next_page.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_next_page.setVisible(True)
        self.action_next_page.setPriority(QtGui.QAction.HighPriority)
        self.action_next_page.setObjectName("action_next_page")
        self.action_previous_page = QtGui.QAction(MainWindowView)
        self.action_previous_page.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/go-previous.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_previous_page.setIcon(icon5)
        self.action_previous_page.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_previous_page.setVisible(True)
        self.action_previous_page.setObjectName("action_previous_page")
        self.action_first_page = QtGui.QAction(MainWindowView)
        self.action_first_page.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/go-first.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_first_page.setIcon(icon6)
        self.action_first_page.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_first_page.setObjectName("action_first_page")
        self.action_last_page = QtGui.QAction(MainWindowView)
        self.action_last_page.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/go-last.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_last_page.setIcon(icon7)
        self.action_last_page.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_last_page.setObjectName("action_last_page")
        self.action_rotate_left = QtGui.QAction(MainWindowView)
        self.action_rotate_left.setCheckable(False)
        self.action_rotate_left.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/object-rotate-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_rotate_left.setIcon(icon8)
        self.action_rotate_left.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.action_rotate_left.setObjectName("action_rotate_left")
        self.action_rotate_right = QtGui.QAction(MainWindowView)
        self.action_rotate_right.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/object-rotate-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_rotate_right.setIcon(icon9)
        self.action_rotate_right.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.action_rotate_right.setObjectName("action_rotate_right")
        self.action_horizontal_fit = QtGui.QAction(MainWindowView)
        self.action_horizontal_fit.setCheckable(True)
        self.action_horizontal_fit.setChecked(False)
        self.action_horizontal_fit.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/freeiconmaker-icons/horizontal-fit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_horizontal_fit.setIcon(icon10)
        self.action_horizontal_fit.setVisible(True)
        self.action_horizontal_fit.setObjectName("action_horizontal_fit")
        self.action_fullscreen = QtGui.QAction(MainWindowView)
        self.action_fullscreen.setCheckable(False)
        self.action_fullscreen.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/freeiconmaker-icons/fullscreen.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_fullscreen.setIcon(icon11)
        self.action_fullscreen.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.action_fullscreen.setObjectName("action_fullscreen")
        self.action_go_to_page = QtGui.QAction(MainWindowView)
        self.action_go_to_page.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_go_to_page.setIcon(icon12)
        self.action_go_to_page.setObjectName("action_go_to_page")
        self.action_original_fit = QtGui.QAction(MainWindowView)
        self.action_original_fit.setCheckable(True)
        self.action_original_fit.setChecked(True)
        self.action_original_fit.setEnabled(False)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/freeiconmaker-icons/original-fit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_original_fit.setIcon(icon13)
        self.action_original_fit.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.action_original_fit.setVisible(True)
        self.action_original_fit.setObjectName("action_original_fit")
        self.action_show_statusbar = QtGui.QAction(MainWindowView)
        self.action_show_statusbar.setCheckable(True)
        self.action_show_statusbar.setChecked(True)
        self.action_show_statusbar.setObjectName("action_show_statusbar")
        self.action_add_bookmark = QtGui.QAction(MainWindowView)
        self.action_add_bookmark.setEnabled(False)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/bookmark-new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_add_bookmark.setIcon(icon14)
        self.action_add_bookmark.setVisible(True)
        self.action_add_bookmark.setObjectName("action_add_bookmark")
        self.action_remove_bookmark = QtGui.QAction(MainWindowView)
        self.action_remove_bookmark.setEnabled(False)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/stock_delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_remove_bookmark.setIcon(icon15)
        self.action_remove_bookmark.setVisible(False)
        self.action_remove_bookmark.setIconVisibleInMenu(True)
        self.action_remove_bookmark.setObjectName("action_remove_bookmark")
        self.action_bookmark_manager = QtGui.QAction(MainWindowView)
        self.action_bookmark_manager.setEnabled(True)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/apps/48/office-database.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_bookmark_manager.setIcon(icon16)
        self.action_bookmark_manager.setObjectName("action_bookmark_manager")
        self.action_open_folder = QtGui.QAction(MainWindowView)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/document-open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open_folder.setIcon(icon17)
        self.action_open_folder.setVisible(False)
        self.action_open_folder.setMenuRole(QtGui.QAction.TextHeuristicRole)
        self.action_open_folder.setIconVisibleInMenu(True)
        self.action_open_folder.setObjectName("action_open_folder")
        self.action_next_comic = QtGui.QAction(MainWindowView)
        self.action_next_comic.setEnabled(False)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/media-skip-forward.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_next_comic.setIcon(icon18)
        self.action_next_comic.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_next_comic.setObjectName("action_next_comic")
        self.action_previous_comic = QtGui.QAction(MainWindowView)
        self.action_previous_comic.setEnabled(False)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/media-skip-backward.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_previous_comic.setIcon(icon19)
        self.action_previous_comic.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.action_previous_comic.setObjectName("action_previous_comic")
        self.action_preference_dialog = QtGui.QAction(MainWindowView)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/document-properties.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_preference_dialog.setIcon(icon20)
        self.action_preference_dialog.setVisible(False)
        self.action_preference_dialog.setObjectName("action_preference_dialog")
        self.action_vertical_fit = QtGui.QAction(MainWindowView)
        self.action_vertical_fit.setCheckable(True)
        self.action_vertical_fit.setChecked(False)
        self.action_vertical_fit.setEnabled(False)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/icons/freeiconmaker-icons/vertical-fit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_vertical_fit.setIcon(icon21)
        self.action_vertical_fit.setAutoRepeat(True)
        self.action_vertical_fit.setVisible(True)
        self.action_vertical_fit.setObjectName("action_vertical_fit")
        self.action_best_fit = QtGui.QAction(MainWindowView)
        self.action_best_fit.setCheckable(True)
        self.action_best_fit.setChecked(False)
        self.action_best_fit.setEnabled(False)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/icons/freeiconmaker-icons/best-fit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_best_fit.setIcon(icon22)
        self.action_best_fit.setVisible(True)
        self.action_best_fit.setObjectName("action_best_fit")
        self.action_save_image = QtGui.QAction(MainWindowView)
        self.action_save_image.setEnabled(True)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/go-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save_image.setIcon(icon23)
        self.action_save_image.setObjectName("action_save_image")
        self.action_open_file = QtGui.QAction(MainWindowView)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/icons/elementary3-icon-theme/actions/48/archive-extract.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_open_file.setIcon(icon24)
        font = QtGui.QFont()
        self.action_open_file.setFont(font)
        self.action_open_file.setObjectName("action_open_file")
        self.actionRecent_file_1 = QtGui.QAction(MainWindowView)
        self.actionRecent_file_1.setVisible(False)
        self.actionRecent_file_1.setObjectName("actionRecent_file_1")
        self.actionRecent_file_2 = QtGui.QAction(MainWindowView)
        self.actionRecent_file_2.setVisible(False)
        self.actionRecent_file_2.setObjectName("actionRecent_file_2")
        self.actionRecent_file_3 = QtGui.QAction(MainWindowView)
        self.actionRecent_file_3.setVisible(False)
        self.actionRecent_file_3.setObjectName("actionRecent_file_3")
        self.actionRecent_file_4 = QtGui.QAction(MainWindowView)
        self.actionRecent_file_4.setVisible(False)
        self.actionRecent_file_4.setObjectName("actionRecent_file_4")
        self.actionRecent_file_5 = QtGui.QAction(MainWindowView)
        self.actionRecent_file_5.setVisible(False)
        self.actionRecent_file_5.setObjectName("actionRecent_file_5")
        self.actionRecent_file_6 = QtGui.QAction(MainWindowView)
        self.actionRecent_file_6.setVisible(False)
        self.actionRecent_file_6.setObjectName("actionRecent_file_6")
        self.actionRecent_file_7 = QtGui.QAction(MainWindowView)
        self.actionRecent_file_7.setVisible(False)
        self.actionRecent_file_7.setObjectName("actionRecent_file_7")
        self.actionRecent_file_8 = QtGui.QAction(MainWindowView)
        self.actionRecent_file_8.setVisible(False)
        self.actionRecent_file_8.setObjectName("actionRecent_file_8")
        self.actionRecent_file_9 = QtGui.QAction(MainWindowView)
        self.actionRecent_file_9.setVisible(False)
        self.actionRecent_file_9.setObjectName("actionRecent_file_9")
        self.actionRecent_file_10 = QtGui.QAction(MainWindowView)
        self.actionRecent_file_10.setVisible(False)
        self.actionRecent_file_10.setObjectName("actionRecent_file_10")
        self.actionRecent_bookmark_1 = QtGui.QAction(MainWindowView)
        self.actionRecent_bookmark_1.setVisible(False)
        self.actionRecent_bookmark_1.setObjectName("actionRecent_bookmark_1")
        self.actionRecent_bookmark_2 = QtGui.QAction(MainWindowView)
        self.actionRecent_bookmark_2.setVisible(False)
        self.actionRecent_bookmark_2.setObjectName("actionRecent_bookmark_2")
        self.actionRecent_bookmark_3 = QtGui.QAction(MainWindowView)
        self.actionRecent_bookmark_3.setVisible(False)
        self.actionRecent_bookmark_3.setObjectName("actionRecent_bookmark_3")
        self.actionRecent_bookmark_4 = QtGui.QAction(MainWindowView)
        self.actionRecent_bookmark_4.setVisible(False)
        self.actionRecent_bookmark_4.setObjectName("actionRecent_bookmark_4")
        self.actionRecent_bookmark_5 = QtGui.QAction(MainWindowView)
        self.actionRecent_bookmark_5.setVisible(False)
        self.actionRecent_bookmark_5.setObjectName("actionRecent_bookmark_5")
        self.action_en_us = QtGui.QAction(MainWindowView)
        self.action_en_us.setCheckable(True)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/icons/famfamfam_flag_icons/png/us.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_en_us.setIcon(icon25)
        self.action_en_us.setObjectName("action_en_us")
        self.action_pt_br = QtGui.QAction(MainWindowView)
        self.action_pt_br.setCheckable(True)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/icons/famfamfam_flag_icons/png/br.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_pt_br.setIcon(icon26)
        self.action_pt_br.setIconText("pt_BR")
        self.action_pt_br.setObjectName("action_pt_br")
        self.action_show_toolbar = QtGui.QAction(MainWindowView)
        self.action_show_toolbar.setCheckable(True)
        self.action_show_toolbar.setChecked(True)
        self.action_show_toolbar.setObjectName("action_show_toolbar")
        self.menu_recent_files.addAction(self.actionRecent_file_1)
        self.menu_recent_files.addAction(self.actionRecent_file_2)
        self.menu_recent_files.addAction(self.actionRecent_file_3)
        self.menu_recent_files.addAction(self.actionRecent_file_4)
        self.menu_recent_files.addAction(self.actionRecent_file_5)
        self.menu_recent_files.addAction(self.actionRecent_file_6)
        self.menu_recent_files.addAction(self.actionRecent_file_7)
        self.menu_recent_files.addAction(self.actionRecent_file_8)
        self.menu_recent_files.addAction(self.actionRecent_file_9)
        self.menu_recent_files.addAction(self.actionRecent_file_10)
        self.menu_file.addAction(self.action_open_file)
        self.menu_file.addAction(self.action_open_folder)
        self.menu_file.addAction(self.menu_recent_files.menuAction())
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_save_image)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_view.addAction(self.action_fullscreen)
        self.menu_view.addSeparator()
        self.menu_view.addAction(self.action_original_fit)
        self.menu_view.addAction(self.action_vertical_fit)
        self.menu_view.addAction(self.action_horizontal_fit)
        self.menu_view.addAction(self.action_best_fit)
        self.menu_view.addSeparator()
        self.menu_view.addAction(self.action_rotate_left)
        self.menu_view.addAction(self.action_rotate_right)
        self.menu_navegation.addAction(self.action_next_page)
        self.menu_navegation.addAction(self.action_previous_page)
        self.menu_navegation.addSeparator()
        self.menu_navegation.addAction(self.action_first_page)
        self.menu_navegation.addAction(self.action_last_page)
        self.menu_navegation.addSeparator()
        self.menu_navegation.addAction(self.action_go_to_page)
        self.menu_navegation.addSeparator()
        self.menu_navegation.addAction(self.action_next_comic)
        self.menu_navegation.addAction(self.action_previous_comic)
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.action_about_qt)
        self.menu_settings.addAction(self.action_show_toolbar)
        self.menu_settings.addAction(self.action_show_statusbar)
        self.menu_settings.addSeparator()
        self.menu_settings.addAction(self.action_preference_dialog)
        self.menu_recent_bookmarks.addAction(self.actionRecent_bookmark_1)
        self.menu_recent_bookmarks.addAction(self.actionRecent_bookmark_2)
        self.menu_recent_bookmarks.addAction(self.actionRecent_bookmark_3)
        self.menu_recent_bookmarks.addAction(self.actionRecent_bookmark_4)
        self.menu_recent_bookmarks.addAction(self.actionRecent_bookmark_5)
        self.menu_bookmarks.addAction(self.action_add_bookmark)
        self.menu_bookmarks.addAction(self.action_remove_bookmark)
        self.menu_bookmarks.addSeparator()
        self.menu_bookmarks.addAction(self.action_bookmark_manager)
        self.menu_bookmarks.addAction(self.menu_recent_bookmarks.menuAction())
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_navegation.menuAction())
        self.menubar.addAction(self.menu_bookmarks.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.toolbar.addAction(self.action_open_file)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_previous_comic)
        self.toolbar.addAction(self.action_first_page)
        self.toolbar.addAction(self.action_previous_page)
        self.toolbar.addAction(self.action_next_page)
        self.toolbar.addAction(self.action_last_page)
        self.toolbar.addAction(self.action_next_comic)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_go_to_page)
        self.toolbar.addAction(self.action_add_bookmark)
        self.toolbar.addAction(self.action_remove_bookmark)
        self.toolbar.addAction(self.action_bookmark_manager)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_rotate_left)
        self.toolbar.addAction(self.action_rotate_right)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_original_fit)
        self.toolbar.addAction(self.action_vertical_fit)
        self.toolbar.addAction(self.action_horizontal_fit)
        self.toolbar.addAction(self.action_best_fit)
        self.toolbar.addAction(self.action_fullscreen)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.action_exit)

        self.retranslateUi(MainWindowView)
        QtCore.QMetaObject.connectSlotsByName(MainWindowView)

    def retranslateUi(self, MainWindowView):
        MainWindowView.setWindowTitle(QtGui.QApplication.translate("MainWindowView", "Pynocchio Comic Reader", None, QtGui.QApplication.UnicodeUTF8))
        MainWindowView.setAccessibleName(QtGui.QApplication.translate("MainWindowView", "Pynocchio Comic Reader", None, QtGui.QApplication.UnicodeUTF8))
        MainWindowView.setAccessibleDescription(QtGui.QApplication.translate("MainWindowView", "The Best Comic Reader", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_file.setTitle(QtGui.QApplication.translate("MainWindowView", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_recent_files.setTitle(QtGui.QApplication.translate("MainWindowView", "Recent files", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_view.setTitle(QtGui.QApplication.translate("MainWindowView", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_navegation.setTitle(QtGui.QApplication.translate("MainWindowView", "&Navegation", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_help.setTitle(QtGui.QApplication.translate("MainWindowView", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_settings.setTitle(QtGui.QApplication.translate("MainWindowView", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_bookmarks.setTitle(QtGui.QApplication.translate("MainWindowView", "&Bookmarks", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_recent_bookmarks.setTitle(QtGui.QApplication.translate("MainWindowView", "Recente bookmarks", None, QtGui.QApplication.UnicodeUTF8))
        self.toolbar.setWindowTitle(QtGui.QApplication.translate("MainWindowView", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_about.setText(QtGui.QApplication.translate("MainWindowView", "About Pynocchio", None, QtGui.QApplication.UnicodeUTF8))
        self.action_about_qt.setText(QtGui.QApplication.translate("MainWindowView", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exit.setText(QtGui.QApplication.translate("MainWindowView", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exit.setShortcut(QtGui.QApplication.translate("MainWindowView", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_next_page.setText(QtGui.QApplication.translate("MainWindowView", "Next page", None, QtGui.QApplication.UnicodeUTF8))
        self.action_next_page.setShortcut(QtGui.QApplication.translate("MainWindowView", "Right", None, QtGui.QApplication.UnicodeUTF8))
        self.action_previous_page.setText(QtGui.QApplication.translate("MainWindowView", "Previous page", None, QtGui.QApplication.UnicodeUTF8))
        self.action_previous_page.setShortcut(QtGui.QApplication.translate("MainWindowView", "Left", None, QtGui.QApplication.UnicodeUTF8))
        self.action_first_page.setText(QtGui.QApplication.translate("MainWindowView", "First page", None, QtGui.QApplication.UnicodeUTF8))
        self.action_first_page.setShortcut(QtGui.QApplication.translate("MainWindowView", "Ctrl+Left", None, QtGui.QApplication.UnicodeUTF8))
        self.action_last_page.setText(QtGui.QApplication.translate("MainWindowView", "Last page", None, QtGui.QApplication.UnicodeUTF8))
        self.action_last_page.setShortcut(QtGui.QApplication.translate("MainWindowView", "Ctrl+Right", None, QtGui.QApplication.UnicodeUTF8))
        self.action_rotate_left.setText(QtGui.QApplication.translate("MainWindowView", "Rotate left", None, QtGui.QApplication.UnicodeUTF8))
        self.action_rotate_left.setShortcut(QtGui.QApplication.translate("MainWindowView", "Ctrl+Shift+R", None, QtGui.QApplication.UnicodeUTF8))
        self.action_rotate_right.setText(QtGui.QApplication.translate("MainWindowView", "Rotate right", None, QtGui.QApplication.UnicodeUTF8))
        self.action_rotate_right.setShortcut(QtGui.QApplication.translate("MainWindowView", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.action_horizontal_fit.setText(QtGui.QApplication.translate("MainWindowView", "Horizontal fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_horizontal_fit.setShortcut(QtGui.QApplication.translate("MainWindowView", "Ctrl+K", None, QtGui.QApplication.UnicodeUTF8))
        self.action_fullscreen.setText(QtGui.QApplication.translate("MainWindowView", "Fullscreen", None, QtGui.QApplication.UnicodeUTF8))
        self.action_fullscreen.setShortcut(QtGui.QApplication.translate("MainWindowView", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.action_go_to_page.setText(QtGui.QApplication.translate("MainWindowView", "Go to page", None, QtGui.QApplication.UnicodeUTF8))
        self.action_go_to_page.setShortcut(QtGui.QApplication.translate("MainWindowView", "Ctrl+G", None, QtGui.QApplication.UnicodeUTF8))
        self.action_original_fit.setText(QtGui.QApplication.translate("MainWindowView", "Original fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_original_fit.setShortcut(QtGui.QApplication.translate("MainWindowView", "Ctrl+H", None, QtGui.QApplication.UnicodeUTF8))
        self.action_show_statusbar.setText(QtGui.QApplication.translate("MainWindowView", "Show Statusbar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_add_bookmark.setText(QtGui.QApplication.translate("MainWindowView", "Add bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.action_remove_bookmark.setText(QtGui.QApplication.translate("MainWindowView", "Remove bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.action_bookmark_manager.setText(QtGui.QApplication.translate("MainWindowView", "Bookmark manager", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open_folder.setText(QtGui.QApplication.translate("MainWindowView", "Open Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.action_next_comic.setText(QtGui.QApplication.translate("MainWindowView", "Next Comic", None, QtGui.QApplication.UnicodeUTF8))
        self.action_next_comic.setShortcut(QtGui.QApplication.translate("MainWindowView", "Ctrl+Shift+Right", None, QtGui.QApplication.UnicodeUTF8))
        self.action_previous_comic.setText(QtGui.QApplication.translate("MainWindowView", "Previous Comic", None, QtGui.QApplication.UnicodeUTF8))
        self.action_previous_comic.setShortcut(QtGui.QApplication.translate("MainWindowView", "Ctrl+Shift+Left", None, QtGui.QApplication.UnicodeUTF8))
        self.action_preference_dialog.setText(QtGui.QApplication.translate("MainWindowView", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.action_vertical_fit.setText(QtGui.QApplication.translate("MainWindowView", "Vertical fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_vertical_fit.setShortcut(QtGui.QApplication.translate("MainWindowView", "Ctrl+J", None, QtGui.QApplication.UnicodeUTF8))
        self.action_best_fit.setText(QtGui.QApplication.translate("MainWindowView", "Best fit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_best_fit.setShortcut(QtGui.QApplication.translate("MainWindowView", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save_image.setText(QtGui.QApplication.translate("MainWindowView", "Save image", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save_image.setWhatsThis(QtGui.QApplication.translate("MainWindowView", "Save current image in disk.", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save_image.setShortcut(QtGui.QApplication.translate("MainWindowView", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open_file.setText(QtGui.QApplication.translate("MainWindowView", "Open File", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open_file.setShortcut(QtGui.QApplication.translate("MainWindowView", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_file_1.setText(QtGui.QApplication.translate("MainWindowView", "recent_file_1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_file_2.setText(QtGui.QApplication.translate("MainWindowView", "recent_file_2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_file_3.setText(QtGui.QApplication.translate("MainWindowView", "recent_file_3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_file_4.setText(QtGui.QApplication.translate("MainWindowView", "recent_file_4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_file_5.setText(QtGui.QApplication.translate("MainWindowView", "recent_file_5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_file_6.setText(QtGui.QApplication.translate("MainWindowView", "recent_file_6", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_file_7.setText(QtGui.QApplication.translate("MainWindowView", "recent_file_7", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_file_8.setText(QtGui.QApplication.translate("MainWindowView", "recent_file_8", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_file_9.setText(QtGui.QApplication.translate("MainWindowView", "recent_file_9", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_file_10.setText(QtGui.QApplication.translate("MainWindowView", "recent_file_10", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_bookmark_1.setText(QtGui.QApplication.translate("MainWindowView", "recent_bookmark_1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_bookmark_2.setText(QtGui.QApplication.translate("MainWindowView", "recent_bookmark_2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_bookmark_3.setText(QtGui.QApplication.translate("MainWindowView", "recent_bookmark_3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_bookmark_4.setText(QtGui.QApplication.translate("MainWindowView", "recent_bookmark_4", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_bookmark_5.setText(QtGui.QApplication.translate("MainWindowView", "recent_bookmark_5", None, QtGui.QApplication.UnicodeUTF8))
        self.action_en_us.setText(QtGui.QApplication.translate("MainWindowView", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.action_en_us.setIconText(QtGui.QApplication.translate("MainWindowView", "en_US", None, QtGui.QApplication.UnicodeUTF8))
        self.action_pt_br.setText(QtGui.QApplication.translate("MainWindowView", "Portuguese", None, QtGui.QApplication.UnicodeUTF8))
        self.action_show_toolbar.setText(QtGui.QApplication.translate("MainWindowView", "Show Toolbar", None, QtGui.QApplication.UnicodeUTF8))

from custom_widgets.qscroll_area_viewer import QScrollAreaViewer
from custom_widgets.status_bar import StatusBar
import main_window_view_rc
import main_window_view_rc
import main_window_view_rc
