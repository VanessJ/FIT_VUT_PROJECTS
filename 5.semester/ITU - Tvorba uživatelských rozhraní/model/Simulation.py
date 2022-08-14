import random

class Simulation:

    def __init__(self, factory):
        self._factory = factory

    def start_all(self):
        for hall in self._factory.halls:
            for machine in hall.machines:
                machine.turn_on()

    # updates temperatures of currently operating machines
    def operating_update(self):
        for hall in self._factory.halls:
            for machine in hall.machines:
                if machine.is_operating():
                    tmp_change = random.randint(1, 5)
                    machine.temperature = machine.temperature + tmp_change
                if machine.temperature > 120:
                    machine.temperature = 120

    def runtime_update(self):
        for machine in self._machine_group:
            if machine.is_operating():
                machine.runtime += 1

    # updates temperatures of currently stopped machines
    def stopped_update(self):
        for hall in self._factory.halls:
            for machine in hall.machines:
                if machine.is_operating() is False:
                    tmp_change = random.randint(1, 3)
                    machine.temperature = machine.temperature - tmp_change
                if machine.temperature < 0:
                    machine.temperature = 0


    # updates nas values of currently filtering machines
    def filtering_update(self):
        for hall in self._factory.halls:
            for machine in hall.machines:
                if machine.is_filtering():
                    nas_change = random.randint(0, 2)
                    machine.nas = machine.nas - nas_change
                if machine.nas < 0:
                    machine.nas = 0

    # updates nas values of not filtering machines
    def not_filtering_update(self):
        for hall in self._factory.halls:
            for machine in hall.machines:
                if machine.is_filtering() is False:
                    nas_change = random.randint(0, 2)
                    machine.nas = machine.nas + nas_change
                if machine.nas > 12:
                    machine.nas = 12







