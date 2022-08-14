from PySide2.QtWidgets import QPushButton


class MachineButton(QPushButton):
    def __init__(self, machine,  parent=None):
        super().__init__(parent=parent)
        self._machine = machine

    @property
    def machine(self):
        return self._machine
