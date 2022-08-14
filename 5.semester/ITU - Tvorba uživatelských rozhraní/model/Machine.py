import random
import time


class Machine:

    def __init__(self, identification):

        # string name or number id
        self._identification = identification
        self._operating = True
        self._filtering = False
        self._monitored = False
        self._start_time = 0
        self._temperature = random.randint(40, 50)
        self._nas = random.randint(5, 12)
        self._sensor = "SD 100"

    @property
    def sensor(self):
        return self._sensor

    # identification getter
    @property
    def identification(self):
        return self._identification

    # runtime getter
    @property
    def start_time(self):
        return self._start_time

    # temperature getter
    @property
    def temperature(self):
        return self._temperature

    # nas getter
    @property
    def nas(self):
        return self._nas

    @identification.setter
    def identification(self, identification):
        self._identification = identification

    @sensor.setter
    def sensor(self, sensor):
        self._sensor = sensor

    @start_time.setter
    def runtime(self, number):
        self._start_time = number

    @temperature.setter
    def temperature(self, number):
        self._temperature = number

    @nas.setter
    def nas(self, number):
        self._nas = number

    def is_operating(self):
        return self._operating

    def is_filtering(self):
        return self._filtering

    def is_monitored(self):
        return self._monitored

    def monitor(self):
        self._monitored = True

    def stop_monitoring(self):
        self._monitored = False

    def turn_on(self):
        self._operating = True

    def turn_off(self):
        self._operating = False

    def filter(self):
        self._filtering = True

    def stop_filtering(self):
        self._filtering = False

