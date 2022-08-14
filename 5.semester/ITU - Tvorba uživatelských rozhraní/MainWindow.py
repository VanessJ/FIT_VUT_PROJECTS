import sys, random
from PyQt5 import QtCore
from PyQt5 import QtGui
from pyqt5_plugins.examplebuttonplugin import QtGui

from view.MachineButton import MachineButton
from view.HallCheckBox import HallCheckBox
from model.Machine import Machine
from model.Hall import Hall
from view.interface import *
from PySide2 import *
from qt_material import *

class MainWindow(QMainWindow):
    def __init__(self, factory):
        QMainWindow.__init__(self)
        self._factory = factory
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QIcon(":/prefix/icons/hammer.png"))
        self.setWindowTitle("MM")
        self.back_route = self.ui.main_menu_page
        self.current_route = self.ui.main_menu_page
        self.machine = None

        #shortcuts
        self._menu_shortcut = None
        self._halls_shortcut = None
        self._machines_shortcut = None
        self._stats_shortcut = None
        self._settings_shortcut = None

        QSizeGrip(self.ui.size_grip)


        #notification settings
        self.notifications()


        self.ui.main_menu_shortcut.editingFinished.connect(lambda: self.get_menu_sequence())
        self.ui.industry_halls_shortcut.editingFinished.connect(lambda: self.get_halls_sequence())
        self.ui.machines_shortcut.editingFinished.connect(lambda: self.get_machines_sequence())
        self.ui.stats_shortcut.editingFinished.connect(lambda: self.get_stat_sequence())
        self.ui.settings_shortcut.editingFinished.connect(lambda: self.get_settings_sequence())

        self.ui.home_button.setStyleSheet("QPushButton{ \
                                            background-color: white; \
                                            border-style: outset; \
                                            border-width: 1px; \
                                            border-radius: 3x; \
                                            border-color: white; \
                                            padding: 3px;}")

        self.ui.radio_temp.setChecked(True)

        self.ui.minimze_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.resize_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        # navigation
        self.ui.home_button.clicked.connect(lambda: self.reroute(self.ui.main_menu_page))
        self.ui.halls_button.clicked.connect(lambda: self.halls_page())
        self.ui.machines_button.clicked.connect(lambda: self.machines_page())
        self.ui.stats_button.clicked.connect(lambda: self.stat_page())
        self.ui.settings_button.clicked.connect(lambda: self.reroute(self.ui.settings_page))

        self.ui.main_menu_halls_button.clicked.connect(lambda: self.halls_page())
        self.ui.main_menu_machines_button.clicked.connect(lambda: self.machines_page())
        self.ui.main_menu_stats_button.clicked.connect(lambda: self.reroute(self.ui.tests_page))
        self.ui.main_menu_settings_button.clicked.connect(lambda: self.reroute(self.ui.settings_page))
        self.ui.add_hall_button.clicked.connect(lambda: self.add_hall_page())
        self.ui.add_machine_button.clicked.connect(lambda: self.add_machine_page())
        self.ui.add_machine_back_button.clicked.connect(lambda: self.machines_page())
        self.ui.add_hall_back_button.clicked.connect(lambda: self.halls_page())
        self.ui.settings_back_button.clicked.connect(lambda: self.reroute(self.back_route))
        self.ui.statistics_back_button.clicked.connect(lambda: self.reroute(self.back_route))
        self.ui.machine_info_back_button.clicked.connect(lambda: self.machines_page())


        # halls search bar
        self.ui.search_bar_2.setPlaceholderText("Search")
        self.ui.search_bar_2.textChanged.connect(self.find_hall)

        # machines search bar
        self.ui.search_bar_3.setPlaceholderText("Search")
        self.ui.search_bar_3.textChanged.connect(lambda: self.find_machine())

        # status bar text updating
        self.ui.home_button.clicked.connect(lambda: self.clicked_button_bar("Welcome to Main Menu"))
        self.ui.halls_button.clicked.connect(lambda: self.clicked_button_bar("Here you can find all halls and info about them"))
        self.ui.machines_button.clicked.connect(lambda: self.clicked_button_bar("Table of all machines"))
        self.ui.stats_button.clicked.connect(lambda: self.clicked_button_bar("Statistics of all machines combined"))
        self.ui.settings_button.clicked.connect(lambda: self.clicked_button_bar("Welcome to Settings page"))
        self.ui.add_hall_button.clicked.connect(lambda: self.clicked_button_bar("Fill out the form and click CONFIRM to add a new hall"))
        self.ui.add_machine_button.clicked.connect(lambda: self.clicked_button_bar("Fill out the form and click CONFIRM to add a new machine"))
        self.ui.machine_info_back_button.clicked.connect(lambda: self.clicked_button_bar("Table of all machines"))
        self.ui.add_hall_back_button.clicked.connect(lambda: self.clicked_button_bar("Here you can find all halls and info about them"))
        self.ui.add_machine_back_button.clicked.connect(lambda: self.clicked_button_bar("Table of all machines"))
        self.ui.confirm_add_button_machine.clicked.connect(lambda: self.clicked_button_bar("Machine sucessfully added"))
        self.ui.confirm_add_button.clicked.connect(lambda: self.clicked_button_bar("Hall sucessfully added"))
        self.ui.main_menu_halls_button.clicked.connect(lambda: self.clicked_button_bar("Here you can find all halls and info about them"))
        self.ui.main_menu_machines_button.clicked.connect(lambda: self.clicked_button_bar("Table of all machines"))
        self.ui.main_menu_stats_button.clicked.connect(lambda: self.clicked_button_bar("Statistics of all machines combined"))
        self.ui.main_menu_settings_button.clicked.connect(lambda: self.clicked_button_bar("Welcome to Settings page"))

        def move_window(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.header_frame.mouseMoveEvent = move_window

        self.ui.menu_button.clicked.connect(lambda: self.slideLeftMenu())


    def notifications(self):
        self.ui.box_temperature_high.setChecked(False)
        self.ui.box_temperature_high.stateChanged.connect(lambda: self.turn_off_notifications())
        self.ui.box_temperature_low.setChecked(False)
        self.ui.box_temperature_low.stateChanged.connect(lambda: self.turn_on_notifications())
        self.ui.box_filtration_stop.setChecked(False)
        self.ui.box_filtration_stop.stateChanged.connect(lambda: self.filtration_off_notifications())
        self.ui.box_filtration_start.setChecked(False)
        self.ui.box_filtration_start.stateChanged.connect(lambda: self.filtration_on_notifications())

    def turn_off_notifications(self):
        self._factory.turn_off_notifications()

    def turn_on_notifications(self):
        self._factory.turn_on_notifications()

    def filtration_off_notifications(self):
        self._factory.filtration_off_notifications()

    def filtration_on_notifications(self):
        self._factory.filtration_on_notifications()

    def get_menu_sequence(self):
        self._menu_shortcut = QKeySequence(self.ui.main_menu_shortcut.keySequence().toString()).toString()
        QShortcut(QKeySequence(self._menu_shortcut), self).activated.connect(lambda: self.reroute(self.ui.main_menu_page))

    def get_halls_sequence(self):
        self._halls_shortcut = QKeySequence(self.ui.industry_halls_shortcut.keySequence().toString()).toString()
        QShortcut(QKeySequence(self._halls_shortcut), self).activated.connect(lambda: self.halls_page())

    def get_machines_sequence(self):
        self._machines_shortcut = QKeySequence(self.ui.machines_shortcut.keySequence().toString()).toString()
        QShortcut(QKeySequence(self._machines_shortcut), self).activated.connect(lambda: self.machines_page())

    def get_stat_sequence(self):
        self._stats_shortcut = QKeySequence(self.ui.stats_shortcut.keySequence().toString()).toString()
        QShortcut(QKeySequence(self._stats_shortcut), self).activated.connect(lambda: self.stat_page())

    def get_settings_sequence(self):
        self._settings_shortcut = QKeySequence(self.ui.settings_shortcut.keySequence().toString()).toString()
        QShortcut(QKeySequence(self._settings_shortcut), self).activated.connect(lambda: self.reroute(self.ui.settings_page))



    def update_values(self):
        self._factory.manage_halls()
        if self.current_route is self.ui.machine_info_page:
            self.machine_info_page(self.machine)
        if self.current_route is self.ui.tests_page:
            self.stat_page()
        if self.current_route is self.ui.machines_list_page:
            self.machines_page()

    def reset_active_page(self):
        style_sheet = "QPushButton:hover{ \
	                    border-radius: 5px; \
	                    border: 1px solid White; \
                        background-color: #00aaff; \ }"

        self.ui.home_button.setStyleSheet(style_sheet)
        self.ui.halls_button.setStyleSheet(style_sheet)
        self.ui.machines_button.setStyleSheet(style_sheet)
        self.ui.stats_button.setStyleSheet(style_sheet)
        self.ui.settings_button.setStyleSheet(style_sheet)

    def active_page(self):
        self.reset_active_page()
        if self.current_route is self.ui.main_menu_page:
            self.ui.home_button.setStyleSheet("QPushButton{ \
                                                background-color: white; \
                                                border-style: outset; \
                                                border-width: 1px; \
                                                border-radius: 3x; \
                                                border-color: white; \
                                                padding: 3px;}")
        if self.current_route is self.ui.tests_page:
            self.ui.stats_button.setStyleSheet("QPushButton{ \
                                                background-color: white; \
                                                border-style: outset; \
                                                border-width: 1px; \
                                                border-radius: 3x; \
                                                border-color: white; \
                                                padding: 3px;}")
        if self.current_route is self.ui.machines_list_page:
            self.ui.machines_button.setStyleSheet("QPushButton{ \
                                                background-color: white; \
                                                border-style: outset; \
                                                border-width: 1px; \
                                                border-radius: 3x; \
                                                border-color: white; \
                                                padding: 3px;}")
        if self.current_route is self.ui.settings_page:
            self.ui.settings_button.setStyleSheet("QPushButton{ \
                                                background-color: white; \
                                                border-style: outset; \
                                                border-width: 1px; \
                                                border-radius: 3x; \
                                                border-color: white; \
                                                padding: 3px;}")
        if self.current_route is self.ui.halls_list_page:
            self.ui.halls_button.setStyleSheet("QPushButton{ \
                                                background-color: white; \
                                                border-style: outset; \
                                                border-width: 1px; \
                                                border-radius: 3x; \
                                                border-color: white; \
                                                padding: 3px;}")



    def temp_radio(self):
        if self.ui.radio_temp.isChecked():
            self.ui.radio_nas.setChecked(False)
            self.stat_page()

    def nas_radio(self):
        if self.ui.radio_nas.isChecked():
            self.ui.radio_temp.setChecked(False)
            self.stat_page()


    def stat_page(self):
        self.reroute(self.ui.tests_page)
        colors = ((0, 51, 104), (0, 153, 153), (102, 0, 102), (153, 0, 51), (102, 204, 255), (255, 255, 255))
        self.ui.radio_temp.toggled.connect(lambda: self.temp_radio())
        self.ui.radio_nas.toggled.connect(lambda: self.nas_radio())

        if self.ui.radio_temp.isChecked():

            # temperature
            temp_values = []
            m_colors = []
            max = []

            hall = self._factory.monitored_hall()
            self.ui.stat_graph.spb_setNoProgressBar(len(hall.machines))
            self.ui.stat_graph.spb_lineWidth(15)
            i = 0

            while self.ui.test_layout.count():
                child = self.ui.test_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

            for machine in hall.machines:
                temp_values.append(machine.temperature)
                max.append(150)
                m_colors.append(colors[i % 5])
                label_text = machine.identification + " " + str(machine.temperature) + " °C "
                label = QLabel(label_text)
                style = "color: rgb" + str(colors[i % 5]) + "; "

                label.setStyleSheet(style)
                self.ui.test_layout.addWidget(label)
                i += 1

            self.ui.stat_graph.spb_setMaximum(tuple(max))
            self.ui.stat_graph.spb_setValue(tuple(temp_values))
            self.ui.stat_graph.spb_lineColor(tuple(m_colors))

        if self.ui.radio_nas.isChecked():

            # temperature
            nas_values = []
            m_colors = []
            max = []

            hall = self._factory.monitored_hall()
            self.ui.stat_graph.spb_setNoProgressBar(len(hall.machines))
            self.ui.stat_graph.spb_lineWidth(15)
            i = 0

            while self.ui.test_layout.count():
                child = self.ui.test_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

            for machine in hall.machines:
                nas_values.append(machine.nas)
                max.append(12)
                m_colors.append(colors[i % 5])
                label_text = machine.identification + " " + str(machine.nas)
                label = QLabel(label_text)
                style = "color: rgb" + str(colors[i % 5]) + "; "

                label.setStyleSheet(style)
                self.ui.test_layout.addWidget(label)
                i += 1

            self.ui.stat_graph.spb_setMaximum(tuple(max))
            self.ui.stat_graph.spb_setValue(tuple(nas_values))
            self.ui.stat_graph.spb_lineColor(tuple(m_colors))




    def add_hall_page(self):
        self.reroute(self.ui.add_hall_form)
        self.ui.confirm_add_button.clicked.connect(lambda: self.create_hall())

    def add_machine_page(self):
        self.reroute(self.ui.add_machine_form)
        self.ui.confirm_add_button_machine.clicked.connect(lambda: self.create_machine())

    def create_hall(self):
        hall_name = self.ui.add_hall_name.text()
        hall_city = self.ui.add_hall_city.text()
        hall_street = self.ui.add_hall_street.text()
        hall_id = self.ui.add_hall_id.text()
        name = hall_name + " " + hall_id
        address = hall_city + hall_street
        hall = Hall(name, address)
        self._factory.add_hall(hall)
        self.halls_page()

    def create_machine(self):
        machine_name = self.ui.add_machine_name.text()
        machine_id = self.ui.add_machine_id.text()
        machine_sensor = self.ui.add_machine_sensor.text()
        name = machine_name + " " + machine_id
        machine = Machine(name)
        machine.sensor = machine_sensor
        self._factory.monitored_hall().add_machine(machine)
        self.machines_page()

    def find_machine(self):
        name = self.ui.search_bar_3.text().lower()
        for row in range(self.ui.machines_table.rowCount()):
            item = self.ui.machines_table.item(row, 0)
            self.ui.machines_table.setRowHidden(row, name not in item.text().lower())

    def find_hall(self):
        name = self.ui.search_bar_2.text().lower()
        for row in range(self.ui.halls_table.rowCount()):
            item = self.ui.halls_table.item(row, 0)
            self.ui.halls_table.setRowHidden(row, name not in item.text().lower())

    def halls_page(self):
        self.reroute(self.ui.halls_list_page)
        self.print_halls_table()

    def machines_page(self):
        self.reroute(self.ui.machines_list_page)
        hall = self._factory.monitored_hall()
        self.print_machines_table(hall)

    def print_machines_table(self, hall):
        self.ui.machines_table.setRowCount(0)
        self.ui.machines_table.verticalHeader().hide()

        for machine in hall.machines:
            row_pos = self.ui.machines_table.rowCount()
            button = MachineButton(machine)
            button.setText("Details")

            self.ui.machines_table.insertRow(row_pos)
            self.ui.machines_table.setItem(row_pos, 0, QTableWidgetItem(machine.identification))
            if machine.is_operating():
                item = QTableWidgetItem('Operating')
                item.setForeground(QBrush(QColor(0, 128, 0)))
                self.ui.machines_table.setItem(row_pos, 1, item)
            else:
                item = QTableWidgetItem('Not operating')
                item.setForeground(QBrush(QColor(255, 0, 0)))
                self.ui.machines_table.setItem(row_pos, 1, item)
            self.ui.machines_table.setItem(row_pos, 2, QTableWidgetItem(str(machine.temperature)))
            self.ui.machines_table.setItem(row_pos, 3, QTableWidgetItem(str(machine.nas)))
            self.ui.machines_table.setCellWidget(row_pos, 4, button)
            button.clicked.connect(lambda: self.machine_button_pressed())
            self.find_machine()

    def machine_button_pressed(self):
        button = self.focusWidget()
        machine = button.machine
        self.machine_info_page(machine)



    def machine_info_page(self, machine):
        self.machine = machine
        self.reroute(self.ui.machine_info_page)
        self.ui.m_info_id.setText(machine.identification)
        self.ui.m_info_hall.setText(self._factory.monitored_hall().name)
        self.ui.m_info_sensor.setText(machine.sensor)

        # Temperature
        self.ui.temperature_bar.rpb_setRange(0, 150)
        self.ui.temperature_bar.rpb_setTextFormat('Value')
        self.ui.temperature_bar.rpb_setValue(machine.temperature)

        if machine.temperature > 40:
            self.ui.temperature_bar.rpb_setLineColor((255, 216, 0))
            self.ui.temperature_bar.rpb_setTextColor((255, 216, 0))

        if machine.temperature > 100:
            self.ui.temperature_bar.rpb_setLineColor((255, 0, 0))
            self.ui.temperature_bar.rpb_setTextColor((255, 0, 0))

        # Nas
        self.ui.NAS_bar.rpb_setRange(0, 12)
        self.ui.NAS_bar.rpb_setTextFormat('Value')
        self.ui.NAS_bar.rpb_setValue(machine.nas)
        self.ui.NAS_bar.rpb_setLineStyle('DotLine')

        if machine.nas >= 10:
            self.ui.NAS_bar.rpb_setLineColor((32, 42, 68))
            self.ui.NAS_bar.rpb_setTextColor((32, 42, 68))

        if machine.nas < 10:
            self.ui.NAS_bar.rpb_setTextColor((75, 104, 184))
            self.ui.NAS_bar.rpb_setLineColor((75, 104, 184))



    def print_halls_table(self):
        self.ui.halls_table.setRowCount(0)
        self.ui.halls_table.verticalHeader().hide()

        for hall in self._factory.halls:
            check_box = HallCheckBox(hall)
            row_pos = self.ui.halls_table.rowCount()
            self.ui.halls_table.insertRow(row_pos)
            self.ui.halls_table.setItem(row_pos, 0, QTableWidgetItem(hall.name))
            self.ui.halls_table.setItem(row_pos, 1, QTableWidgetItem(str(len(hall.machines))))
            self.ui.halls_table.setItem(row_pos, 2, QTableWidgetItem(hall.address))
            self.ui.halls_table.setCellWidget(row_pos, 3, check_box)
            if hall.monitored:
                check_box.setChecked(True)

            check_box.stateChanged.connect(lambda: self.handle_halls_checkbox())

    def handle_halls_checkbox(self):
        check_box = self.focusWidget()
        if check_box.isChecked():
            self._factory.monitor(check_box.hall)
            self.print_halls_table()

    def halls_checkbox(self, checkbox, hall):
        if checkbox.isChecked():
            self._factory.monitor(hall)
            self.print_halls_table()

    def slideLeftMenu(self):
        width = self.ui.left_menu_frame.width()

        if width == 40:
            newWidth = 155
        else:
            newWidth = 40

        self.animation = QPropertyAnimation(self.ui.left_menu_frame, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.resize_window_button.setIcon(QtGui.QIcon(u":/prefix/icons/albums.png"))
        else:
            self.showMaximized()
            self.ui.resize_window_button.setIcon(QtGui.QIcon(u":/prefix/icons/copy.png"))

    def reroute(self, route):
        self.current_route = route
        self.active_page()
        previous_page = self.ui.stackedWidget.currentWidget()
        self.ui.stackedWidget.setCurrentWidget(route)
        if previous_page is not self.ui.stackedWidget.currentWidget():
            self.back_route = previous_page

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def clicked_button_bar(self, text):
        self.ui.status_bar.setText(text)
