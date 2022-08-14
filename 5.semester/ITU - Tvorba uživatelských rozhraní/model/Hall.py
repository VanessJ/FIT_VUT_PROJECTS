from win10toast import ToastNotifier
import time


class Hall:

    def __init__(self, name, address):
        self._name = name
        self._address = address
        self._machines = []
        self._monitored = False

        #notification settings
        self._notifier = None
        self._turn_on_notification = False
        self._turn_off_notification = False
        self._filtration_off_notification = False
        self._filtration_on_notification = False

    def turn_on_notifications(self):
        if self._turn_on_notification is False:
            self._turn_on_notification = True
        elif self._turn_on_notification is True:
            self._turn_on_notification = False

    def turn_off_notifications(self):
        if self._turn_off_notification is False:
            self._turn_off_notification = True
        elif self._turn_off_notification is True:
            self._turn_off_notification = False

    def filtration_off_notifications(self):
        if self._filtration_on_notification is False:
            self._filtration_on_notification = True
        elif self._filtration_on_notification is True:
            self._filtration_on_notification = False

    def filtration_on_notifications(self):
        if self._filtration_off_notification is False:
            self._filtration_off_notification = True
        elif self._filtration_off_notification is True:
            self._filtration_off_notification = False

    # name getter
    @property
    def name(self):
        return self._name

    # machines getter
    @property
    def machines(self):
        return self._machines

    @property
    def address(self):
        return self._address

    @property
    def monitored(self):
        return self._monitored
    @property
    def notifier(self):
        return self._notifier

    @notifier.setter
    def notifier(self, notifier):
        self._notifier = notifier

    @name.setter
    def name(self, name):
        self._name = name

    @address.setter
    def address(self, address):
        self._address = address

    # selects machine from group by id
    def get_by_id(self, identification):
        for machine in self._machines:
            if machine.identification == identification:
                return machine
        return None

    def add_machine(self, machine):
        self._machines.append(machine)

    def monitor(self):
        self._monitored = True

    def stop_monitoring(self):
        self._monitored = False

    def manage_machines(self):
        for machine in self._machines:
            if machine.is_operating() and machine.temperature >= 120:
                machine.turn_off()
                if self._turn_off_notification and self._monitored:
                    n_text = machine.identification + ": temperature exceeded 120°C - turning off"
                    self._notifier.show_toast("Machine Manager", n_text, duration=10, threaded=True)
            if machine.is_operating() is False and machine.temperature <= 50:
                machine.turn_on()
                if self._turn_on_notification and self._monitored:
                    n_text = machine.identification + ": temperature bellow 50° C - resuming operation"
                    self._notifier.show_toast("Machine Manager", n_text, duration=10, threaded=True)
            if machine.is_filtering() and machine.nas <= 3:
                machine.stop_filtering()
                if self._filtration_off_notification and self._monitored:
                    n_text = machine.identification + ": NAS bellow 3 - Stopped filtration"
                    self._notifier.show_toast("Machine Manager", n_text, duration=10, threaded=True)
            if machine.is_filtering() is False and machine.nas >= 10:
                machine.filter()
                if self._filtration_on_notification and self._monitored:
                    n_text = machine.identification + ": NAS exceeded value 12 - starting filtration"
                    self._notifier.show_toast("Machine Manager", n_text, duration=10, threaded=True)

    def print_values(self):
        for machine in self._machines:
            print(machine.identification)
            if machine.is_operating():
                print("\tCurrently operating")
            if machine.is_filtering():
                print("\tCurrently filtering")
            print("\tTemperature: " + str(machine.temperature) + "°C")
            if machine.is_operating() and machine.temperature >= 120:
                print("\tStopping operation")
                machine.turn_off()
            if machine.is_operating() is False and machine.temperature <= 50:
                print("\tTurning on")
                machine.turn_on()
            print("\tNAS value: " + str(machine.nas))
            if machine.is_filtering() and machine.nas <= 3:
                print("\tStopping filtration")
                machine.stop_filtering()
            if machine.is_filtering() is False and machine.nas >= 12:
                print("\tStarting filtration")
                machine.filter()
            print("")


