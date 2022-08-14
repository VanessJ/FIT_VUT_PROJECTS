#pragma once

#include <string>
#include <vector>
#include <string>
#include "package.hpp"

struct distance_to_region
{
    std::string region;
    double distance;
    double mean;
};

class Car : public Process
{
public:
    void Behavior();
    Car();
    void SetQueue(std::vector<Package> q);
    bool InDepo();
    double GetEndTime();
    double GetTotalDistance();
    double GetDuration();
    double GetConsumption();
    double GetFuelCost();
    double getTopTransCost();
    double getDriverCost();

private:
    int capacity;
    std::vector<Package> queue;
    double start_time;
    double end_time;
    double duration;
    double road_time;
    double distance;
    double total_distance;
    double total_roadtime;
    double consumption;
    double fuel_cost;
    int speed;
    int visit_in_row;
    double top_trans_cost;
    std::string current_region;
    std::vector<distance_to_region> current_region_distancies;
    bool traveling;
    bool in_depo;

    void topTransPrice();
    double distanceFromTime(double time);
    void loadPackage();
    void deliverPackage();
    void loadDistances();
    void loadZLKDistances();
    void loadMSKDistances();
    void loadJHMDistances();
    void loadOLKDistances();
    void loadVYSDistances();
    void loadJHCDistances();
    void loadPLKDistances();
    void loadKVKDistances();
    void loadSTCDistances();
    void loadPrahaDistances();
    void loadHKKDistances();
    void loadPAKDistances();
    void loadLBKDistances();
    void loadULKDistances();
    void chooseDistanceTable();
    void travelToClosest();
    void returnToDepo();

    std::vector<Package> loaded_packages;
    std::vector<distance_to_region> HKK_distances;
    std::vector<distance_to_region> LBK_distances;
    std::vector<distance_to_region> PLK_distances;
    std::vector<distance_to_region> JHC_distances;
    std::vector<distance_to_region> MSK_distances;
    std::vector<distance_to_region> Praha_distances;
    std::vector<distance_to_region> VYS_distances;
    std::vector<distance_to_region> JHM_distances;
    std::vector<distance_to_region> OLK_distances;
    std::vector<distance_to_region> STC_distances;
    std::vector<distance_to_region> ZLK_distances;
    std::vector<distance_to_region> KVK_distances;
    std::vector<distance_to_region> PAK_distances;
    std::vector<distance_to_region> ULK_distances;
};
