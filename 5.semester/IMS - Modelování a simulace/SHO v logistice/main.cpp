
#include <iostream>
#include <vector>
#include <time.h>
#include "simlib.h"
#include "main.hpp"
#include "car.hpp"
#include "package.hpp"
#include "min_convertor.hpp"

using namespace std;

#define MULTIPLE_DELIVERIES false
#define DAYS 1

#define MIN_ORDER 2
#define MAX_ORDER 8

Stat STAT_DriverBreak("Time between deliveries\n");
Stat STAT_KM("Distance in km\n");
Stat STAT_DELIVERY_TIME("Delivery duration in minutes\n");
Stat STAT_UNFINISHED_DELIVERY("Number of unfinished deliveries\n");
Stat STAT_FUEL_CONSUMPTION("Fuel consumption\n");
Stat STAT_FUEL_COST("Cost of fuel\n");
Stat STAT_DRIVER_COST("Cost of driver\n");
Stat STAT_TOP_TRANS_COST("Cost of Toptrans");

int main()
{
    RandomSeed(time(NULL));

    for (int i = 0; i < 100000; i++)
    {
        PackagePrep prep;
        Car car;
        prep.SetCar(&car);
        Init(0, 60 * 24 * DAYS);
        prep.Activate();

        Run();
        double total_distance = car.GetTotalDistance();
        double duration = car.GetDuration();
        if (total_distance == 0)
        {
            STAT_UNFINISHED_DELIVERY(total_distance);
        }
        else
        {
            STAT_KM(total_distance);
        }

        if (duration != 0)
        {
            STAT_DELIVERY_TIME(duration);
        }

        if (car.GetFuelCost() != 0)
        {
            STAT_FUEL_COST(car.GetFuelCost());
        }

        if (car.GetConsumption() != 0)
        {
            STAT_FUEL_CONSUMPTION(car.GetConsumption());
        }

        if (car.getDriverCost() != 0)
        {
            STAT_DRIVER_COST(car.getDriverCost());
        }
        if (car.getTopTransCost() != 0)
        {
            STAT_TOP_TRANS_COST(car.getTopTransCost());
        }
    }
    STAT_KM.Output();
    STAT_DELIVERY_TIME.Output();
    STAT_UNFINISHED_DELIVERY.Output();
    STAT_FUEL_COST.Output();
    STAT_FUEL_CONSUMPTION.Output();
    STAT_DRIVER_COST.Output();
    STAT_TOP_TRANS_COST.Output();
}

void PackagePrep::Behavior()
{

#ifdef VERBOSE
    cout << "\n\n\nPríchod nových balíčkov:\n";
#endif
    int order_amount = Uniform(MIN_ORDER, MAX_ORDER);
    // int order_amount = 10;
    std::vector<Package> packages;
    for (int i = 0; i < order_amount; i++)
    {
        Package package;
        packages.push_back(package);
    }

    this->car->SetQueue(packages);
    if (this->car->InDepo())
    {
        double end_time = car->GetEndTime();
        if (end_time != 0)
        {
            double break_duration = Time - end_time;
            cout << "Prestávka medzi jazdami trvala: " << TransformToHours(break_duration) << ":" << TransformToMinutes(break_duration) << " hodín\n";
            STAT_DriverBreak(break_duration);
        }
        this->car->Activate();
    }

    else
    {
        cout << "\n\n\n Auto nie je načas v depe \n \n \n";
    }
    if (MULTIPLE_DELIVERIES)
    {
        Activate(Time + Normal(24 * 60, 10));
    }
}

void PackagePrep::SetCar(Car *car)
{
    this->car = car;
}
