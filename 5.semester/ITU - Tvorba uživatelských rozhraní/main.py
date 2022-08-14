from model.Machine import Machine
from model.Hall import Hall
from model.Factory import Factory
from model.Simulation import Simulation
from MainWindow import MainWindow
import time
import schedule
from view.interface import *
from qt_material import *


if __name__ == "__main__":

    hallA = Hall("Hall A", "Bratislava 4")
    machine1 = Machine("M1")
    machine2 = Machine("M2")
    machine3 = Machine("M3")

    machine4 = Machine("M4")
    machine5 = Machine("M5")
    machine6 = Machine("M6")

    hallA.add_machine(machine1)
    hallA.add_machine(machine2)
    hallA.add_machine(machine3)

    hallB = Hall("Hall B", "Košice 5")
    hallB.add_machine(machine4)
    hallB.add_machine(machine5)
    hallB.add_machine(machine6)

    f = Factory()
    f.add_hall(hallA)
    f.add_hall(hallB)
    f.monitor(hallA)

    sim = Simulation(f)
    sim.start_all()

    app = QApplication(sys.argv)
    window = MainWindow(f)
    window.ui.stackedWidget.setCurrentWidget(window.ui.main_menu_page)
    window.show()

    schedule.every(1).seconds.do(lambda: sim.operating_update())
    schedule.every(1).seconds.do(lambda: sim.stopped_update())
    schedule.every(5).seconds.do(lambda: sim.not_filtering_update())
    schedule.every(2).seconds.do(lambda: sim.filtering_update())
    schedule.every(1).seconds.do(lambda: window.update_values())

    while True:
        QApplication.processEvents()
        schedule.run_pending()
        time.sleep(0.01)

    app.exec_()








