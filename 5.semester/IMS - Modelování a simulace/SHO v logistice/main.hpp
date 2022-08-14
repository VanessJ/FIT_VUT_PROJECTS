#include "car.hpp"

class PackagePrep : public Event
{
public:
    void Behavior();
    void SetCar(Car *car);

private:
    Car *car;
};
