from PySide2.QtWidgets import QCheckBox


class HallCheckBox(QCheckBox):
    def __init__(self, hall,  parent=None):
        super().__init__(parent=parent)
        self._hall = hall

    @property
    def hall(self):
        return self._hall

