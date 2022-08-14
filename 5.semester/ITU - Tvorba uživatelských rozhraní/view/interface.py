# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainArTvMA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(783, 602)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border:none;")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left = QFrame(self.header_frame)
        self.header_left.setObjectName(u"header_left")
        self.header_left.setFrameShape(QFrame.StyledPanel)
        self.header_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, 0, 0, 0)
        self.menu_button = QPushButton(self.header_left)
        self.menu_button.setObjectName(u"menu_button")
        font = QFont()
        font.setFamily(u"Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.menu_button.setFont(font)
        self.menu_button.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 5px;\n"
"	border: 1px solid White;\n"
"	background-color: #00aaff;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/prefix/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_button.setIcon(icon)
        self.menu_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.menu_button)


        self.horizontalLayout.addWidget(self.header_left, 0, Qt.AlignLeft)

        self.header_center = QFrame(self.header_frame)
        self.header_center.setObjectName(u"header_center")
        self.header_center.setMaximumSize(QSize(266, 200))
        self.header_center.setFrameShape(QFrame.StyledPanel)
        self.header_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.header_center)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(20, 20))
        self.label.setPixmap(QPixmap(u":/prefix/icons/hammer.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.header_center)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Nirmala UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.header_center, 0, Qt.AlignHCenter)

        self.header_right = QFrame(self.header_frame)
        self.header_right.setObjectName(u"header_right")
        self.header_right.setFrameShape(QFrame.StyledPanel)
        self.header_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 3, 0)
        self.minimze_window_button = QPushButton(self.header_right)
        self.minimze_window_button.setObjectName(u"minimze_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/prefix/icons/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimze_window_button.setIcon(icon1)
        self.minimze_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.minimze_window_button)

        self.resize_window_button = QPushButton(self.header_right)
        self.resize_window_button.setObjectName(u"resize_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/prefix/icons/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resize_window_button.setIcon(icon2)
        self.resize_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.resize_window_button)

        self.close_window_button = QPushButton(self.header_right)
        self.close_window_button.setObjectName(u"close_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/prefix/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon3)
        self.close_window_button.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.close_window_button)


        self.horizontalLayout.addWidget(self.header_right, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.left_menu_frame = QFrame(self.main_body_frame)
        self.left_menu_frame.setObjectName(u"left_menu_frame")
        self.left_menu_frame.setMinimumSize(QSize(40, 0))
        self.left_menu_frame.setMaximumSize(QSize(40, 16777215))
        self.left_menu_frame.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border:none;")
        self.left_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.left_menu_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(200, 0))
        self.menu_frame.setStyleSheet(u"margin-left: 2px;")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.stats_button = QPushButton(self.menu_frame)
        self.stats_button.setObjectName(u"stats_button")
        font2 = QFont()
        font2.setFamily(u"Nirmala UI")
        font2.setPointSize(10)
        self.stats_button.setFont(font2)
        self.stats_button.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 5px;\n"
"	border: 1px solid White;\n"
"	background-color: #00aaff;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/prefix/icons/analytics.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stats_button.setIcon(icon4)
        self.stats_button.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.stats_button, 3, 0, 1, 1, Qt.AlignLeft)

        self.machines_button = QPushButton(self.menu_frame)
        self.machines_button.setObjectName(u"machines_button")
        self.machines_button.setFont(font2)
        self.machines_button.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 5px;\n"
"	border: 1px solid White;\n"
"	background-color: #00aaff;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/prefix/icons/hardware-chip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.machines_button.setIcon(icon5)
        self.machines_button.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.machines_button, 2, 0, 1, 1, Qt.AlignLeft)

        self.settings_button = QPushButton(self.menu_frame)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setFont(font2)
        self.settings_button.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 5px;\n"
"	border: 1px solid White;\n"
"	background-color: #00aaff;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/prefix/icons/construct.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon6)
        self.settings_button.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.settings_button, 4, 0, 1, 1, Qt.AlignLeft)

        self.home_button = QPushButton(self.menu_frame)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setFont(font)
        self.home_button.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 5px;\n"
"	border: 1px solid White;\n"
"	background-color: #00aaff;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/prefix/icons/cube.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon7)
        self.home_button.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.home_button, 0, 0, 1, 1, Qt.AlignLeft)

        self.halls_button = QPushButton(self.menu_frame)
        self.halls_button.setObjectName(u"halls_button")
        self.halls_button.setFont(font2)
        self.halls_button.setStyleSheet(u"QPushButton:hover{\n"
"	border-radius: 5px;\n"
"	border: 1px solid White;\n"
"	background-color: #00aaff;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/prefix/icons/factory.png", QSize(), QIcon.Normal, QIcon.Off)
        self.halls_button.setIcon(icon8)
        self.halls_button.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.halls_button, 1, 0, 1, 1, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.left_menu_frame)

        self.main_body_content = QFrame(self.main_body_frame)
        self.main_body_content.setObjectName(u"main_body_content")
        self.main_body_content.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.main_body_content.setFrameShape(QFrame.StyledPanel)
        self.main_body_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_body_content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_body_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.main_menu_page = QWidget()
        self.main_menu_page.setObjectName(u"main_menu_page")
        self.verticalLayout_10 = QVBoxLayout(self.main_menu_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.main_menu_label = QFrame(self.main_menu_page)
        self.main_menu_label.setObjectName(u"main_menu_label")
        self.main_menu_label.setMaximumSize(QSize(16777215, 60))
        self.main_menu_label.setFrameShape(QFrame.StyledPanel)
        self.main_menu_label.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.main_menu_label)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_27 = QLabel(self.main_menu_label)
        self.label_27.setObjectName(u"label_27")
        font3 = QFont()
        font3.setFamily(u"Nirmala UI")
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_27.setFont(font3)
        self.label_27.setLayoutDirection(Qt.LeftToRight)
        self.label_27.setAutoFillBackground(False)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_27)


        self.verticalLayout_10.addWidget(self.main_menu_label)

        self.main_menu_buttons_frame = QFrame(self.main_menu_page)
        self.main_menu_buttons_frame.setObjectName(u"main_menu_buttons_frame")
        self.main_menu_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.main_menu_buttons_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.main_menu_buttons_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.main_menu_machines_button = QPushButton(self.main_menu_buttons_frame)
        self.main_menu_machines_button.setObjectName(u"main_menu_machines_button")
        self.main_menu_machines_button.setMinimumSize(QSize(0, 50))
        self.main_menu_machines_button.setFont(font1)
        self.main_menu_machines_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(80, 170, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00aaff;\n"
"}")
        self.main_menu_machines_button.setIcon(icon5)
        self.main_menu_machines_button.setIconSize(QSize(32, 32))

        self.gridLayout_6.addWidget(self.main_menu_machines_button, 1, 1, 1, 1)

        self.main_menu_stats_button = QPushButton(self.main_menu_buttons_frame)
        self.main_menu_stats_button.setObjectName(u"main_menu_stats_button")
        self.main_menu_stats_button.setMinimumSize(QSize(0, 50))
        self.main_menu_stats_button.setFont(font1)
        self.main_menu_stats_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(80, 170, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00aaff;\n"
"}")
        self.main_menu_stats_button.setIcon(icon4)
        self.main_menu_stats_button.setIconSize(QSize(32, 32))

        self.gridLayout_6.addWidget(self.main_menu_stats_button, 3, 0, 1, 1)

        self.main_menu_settings_button = QPushButton(self.main_menu_buttons_frame)
        self.main_menu_settings_button.setObjectName(u"main_menu_settings_button")
        self.main_menu_settings_button.setMinimumSize(QSize(0, 50))
        self.main_menu_settings_button.setFont(font1)
        self.main_menu_settings_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(80, 170, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00aaff;\n"
"}")
        self.main_menu_settings_button.setIcon(icon6)
        self.main_menu_settings_button.setIconSize(QSize(32, 32))

        self.gridLayout_6.addWidget(self.main_menu_settings_button, 3, 1, 1, 1)

        self.main_menu_halls_button = QPushButton(self.main_menu_buttons_frame)
        self.main_menu_halls_button.setObjectName(u"main_menu_halls_button")
        self.main_menu_halls_button.setMinimumSize(QSize(0, 50))
        self.main_menu_halls_button.setFont(font1)
        self.main_menu_halls_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(80, 170, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00aaff;\n"
"}")
        self.main_menu_halls_button.setIcon(icon8)
        self.main_menu_halls_button.setIconSize(QSize(32, 32))

        self.gridLayout_6.addWidget(self.main_menu_halls_button, 1, 0, 1, 1)

        self.spacer = QFrame(self.main_menu_buttons_frame)
        self.spacer.setObjectName(u"spacer")
        self.spacer.setMinimumSize(QSize(0, 20))
        self.spacer.setFrameShape(QFrame.StyledPanel)
        self.spacer.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.spacer, 0, 0, 1, 1)

        self.spacer2 = QFrame(self.main_menu_buttons_frame)
        self.spacer2.setObjectName(u"spacer2")
        self.spacer2.setFrameShape(QFrame.StyledPanel)
        self.spacer2.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.spacer2, 2, 0, 1, 1)


        self.verticalLayout_10.addWidget(self.main_menu_buttons_frame, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.main_menu_page)
        self.halls_list_page = QWidget()
        self.halls_list_page.setObjectName(u"halls_list_page")
        self.verticalLayout_6 = QVBoxLayout(self.halls_list_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.halls_list_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.halls_label = QLabel(self.frame)
        self.halls_label.setObjectName(u"halls_label")
        font4 = QFont()
        font4.setFamily(u"Nirmala UI")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.halls_label.setFont(font4)

        self.horizontalLayout_10.addWidget(self.halls_label)

        self.add_hall_button = QPushButton(self.frame)
        self.add_hall_button.setObjectName(u"add_hall_button")
        self.add_hall_button.setMinimumSize(QSize(0, 25))
        self.add_hall_button.setMaximumSize(QSize(90, 16777215))
        font5 = QFont()
        font5.setFamily(u"Nirmala UI")
        font5.setBold(True)
        font5.setWeight(75)
        self.add_hall_button.setFont(font5)
        self.add_hall_button.setAutoFillBackground(False)
        self.add_hall_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(80, 170, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00aaff;\n"
"}")

        self.horizontalLayout_10.addWidget(self.add_hall_button)

        self.search_bar_2 = QLineEdit(self.frame)
        self.search_bar_2.setObjectName(u"search_bar_2")
        self.search_bar_2.setMaximumSize(QSize(200, 16777215))
        self.search_bar_2.setStyleSheet(u"border-color: rgb(0, 0, 0);")

        self.horizontalLayout_10.addWidget(self.search_bar_2)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_4 = QFrame(self.halls_list_page)
        self.frame_4.setObjectName(u"frame_4")
        font6 = QFont()
        font6.setFamily(u"Palace Script MT")
        self.frame_4.setFont(font6)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.halls_table = QTableWidget(self.frame_4)
        if (self.halls_table.columnCount() < 4):
            self.halls_table.setColumnCount(4)
        font7 = QFont()
        font7.setBold(True)
        font7.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font7);
        self.halls_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font7);
        self.halls_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font7);
        self.halls_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font7);
        self.halls_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.halls_table.setObjectName(u"halls_table")
        self.halls_table.setGeometry(QRect(15, 11, 681, 371))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(9)
        self.halls_table.setFont(font8)

        self.verticalLayout_6.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.halls_list_page)
        self.add_hall_form = QWidget()
        self.add_hall_form.setObjectName(u"add_hall_form")
        self.verticalLayout_3 = QVBoxLayout(self.add_hall_form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.top_add_hall_form = QFrame(self.add_hall_form)
        self.top_add_hall_form.setObjectName(u"top_add_hall_form")
        self.top_add_hall_form.setMaximumSize(QSize(16777215, 50))
        self.top_add_hall_form.setFrameShape(QFrame.StyledPanel)
        self.top_add_hall_form.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.top_add_hall_form)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_8 = QLabel(self.top_add_hall_form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)

        self.horizontalLayout_11.addWidget(self.label_8)

        self.add_hall_back_button = QPushButton(self.top_add_hall_form)
        self.add_hall_back_button.setObjectName(u"add_hall_back_button")
        self.add_hall_back_button.setMaximumSize(QSize(80, 30))
        font9 = QFont()
        font9.setFamily(u"Nirmala UI")
        font9.setPointSize(8)
        font9.setBold(True)
        font9.setWeight(75)
        self.add_hall_back_button.setFont(font9)
        self.add_hall_back_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(80, 170, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00aaff;\n"
"}")

        self.horizontalLayout_11.addWidget(self.add_hall_back_button)


        self.verticalLayout_3.addWidget(self.top_add_hall_form)

        self.form_frame_add_hall = QFrame(self.add_hall_form)
        self.form_frame_add_hall.setObjectName(u"form_frame_add_hall")
        self.form_frame_add_hall.setFrameShape(QFrame.StyledPanel)
        self.form_frame_add_hall.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.form_frame_add_hall)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_10 = QLabel(self.form_frame_add_hall)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.add_hall_name = QLineEdit(self.form_frame_add_hall)
        self.add_hall_name.setObjectName(u"add_hall_name")
        self.add_hall_name.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(247, 247, 247);\n"
"	border: 2px solid #55aaff;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid #00ffff;\n"
"}")

        self.gridLayout_2.addWidget(self.add_hall_name, 0, 1, 1, 1)

        self.label_9 = QLabel(self.form_frame_add_hall)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1, Qt.AlignTop)

        self.label_11 = QLabel(self.form_frame_add_hall)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_12 = QLabel(self.form_frame_add_hall)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.gridLayout_2.addWidget(self.label_12, 4, 0, 1, 1)

        self.add_hall_street = QLineEdit(self.form_frame_add_hall)
        self.add_hall_street.setObjectName(u"add_hall_street")
        self.add_hall_street.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(247, 247, 247);\n"
"	border: 2px solid #55aaff;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid #00ffff;\n"
"}")

        self.gridLayout_2.addWidget(self.add_hall_street, 4, 1, 1, 1)

        self.add_hall_id = QLineEdit(self.form_frame_add_hall)
        self.add_hall_id.setObjectName(u"add_hall_id")
        self.add_hall_id.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(247, 247, 247);\n"
"	border: 2px solid #55aaff;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid #00ffff;\n"
"}")

        self.gridLayout_2.addWidget(self.add_hall_id, 1, 1, 1, 1)

        self.add_hall_city = QLineEdit(self.form_frame_add_hall)
        self.add_hall_city.setObjectName(u"add_hall_city")
        self.add_hall_city.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(247, 247, 247);\n"
"	border: 2px solid #55aaff;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid #00ffff;\n"
"}")

        self.gridLayout_2.addWidget(self.add_hall_city, 2, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.form_frame_add_hall)

        self.confirm_button_add_hall = QFrame(self.add_hall_form)
        self.confirm_button_add_hall.setObjectName(u"confirm_button_add_hall")
        self.confirm_button_add_hall.setMaximumSize(QSize(16777215, 40))
        self.confirm_button_add_hall.setFrameShape(QFrame.StyledPanel)
        self.confirm_button_add_hall.setFrameShadow(QFrame.Raised)
        self.confirm_add_button = QPushButton(self.confirm_button_add_hall)
        self.confirm_add_button.setObjectName(u"confirm_add_button")
        self.confirm_add_button.setGeometry(QRect(610, 10, 93, 28))
        self.confirm_add_button.setFont(font5)
        self.confirm_add_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(80, 170, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00aaff;\n"
"}")

        self.verticalLayout_3.addWidget(self.confirm_button_add_hall)

        self.stackedWidget.addWidget(self.add_hall_form)
        self.machines_list_page = QWidget()
        self.machines_list_page.setObjectName(u"machines_list_page")
        self.verticalLayout_5 = QVBoxLayout(self.machines_list_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.top_bar_machines = QFrame(self.machines_list_page)
        self.top_bar_machines.setObjectName(u"top_bar_machines")
        self.top_bar_machines.setMaximumSize(QSize(16777215, 50))
        self.top_bar_machines.setFrameShape(QFrame.StyledPanel)
        self.top_bar_machines.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.top_bar_machines)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.machines_label = QLabel(self.top_bar_machines)
        self.machines_label.setObjectName(u"machines_label")
        self.machines_label.setFont(font4)

        self.horizontalLayout_12.addWidget(self.machines_label)

        self.add_machine_button = QPushButton(self.top_bar_machines)
        self.add_machine_button.setObjectName(u"add_machine_button")
        self.add_machine_button.setMinimumSize(QSize(0, 25))
        self.add_machine_button.setMaximumSize(QSize(120, 16777215))
        self.add_machine_button.setFont(font5)
        self.add_machine_button.setAutoFillBackground(False)
        self.add_machine_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(80, 170, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00aaff;\n"
"}")

        self.horizontalLayout_12.addWidget(self.add_machine_button)

        self.search_bar_3 = QLineEdit(self.top_bar_machines)
        self.search_bar_3.setObjectName(u"search_bar_3")
        self.search_bar_3.setMaximumSize(QSize(200, 16777215))
        self.search_bar_3.setStyleSheet(u"border-color: rgb(0, 0, 0);")

        self.horizontalLayout_12.addWidget(self.search_bar_3)


        self.verticalLayout_5.addWidget(self.top_bar_machines)

        self.machines_table = QTableWidget(self.machines_list_page)
        if (self.machines_table.columnCount() < 5):
            self.machines_table.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font7);
        self.machines_table.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font7);
        self.machines_table.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font7);
        self.machines_table.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font7);
        self.machines_table.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font7);
        self.machines_table.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.machines_table.setObjectName(u"machines_table")

        self.verticalLayout_5.addWidget(self.machines_table)

        self.stackedWidget.addWidget(self.machines_list_page)
        self.add_machine_form = QWidget()
        self.add_machine_form.setObjectName(u"add_machine_form")
        self.verticalLayout_4 = QVBoxLayout(self.add_machine_form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.top_add_hall_form_2 = QFrame(self.add_machine_form)
        self.top_add_hall_form_2.setObjectName(u"top_add_hall_form_2")
        self.top_add_hall_form_2.setMaximumSize(QSize(16777215, 50))
        self.top_add_hall_form_2.setFrameShape(QFrame.StyledPanel)
        self.top_add_hall_form_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.top_add_hall_form_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.top_add_hall_form_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font4)

        self.horizontalLayout_13.addWidget(self.label_13)

        self.add_machine_back_button = QPushButton(self.top_add_hall_form_2)
        self.add_machine_back_button.setObjectName(u"add_machine_back_button")
        self.add_machine_back_button.setMaximumSize(QSize(80, 30))
        self.add_machine_back_button.setFont(font9)
        self.add_machine_back_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(80, 170, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00aaff;\n"
"}")

        self.horizontalLayout_13.addWidget(self.add_machine_back_button)


        self.verticalLayout_4.addWidget(self.top_add_hall_form_2)

        self.form_frame_add_hall_2 = QFrame(self.add_machine_form)
        self.form_frame_add_hall_2.setObjectName(u"form_frame_add_hall_2")
        self.form_frame_add_hall_2.setFrameShape(QFrame.StyledPanel)
        self.form_frame_add_hall_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.form_frame_add_hall_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.add_machine_name = QLineEdit(self.form_frame_add_hall_2)
        self.add_machine_name.setObjectName(u"add_machine_name")
        self.add_machine_name.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(247, 247, 247);\n"
"	border: 2px solid #55aaff;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid #00ffff;\n"
"}")

        self.gridLayout_3.addWidget(self.add_machine_name, 0, 1, 1, 1)

        self.label_16 = QLabel(self.form_frame_add_hall_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)

        self.add_machine_id = QLineEdit(self.form_frame_add_hall_2)
        self.add_machine_id.setObjectName(u"add_machine_id")
        self.add_machine_id.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(247, 247, 247);\n"
"	border: 2px solid #55aaff;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid #00ffff;\n"
"}")

        self.gridLayout_3.addWidget(self.add_machine_id, 1, 1, 1, 1)

        self.add_machine_sensor = QLineEdit(self.form_frame_add_hall_2)
        self.add_machine_sensor.setObjectName(u"add_machine_sensor")
        self.add_machine_sensor.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(247, 247, 247);\n"
"	border: 2px solid #55aaff;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid #00ffff;\n"
"}")

        self.gridLayout_3.addWidget(self.add_machine_sensor, 3, 1, 1, 1)

        self.label_14 = QLabel(self.form_frame_add_hall_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.gridLayout_3.addWidget(self.label_14, 1, 0, 1, 1)

        self.label_15 = QLabel(self.form_frame_add_hall_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1, Qt.AlignTop)

        self.add_machine_hall = QLineEdit(self.form_frame_add_hall_2)
        self.add_machine_hall.setObjectName(u"add_machine_hall")
        self.add_machine_hall.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(247, 247, 247);\n"
"	border: 2px solid #55aaff;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:focus{\n"
"	border: 2px solid #00ffff;\n"
"}")

        self.gridLayout_3.addWidget(self.add_machine_hall, 2, 1, 1, 1)

        self.label_17 = QLabel(self.form_frame_add_hall_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.gridLayout_3.addWidget(self.label_17, 3, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.form_frame_add_hall_2)

        self.confirm_button_add_hall_2 = QFrame(self.add_machine_form)
        self.confirm_button_add_hall_2.setObjectName(u"confirm_button_add_hall_2")
        self.confirm_button_add_hall_2.setMaximumSize(QSize(16777215, 40))
        self.confirm_button_add_hall_2.setFrameShape(QFrame.StyledPanel)
        self.confirm_button_add_hall_2.setFrameShadow(QFrame.Raised)
        self.confirm_add_button_machine = QPushButton(self.confirm_button_add_hall_2)
        self.confirm_add_button_machine.setObjectName(u"confirm_add_button_machine")
        self.confirm_add_button_machine.setGeometry(QRect(610, 10, 93, 28))
        self.confirm_add_button_machine.setFont(font5)
        self.confirm_add_button_machine.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(80, 170, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	width: 80px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00aaff;\n"
"}")

        self.verticalLayout_4.addWidget(self.confirm_button_add_hall_2)

        self.stackedWidget.addWidget(self.add_machine_form)
        self.machine_info_page = QWidget()
        self.machine_info_page.setObjectName(u"machine_info_page")
        self.verticalLayout_7 = QVBoxLayout(self.machine_info_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.top_add_hall_form_3 = QFrame(self.machine_info_page)
        self.top_add_hall_form_3.setObjectName(u"top_add_hall_form_3")
        self.top_add_hall_form_3.setMaximumSize(QSize(16777215, 50))
        self.top_add_hall_form_3.setFrameShape(QFrame.StyledPanel)
        self.top_add_hall_form_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.top_add_hall_form_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_18 = QLabel(self.top_add_hall_form_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font4)

        self.horizontalLayout_14.addWidget(self.label_18)

        self.machine_info_back_button = QPushButton(self.top_add_hall_form_3)
        self.machine_info_back_button.setObjectName(u"machine_info_back_button")
        self.machine_info_back_button.setMaximumSize(QSize(80, 30))
        self.machine_info_back_button.setFont(font9)
        self.machine_info_back_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(80, 170, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	width: 80px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00aaff;\n"
"}")

        self.horizontalLayout_14.addWidget(self.machine_info_back_button)


        self.verticalLayout_7.addWidget(self.top_add_hall_form_3)

        self.machines_id_frame = QFrame(self.machine_info_page)
        self.machines_id_frame.setObjectName(u"machines_id_frame")
        self.machines_id_frame.setMaximumSize(QSize(16777215, 50))
        self.machines_id_frame.setFrameShape(QFrame.StyledPanel)
        self.machines_id_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.machines_id_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.m_info_hall = QLabel(self.machines_id_frame)
        self.m_info_hall.setObjectName(u"m_info_hall")

        self.gridLayout_4.addWidget(self.m_info_hall, 0, 3, 1, 1)

        self.label_19 = QLabel(self.machines_id_frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font7)

        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)

        self.m_info_id = QLabel(self.machines_id_frame)
        self.m_info_id.setObjectName(u"m_info_id")

        self.gridLayout_4.addWidget(self.m_info_id, 0, 1, 1, 1)

        self.label_21 = QLabel(self.machines_id_frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font7)

        self.gridLayout_4.addWidget(self.label_21, 0, 2, 1, 1)

        self.m_info_sensor = QLabel(self.machines_id_frame)
        self.m_info_sensor.setObjectName(u"m_info_sensor")

        self.gridLayout_4.addWidget(self.m_info_sensor, 0, 5, 1, 1)

        self.label_23 = QLabel(self.machines_id_frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font7)

        self.gridLayout_4.addWidget(self.label_23, 0, 4, 1, 1)


        self.verticalLayout_7.addWidget(self.machines_id_frame)

        self.tmp_nas_frame = QFrame(self.machine_info_page)
        self.tmp_nas_frame.setObjectName(u"tmp_nas_frame")
        self.tmp_nas_frame.setFrameShape(QFrame.StyledPanel)
        self.tmp_nas_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.tmp_nas_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.temperature_label = QLabel(self.tmp_nas_frame)
        self.temperature_label.setObjectName(u"temperature_label")
        self.temperature_label.setFont(font7)

        self.gridLayout_5.addWidget(self.temperature_label, 0, 0, 1, 1)

        self.NA_label = QLabel(self.tmp_nas_frame)
        self.NA_label.setObjectName(u"NA_label")
        self.NA_label.setFont(font7)

        self.gridLayout_5.addWidget(self.NA_label, 0, 1, 1, 1)

        self.NAS_bar = roundProgressBar(self.tmp_nas_frame)
        self.NAS_bar.setObjectName(u"NAS_bar")

        self.gridLayout_5.addWidget(self.NAS_bar, 1, 1, 1, 1)

        self.temperature_bar = roundProgressBar(self.tmp_nas_frame)
        self.temperature_bar.setObjectName(u"temperature_bar")

        self.gridLayout_5.addWidget(self.temperature_bar, 1, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.tmp_nas_frame)

        self.stackedWidget.addWidget(self.machine_info_page)
        self.tests_page = QWidget()
        self.tests_page.setObjectName(u"tests_page")
        self.verticalLayout_8 = QVBoxLayout(self.tests_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.test_top_frame = QFrame(self.tests_page)
        self.test_top_frame.setObjectName(u"test_top_frame")
        self.test_top_frame.setMaximumSize(QSize(16777215, 50))
        self.test_top_frame.setFrameShape(QFrame.StyledPanel)
        self.test_top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.test_top_frame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_25 = QLabel(self.test_top_frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font4)

        self.horizontalLayout_15.addWidget(self.label_25)

        self.statistics_back_button = QPushButton(self.test_top_frame)
        self.statistics_back_button.setObjectName(u"statistics_back_button")
        self.statistics_back_button.setMaximumSize(QSize(80, 30))
        self.statistics_back_button.setFont(font9)
        self.statistics_back_button.setMouseTracking(False)
        self.statistics_back_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(80, 170, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	width: 80px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00aaff;\n"
"}")

        self.horizontalLayout_15.addWidget(self.statistics_back_button)


        self.verticalLayout_8.addWidget(self.test_top_frame)

        self.graph_frame = QFrame(self.tests_page)
        self.graph_frame.setObjectName(u"graph_frame")
        self.horizontalLayout_16 = QHBoxLayout(self.graph_frame)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.stat_graph = spiralProgressBar(self.graph_frame)
        self.stat_graph.setObjectName(u"stat_graph")

        self.horizontalLayout_16.addWidget(self.stat_graph)

        self.stat_frame = QFrame(self.graph_frame)
        self.stat_frame.setObjectName(u"stat_frame")
        self.radio_temp = QRadioButton(self.stat_frame)
        self.radio_temp.setObjectName(u"radio_temp")
        self.radio_temp.setGeometry(QRect(10, 10, 111, 20))
        self.radio_nas = QRadioButton(self.stat_frame)
        self.radio_nas.setObjectName(u"radio_nas")
        self.radio_nas.setGeometry(QRect(150, 10, 111, 20))
        self.verticalLayoutWidget = QWidget(self.stat_frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 40, 191, 321))
        self.test_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.test_layout.setObjectName(u"test_layout")
        self.test_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_16.addWidget(self.stat_frame)


        self.verticalLayout_8.addWidget(self.graph_frame)

        self.stackedWidget.addWidget(self.tests_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.verticalLayout_9 = QVBoxLayout(self.settings_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.test_top_frame_2 = QFrame(self.settings_page)
        self.test_top_frame_2.setObjectName(u"test_top_frame_2")
        self.test_top_frame_2.setMaximumSize(QSize(16777215, 50))
        self.test_top_frame_2.setFrameShape(QFrame.StyledPanel)
        self.test_top_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.test_top_frame_2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_26 = QLabel(self.test_top_frame_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font4)

        self.horizontalLayout_17.addWidget(self.label_26)

        self.settings_back_button = QPushButton(self.test_top_frame_2)
        self.settings_back_button.setObjectName(u"settings_back_button")
        self.settings_back_button.setMaximumSize(QSize(80, 30))
        self.settings_back_button.setFont(font9)
        self.settings_back_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(80, 170, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 5px;\n"
"	width: 80px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #00aaff;\n"
"}")

        self.horizontalLayout_17.addWidget(self.settings_back_button)


        self.verticalLayout_9.addWidget(self.test_top_frame_2)

        self.settingsframe = QFrame(self.settings_page)
        self.settingsframe.setObjectName(u"settingsframe")
        self.settingsframe.setFrameShape(QFrame.StyledPanel)
        self.settingsframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.settingsframe)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_2 = QFrame(self.settingsframe)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.machines_shortcut = QKeySequenceEdit(self.frame_2)
        self.machines_shortcut.setObjectName(u"machines_shortcut")
        self.machines_shortcut.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_7.addWidget(self.machines_shortcut, 4, 1, 1, 1)

        self.main_menu_shortcut = QKeySequenceEdit(self.frame_2)
        self.main_menu_shortcut.setObjectName(u"main_menu_shortcut")
        self.main_menu_shortcut.setMaximumSize(QSize(100, 16777))

        self.gridLayout_7.addWidget(self.main_menu_shortcut, 2, 1, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))
        font10 = QFont()
        font10.setFamily(u"Nirmala UI")
        self.label_7.setFont(font10)

        self.gridLayout_7.addWidget(self.label_7, 1, 2, 1, 1)

        self.label_31 = QLabel(self.frame_2)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_7.addWidget(self.label_31, 8, 0, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        font11 = QFont()
        font11.setFamily(u"Nirmala UI")
        font11.setPointSize(9)
        self.label_6.setFont(font11)

        self.gridLayout_7.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_24 = QLabel(self.frame_2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font11)

        self.gridLayout_7.addWidget(self.label_24, 4, 0, 1, 1)

        self.label_28 = QLabel(self.frame_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font11)

        self.gridLayout_7.addWidget(self.label_28, 5, 0, 1, 1)

        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font11)

        self.gridLayout_7.addWidget(self.label_22, 3, 0, 1, 1)

        self.settings_shortcut = QKeySequenceEdit(self.frame_2)
        self.settings_shortcut.setObjectName(u"settings_shortcut")
        self.settings_shortcut.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_7.addWidget(self.settings_shortcut, 6, 1, 1, 1)

        self.label_20 = QLabel(self.frame_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setFont(font10)

        self.gridLayout_7.addWidget(self.label_20, 0, 2, 1, 1)

        self.label_29 = QLabel(self.frame_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font11)

        self.gridLayout_7.addWidget(self.label_29, 6, 0, 1, 1)

        self.label_30 = QLabel(self.frame_2)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_7.addWidget(self.label_30, 7, 0, 1, 1)

        self.industry_halls_shortcut = QKeySequenceEdit(self.frame_2)
        self.industry_halls_shortcut.setObjectName(u"industry_halls_shortcut")
        self.industry_halls_shortcut.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_7.addWidget(self.industry_halls_shortcut, 3, 1, 1, 1)

        self.automatic_tests_setting_time = QTimeEdit(self.frame_2)
        self.automatic_tests_setting_time.setObjectName(u"automatic_tests_setting_time")
        self.automatic_tests_setting_time.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_7.addWidget(self.automatic_tests_setting_time, 0, 1, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font11)

        self.gridLayout_7.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(300, 0))
        self.label_4.setFont(font11)

        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_32 = QLabel(self.frame_2)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_7.addWidget(self.label_32, 9, 0, 1, 1)

        self.graph_time_conversion_rate = QSpinBox(self.frame_2)
        self.graph_time_conversion_rate.setObjectName(u"graph_time_conversion_rate")
        self.graph_time_conversion_rate.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_7.addWidget(self.graph_time_conversion_rate, 1, 1, 1, 1)

        self.stats_shortcut = QKeySequenceEdit(self.frame_2)
        self.stats_shortcut.setObjectName(u"stats_shortcut")
        self.stats_shortcut.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_7.addWidget(self.stats_shortcut, 5, 1, 1, 1)

        self.label_33 = QLabel(self.frame_2)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_7.addWidget(self.label_33, 10, 0, 1, 1)

        self.box_temperature_high = QCheckBox(self.frame_2)
        self.box_temperature_high.setObjectName(u"box_temperature_high")

        self.gridLayout_7.addWidget(self.box_temperature_high, 7, 1, 1, 1, Qt.AlignHCenter)

        self.box_temperature_low = QCheckBox(self.frame_2)
        self.box_temperature_low.setObjectName(u"box_temperature_low")

        self.gridLayout_7.addWidget(self.box_temperature_low, 8, 1, 1, 1, Qt.AlignHCenter)

        self.box_filtration_start = QCheckBox(self.frame_2)
        self.box_filtration_start.setObjectName(u"box_filtration_start")

        self.gridLayout_7.addWidget(self.box_filtration_start, 9, 1, 1, 1, Qt.AlignHCenter)

        self.box_filtration_stop = QCheckBox(self.frame_2)
        self.box_filtration_stop.setObjectName(u"box_filtration_stop")

        self.gridLayout_7.addWidget(self.box_filtration_stop, 10, 1, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_19.addWidget(self.frame_2, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.settingsframe)

        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.main_body_content)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border:none;\n"
"")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.footer_left = QFrame(self.footer_frame)
        self.footer_left.setObjectName(u"footer_left")
        self.footer_left.setFrameShape(QFrame.StyledPanel)
        self.footer_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_left)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.footer_left)
        self.label_3.setObjectName(u"label_3")
        font12 = QFont()
        font12.setFamily(u"Nirmala UI")
        font12.setBold(False)
        font12.setWeight(50)
        self.label_3.setFont(font12)

        self.horizontalLayout_6.addWidget(self.label_3)


        self.horizontalLayout_5.addWidget(self.footer_left)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setStyleSheet(u"border:none\n"
"")
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip)

        self.status_frame = QFrame(self.footer_frame)
        self.status_frame.setObjectName(u"status_frame")
        self.status_frame.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid black;\n"
"background-color: rgb(255, 255, 255);")
        self.status_frame.setFrameShape(QFrame.StyledPanel)
        self.status_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.status_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.status_bar = QLabel(self.status_frame)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setFont(font9)
        self.status_bar.setStyleSheet(u"border:none")

        self.horizontalLayout_7.addWidget(self.status_bar, 0, Qt.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.status_frame)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_button.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MACHINE MANAGER", None))
        self.minimze_window_button.setText("")
        self.resize_window_button.setText("")
        self.close_window_button.setText("")
        self.stats_button.setText(QCoreApplication.translate("MainWindow", u" Statistics", None))
#if QT_CONFIG(shortcut)
        self.stats_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.machines_button.setText(QCoreApplication.translate("MainWindow", u" Machines", None))
#if QT_CONFIG(shortcut)
        self.machines_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u" Settings", None))
#if QT_CONFIG(shortcut)
        self.settings_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.home_button.setText(QCoreApplication.translate("MainWindow", u" Main Menu", None))
#if QT_CONFIG(shortcut)
        self.home_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.halls_button.setText(QCoreApplication.translate("MainWindow", u" Industry Halls", None))
#if QT_CONFIG(shortcut)
        self.halls_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"MAIN MENU", None))
        self.main_menu_machines_button.setText(QCoreApplication.translate("MainWindow", u"  Machines", None))
        self.main_menu_stats_button.setText(QCoreApplication.translate("MainWindow", u"  Statistics", None))
        self.main_menu_settings_button.setText(QCoreApplication.translate("MainWindow", u"  Settings", None))
        self.main_menu_halls_button.setText(QCoreApplication.translate("MainWindow", u"  Industry halls ", None))
        self.halls_label.setText(QCoreApplication.translate("MainWindow", u"INDUSTRY HALLS              ", None))
        self.add_hall_button.setText(QCoreApplication.translate("MainWindow", u" ADD HALL ", None))
        self.search_bar_2.setText("")
        ___qtablewidgetitem = self.halls_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Hall ", None));
        ___qtablewidgetitem1 = self.halls_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Machines", None));
        ___qtablewidgetitem2 = self.halls_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Adress", None));
        ___qtablewidgetitem3 = self.halls_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Monitor", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ADD NEW HALL                                                                           ", None))
        self.add_hall_back_button.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Hall name:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"City", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Street and number", None))
        self.confirm_add_button.setText(QCoreApplication.translate("MainWindow", u"CONFIRM", None))
        self.machines_label.setText(QCoreApplication.translate("MainWindow", u"MACHINES", None))
        self.add_machine_button.setText(QCoreApplication.translate("MainWindow", u" ADD MACHINE", None))
        self.search_bar_3.setText("")
        ___qtablewidgetitem4 = self.machines_table.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem5 = self.machines_table.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Active", None));
        ___qtablewidgetitem6 = self.machines_table.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Temperature ", None));
        ___qtablewidgetitem7 = self.machines_table.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"NAS", None));
        ___qtablewidgetitem8 = self.machines_table.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"More info", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ADD NEW MACHINE", None))
        self.add_machine_back_button.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Hall:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Machine name:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Sensors ID:", None))
        self.confirm_add_button_machine.setText(QCoreApplication.translate("MainWindow", u"CONFIRM", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"MACHINE INFO AND STATISTICS                                                  ", None))
        self.machine_info_back_button.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.m_info_hall.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.m_info_id.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Hall:", None))
        self.m_info_sensor.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Sensor ID:", None))
        self.temperature_label.setText(QCoreApplication.translate("MainWindow", u"Temperature:", None))
        self.NA_label.setText(QCoreApplication.translate("MainWindow", u"NAS:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.statistics_back_button.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.radio_temp.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.radio_nas.setText(QCoreApplication.translate("MainWindow", u"NAS", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.settings_back_button.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"(1sec = ? minutes)", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Notification when temperature is low:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Main Menu shortcut:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Machines shortcut:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Statistics shortcut:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Industry Halls shortcut:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"(everyday at ?:??)", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Settings shortcut:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Notification when temperature is high:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Set up graph time conversion:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Set up automatic test:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Notification when filtration starts:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Notification when filtration stops:", None))
        self.box_temperature_high.setText("")
        self.box_temperature_low.setText("")
        self.box_filtration_start.setText("")
        self.box_filtration_stop.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version 1.8 | ITU | Copyright RHVJTH", None))
        self.status_bar.setText(QCoreApplication.translate("MainWindow", u"Welcome to Main Menu", None))
    # retranslateUi

