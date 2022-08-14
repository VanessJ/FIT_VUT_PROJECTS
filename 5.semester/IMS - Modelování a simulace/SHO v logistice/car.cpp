#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <fstream>

#include "simlib.h"
#include "car.hpp"
#include "min_convertor.hpp"
using namespace std;

#define BETWEEN_REGIONS_SPEED 1
#define IN_REGION_SPEED 2

#define DRIVER_COST_HOUR 174
#define CENTRAL "ZLK"
//#define VERBOSE true

#define DIESEL_PRICE 35.65

struct distance_to_region;
string regions[14] = {"ZLK", "MSK", "JHM", "OLK", "VYS", "JHC", "PLK", "KVK", "STC", "Praha", "HKK", "PAK", "LBK", "ULK"};

Car::Car()
{

    this->current_region = CENTRAL;
    this->in_depo = true;
    this->capacity = 50;
    this->end_time = 0;
    this->distance = 0;
    this->total_distance = 0;
}

double Car::GetConsumption()
{
    return this->consumption;
}

double Car::GetFuelCost()
{
    return this->fuel_cost;
}

double Car::GetEndTime()
{
    return this->end_time;
}

double Car::GetTotalDistance()
{
    return this->total_distance;
}

double Car::GetDuration()
{
    return this->duration;
}

double Car::getTopTransCost()
{
    return this->top_trans_cost;
}

double Car::getDriverCost()
{
    return this->duration / 60 * DRIVER_COST_HOUR;
}

bool Car::InDepo()
{
    return this->in_depo;
}

void Car::topTransPrice()
{
    if (this->distance > 800)
    {
        this->top_trans_cost += 1073;
    }
    else if (this->distance > 700)
    {
        this->top_trans_cost += 1014;
    }
    else if (this->distance > 600)
    {
        this->top_trans_cost += 931;
    }
    else if (this->distance > 500)
    {
        this->top_trans_cost += 916;
    }
    else if (this->distance > 400)
    {
        this->top_trans_cost += 866;
    }
    else if (this->distance > 300)
    {
        this->top_trans_cost += 807;
    }
    else if (this->distance > 200)
    {
        this->top_trans_cost += 744;
    }
    else if (this->distance > 100)
    {
        this->top_trans_cost += 658;
    }
    else
    {
        this->top_trans_cost += 549;
    }
}

void Car::Behavior()
{
begin:

    this->road_time = 0;
    this->distance = 0;
    this->visit_in_row = 1;
    this->consumption = 0;
    this->fuel_cost = 0;
    this->top_trans_cost = 0;

    in_depo = false;

    while (this->queue.size())
    {
        if (this->loaded_packages.size() >= capacity)
        {
#ifdef VERBOSE
            cout << "Auto kvôli kapacite nemohlo naložiť všetko\n";
#endif
            break;
        }
        this->loadPackage();
    }
    this->loadDistances();
    this->chooseDistanceTable();
#ifdef VERBOSE
    cout << "\n";
#endif

    this->start_time = Time;
    while (this->loaded_packages.size() != 0)
    {
        this->travelToClosest();
        this->deliverPackage();
        this->chooseDistanceTable();
#ifdef VERBOSE
        cout << "\n";
#endif
    }
    this->returnToDepo();
    this->end_time = Time;
    this->duration = this->end_time - this->start_time;
    this->total_distance = distance;
    this->consumption = (this->distance / 100) * 10.5;
    this->fuel_cost = consumption * DIESEL_PRICE;

#ifdef VERBOSE
    cout << "######################################################################################\n";
    cout << "Auto sa vrátilo, aktuálny čas: " << Time << "\n";
    // cout << "Celý proces trval: " << delivery_time << "\n";
    cout << "Celý proces trval: " << TransformToHours(this->duration) << ":" << TransformToMinutes(this->duration) << "hodín\n";
    // cout << "Auto na ceste strávilo " << this->road_time << " minút\n";
    cout << "Auto na ceste strávilo " << TransformToHours(this->road_time) << ":" << TransformToMinutes(this->road_time) << " hodín\n";
    cout << "Najazdilo " << this->distance << " km\n";
    cout << "Spotreba: " << consumption << "l \n";
    cout << "Cena benzínu: " << fuel_cost << " czk\n";
    cout << "Cena za vodiča: " << this->getDriverCost() << "\n";
    cout << "Ekvivalent TopTrans ceny: " << this->getTopTransCost() << "\n";
    cout << "######################################################################################\n";
#endif
    if (queue.size())
    {
        cout << "\nAuto nestihlo rozniesť všetky objednávky na čas, musí okamžite začať novú trasu\n";
        goto begin;
    }
    Passivate();
    goto begin;
}

double Car::distanceFromTime(double time)
{
    double speed_km;
    if (this->speed == BETWEEN_REGIONS_SPEED)
    {
        speed_km = Lim(Normal(80, 10), 10, 120).Value();
        // speed_km = Normal(80, 10);
    }
    else
    {
        speed_km = Lim(Normal(50, 5), 10, 120).Value();
        // speed_km = Normal(40, 5);
    }
    double km = (time / 60) * speed_km;
#ifdef VERBOSE
    cout << "Priemerná rýchlosť auta: " << speed_km << "\n";
    cout << "Na tomto úseku prešlo " << km << "km\n";
#endif

    return km;
}

void Car::SetQueue(std::vector<Package> q)
{
    for (int i = 0; i < q.size(); i++)
    {
        this->queue.push_back(q[i]);
    }
}

void Car::returnToDepo()
{

    distance_to_region next_region;
    for (int i = 0; i < 14; i++)
    {
        if (this->current_region_distancies[i].region == CENTRAL)
        {
            next_region = this->current_region_distancies[i];
        }
    }

#ifdef VERBOSE
    cout << "Auto sa vracia do: " << next_region.region << ": " << next_region.distance << " " << next_region.mean << "\n";
#endif

    if (next_region.region == this->current_region)
    {
        this->speed = IN_REGION_SPEED;
        this->visit_in_row++;
        // cout << "Visit in row inkrementovaná\n";
    }
    else
    {
        this->speed = BETWEEN_REGIONS_SPEED;
        this->visit_in_row = 1;
    }

    double disperse = sqrt(next_region.mean);
    double wait_time = Normal(next_region.distance, disperse);

    // spodny limit
    if (wait_time < 0)
    {
        wait_time = 5;
    }

    if (visit_in_row > 1)
    {
        wait_time = wait_time / visit_in_row;
        // cout << "Visit in row: " << this->visit_in_row << " ,čas je skrátený na " << wait_time << "\n";
    }

#ifdef VERBOSE
    cout << "Trvá mu to: " << wait_time << "\n";
#endif

    this->distance += this->distanceFromTime(wait_time);
    this->road_time += wait_time;
    Wait(wait_time);
    this->in_depo = true;
}

void Car::travelToClosest()
{
    int min = 10000;
    string region;
    distance_to_region next_region;
    for (int i = 0; i < 14; i++)
    {
        if (this->current_region_distancies[i].distance < min)
        {
            region = current_region_distancies[i].region;
            bool found = false;

            // looping though all packages to see if there is any delivery scheduled to current minimum region
            for (int i = 0; i < this->loaded_packages.size(); i++)
            {
                if (this->loaded_packages[i].region == region)
                {
                    found = true;
                }
            }

            if (found == true)
            {
                min = this->current_region_distancies[i].distance;
                next_region = this->current_region_distancies[i];
            }
        }
    }

#ifdef VERBOSE
    cout << "Nájdené ako najbližšie: " << next_region.region << " so vzdialenosťou " << next_region.distance << "\n";
#endif

    if (next_region.region == this->current_region)
    {
        this->speed = IN_REGION_SPEED;
        this->visit_in_row++;
        // cout << "Visit in row inkrementovaná\n";
    }
    else
    {
        this->speed = BETWEEN_REGIONS_SPEED;
        this->visit_in_row = 1;
    }

    double disperse = sqrt(next_region.mean);
    // cout << "Rozptyl: " << disperse << "\n";
    double wait_time = Normal(next_region.distance, disperse);
#ifdef VERBOSE
    cout << wait_time << "\n";
#endif
    if (wait_time < 0)
    {
        wait_time = 5;
    }

    if (visit_in_row > 1)
    {
        if (Random() < 0.9)
        {
            wait_time = wait_time / visit_in_row;
            // cout << "Visit in row: " << this->visit_in_row << " ,čas je skrátený na " << wait_time << "\n";
        }
    }

    this->road_time += wait_time;

    this->distance += this->distanceFromTime(wait_time);
    this->topTransPrice();
#ifdef VERBOSE
    cout << "Aktuálna vzdialenost je " << this->distance << " a TopTrans cena " << this->top_trans_cost << "\n";
#endif
    Wait(wait_time);
    this->current_region = next_region.region;
}

void Car::deliverPackage()
{
    double wait_time = Uniform(2.0, 5.0);
    Wait(wait_time);

    for (int i = 0; i < this->loaded_packages.size(); i++)
    {
        if (this->loaded_packages[i].region == this->current_region)
        {
            this->loaded_packages.erase(this->loaded_packages.begin() + i);
            break;
        }
    }

#ifdef VERBOSE
    cout << "Vykladanie trvalo: " << wait_time << "\n";
    cout << "Zostávajú balíčky: \n";
#endif
    for (int i = 0; i < this->loaded_packages.size(); i++)
    {
#ifdef VERBOSE
        cout << this->loaded_packages[i].region << " ";
#endif
    }
#ifdef VERBOSE
    cout << "\n";
#endif
}

void Car::chooseDistanceTable()
{
    if (this->current_region == "ZLK")
    {
        this->current_region_distancies = this->ZLK_distances;
    }

    else if (this->current_region == "MSK")
    {
        this->current_region_distancies = this->MSK_distances;
    }

    else if (this->current_region == "JHM")
    {
        this->current_region_distancies = this->JHM_distances;
    }

    else if (this->current_region == "OLK")
    {
        this->current_region_distancies = this->OLK_distances;
    }

    else if (this->current_region == "VYS")
    {
        this->current_region_distancies = this->VYS_distances;
    }

    else if (this->current_region == "JHC")
    {
        this->current_region_distancies = this->JHC_distances;
    }

    else if (this->current_region == "PLK")
    {
        this->current_region_distancies = this->PLK_distances;
    }

    else if (this->current_region == "KVK")
    {
        this->current_region_distancies = this->KVK_distances;
    }

    else if (this->current_region == "STC")
    {
        this->current_region_distancies = this->STC_distances;
    }

    else if (this->current_region == "Praha")
    {
        this->current_region_distancies = this->Praha_distances;
    }

    else if (this->current_region == "HKK")
    {
        this->current_region_distancies = this->HKK_distances;
    }

    else if (this->current_region == "PAK")
    {
        this->current_region_distancies = this->PAK_distances;
    }

    else if (this->current_region == "LBK")
    {
        this->current_region_distancies = this->LBK_distances;
    }

    else if (this->current_region == "ULK")
    {
        this->current_region_distancies = this->ULK_distances;
    }
}

void Car::loadPackage()
{
    double wait_time = Uniform(2.0, 5.0);
    Wait(wait_time);
    Package to_load = this->queue.back();
    this->queue.pop_back();
    this->loaded_packages.push_back(to_load);
#ifdef VERBOSE
    cout << "Nakladanie trvalo: " << wait_time << "\n";
#endif
}

void Car::loadDistances()
{
    this->loadZLKDistances();
    this->loadMSKDistances();
    this->loadJHMDistances();
    this->loadOLKDistances();
    this->loadVYSDistances();
    this->loadJHCDistances();
    this->loadPLKDistances();
    this->loadKVKDistances();
    this->loadSTCDistances();
    this->loadPrahaDistances();
    this->loadHKKDistances();
    this->loadPAKDistances();
    this->loadLBKDistances();
    this->loadULKDistances();
}

void Car::loadZLKDistances()
{

    int distances[14] = {30, 90, 90, 80, 150, 240, 240, 270, 180, 180, 150, 120, 210, 240};
    int mean[14] = {400, 400, 900, 400, 900, 900, 900, 900, 900, 100, 900, 400, 900, 100};

    for (int i = 0; i < 14; i++)
    {
        distance_to_region cell;
        this->ZLK_distances.push_back(cell);
        this->ZLK_distances[i].region = regions[i];
        this->ZLK_distances[i].distance = distances[i];
        this->ZLK_distances[i].mean = mean[i];
    }
}

void Car::loadMSKDistances()
{
    int distances[14] = {90, 90, 120, 90, 150, 270, 270, 300, 210, 210, 150, 150, 210, 270};
    int mean[14] = {400, 900, 900, 900, 400, 900, 900, 900, 900, 100, 900, 900, 900, 900};

    for (int i = 0; i < 14; i++)
    {
        distance_to_region cell;
        this->MSK_distances.push_back(cell);
        this->MSK_distances[i].region = regions[i];
        this->MSK_distances[i].distance = distances[i];
        this->MSK_distances[i].mean = mean[i];
    }
}
void Car::loadJHMDistances()
{

    int distances[14] = {90, 120, 30, 80, 120, 180, 180, 210, 120, 120, 120, 90, 180, 180};
    int mean[14] = {900, 900, 400, 900, 900, 900, 900, 900, 900, 100, 900, 900, 900, 900};

    for (int i = 0; i < 14; i++)
    {
        distance_to_region cell;
        this->JHM_distances.push_back(cell);
        this->JHM_distances[i].region = regions[i];
        this->JHM_distances[i].distance = distances[i];
        this->JHM_distances[i].mean = mean[i];
    }
}

void Car::loadOLKDistances()
{
    int distances[14] = {80, 90, 80, 40, 100, 210, 210, 240, 150, 150, 90, 90, 150, 210};
    int mean[14] = {400, 900, 900, 900, 900, 900, 900, 900, 900, 100, 900, 900, 900, 900};

    for (int i = 0; i < 14; i++)
    {
        distance_to_region cell;
        this->OLK_distances.push_back(cell);
        this->OLK_distances[i].region = regions[i];
        this->OLK_distances[i].distance = distances[i];
        this->OLK_distances[i].mean = mean[i];
    }
}

void Car::loadVYSDistances()
{
    int distances[14] = {150, 150, 120, 100, 40, 120, 150, 150, 120, 120, 120, 90, 150, 150};
    int mean[14] = {900, 400, 900, 900, 200, 900, 900, 900, 900, 100, 900, 900, 900, 900};

    for (int i = 0; i < 14; i++)
    {
        distance_to_region cell;
        this->VYS_distances.push_back(cell);
        this->VYS_distances[i].region = regions[i];
        this->VYS_distances[i].distance = distances[i];
        this->VYS_distances[i].mean = mean[i];
    }
}

void Car::loadJHCDistances()
{
    int distances[14] = {240, 270, 180, 210, 120, 40, 100, 150, 90, 90, 150, 150, 150, 150};
    int mean[14] = {900, 900, 900, 900, 900, 900, 900, 900, 900, 100, 900, 900, 900, 900};

    for (int i = 0; i < 14; i++)
    {
        distance_to_region cell;
        this->JHC_distances.push_back(cell);
        this->JHC_distances[i].region = regions[i];
        this->JHC_distances[i].distance = distances[i];
        this->JHC_distances[i].mean = mean[i];
    }
}

void Car::loadPLKDistances()
{
    int distances[14] = {240, 270, 180, 210, 150, 100, 40, 60, 60, 60, 150, 150, 150, 120};
    int mean[14] = {900, 900, 900, 900, 900, 900, 900, 900, 900, 100, 900, 900, 900, 900};

    for (int i = 0; i < 14; i++)
    {
        distance_to_region cell;
        this->PLK_distances.push_back(cell);
        this->PLK_distances[i].region = regions[i];
        this->PLK_distances[i].distance = distances[i];
        this->PLK_distances[i].mean = mean[i];
    }
}

void Car::loadKVKDistances()
{

    int distances[14] = {270, 300, 210, 240, 150, 150, 60, 30, 90, 90, 150, 150, 150, 120};
    int mean[14] = {900, 900, 900, 900, 900, 900, 900, 400, 900, 100, 900, 900, 900, 900};

    for (int i = 0; i < 14; i++)
    {
        distance_to_region cell;
        this->KVK_distances.push_back(cell);
        this->KVK_distances[i].region = regions[i];
        this->KVK_distances[i].distance = distances[i];
        this->KVK_distances[i].mean = mean[i];
    }
}

void Car::loadSTCDistances()
{

    int distances[14] = {180, 210, 120, 150, 120, 90, 60, 90, 40, 20, 90, 90, 90, 60};
    int mean[14] = {900, 900, 900, 900, 900, 900, 900, 900, 900, 400, 900, 900, 900, 900};

    for (int i = 0; i < 14; i++)
    {
        distance_to_region cell;
        this->STC_distances.push_back(cell);
        this->STC_distances[i].region = regions[i];
        this->STC_distances[i].distance = distances[i];
        this->STC_distances[i].mean = mean[i];
    }
}

void Car::loadPrahaDistances()
{
    int distances[14] = {180, 210, 120, 150, 120, 90, 60, 90, 20, 15, 90, 90, 90, 60};
    int mean[14] = {100, 100, 100, 100, 100, 100, 100, 100, 400, 100, 900, 900, 900, 900};

    for (int i = 0; i < 14; i++)
    {
        distance_to_region cell;
        this->Praha_distances.push_back(cell);
        this->Praha_distances[i].region = regions[i];
        this->Praha_distances[i].distance = distances[i];
        this->Praha_distances[i].mean = mean[i];
    }
}

void Car::loadHKKDistances()
{
    int distances[14] = {150, 150, 120, 90, 120, 150, 150, 150, 90, 90, 40, 50, 60, 120};
    int mean[14] = {900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 400, 400, 900, 900};

    for (int i = 0; i < 14; i++)
    {
        distance_to_region cell;
        this->HKK_distances.push_back(cell);
        this->HKK_distances[i].region = regions[i];
        this->HKK_distances[i].distance = distances[i];
        this->HKK_distances[i].mean = mean[i];
    }
}

void Car::loadPAKDistances()
{
    int distances[14] = {120, 150, 90, 90, 90, 150, 150, 150, 90, 90, 50, 40, 90, 120};
    int mean[14] = {400, 900, 900, 900, 900, 900, 900, 900, 900, 900, 400, 400, 900, 900};

    for (int i = 0; i < 14; i++)
    {
        distance_to_region cell;
        this->PAK_distances.push_back(cell);
        this->PAK_distances[i].region = regions[i];
        this->PAK_distances[i].distance = distances[i];
        this->PAK_distances[i].mean = mean[i];
    }
}

void Car::loadLBKDistances()
{
    int distances[14] = {210, 210, 180, 150, 150, 150, 150, 150, 90, 90, 60, 90, 40, 90};
    int mean[14] = {900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 400, 900};

    for (int i = 0; i < 14; i++)
    {
        distance_to_region cell;
        this->LBK_distances.push_back(cell);
        this->LBK_distances[i].region = regions[i];
        this->LBK_distances[i].distance = distances[i];
        this->LBK_distances[i].mean = mean[i];
    }
}

void Car::loadULKDistances()
{

    int distances[14] = {240, 270, 180, 210, 150, 150, 120, 120, 60, 60, 120, 120, 90, 40};
    int mean[14] = {100, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 400};

    for (int i = 0; i < 14; i++)
    {
        distance_to_region cell;
        this->ULK_distances.push_back(cell);
        this->ULK_distances[i].region = regions[i];
        this->ULK_distances[i].distance = distances[i];
        this->ULK_distances[i].mean = mean[i];
    }
}
