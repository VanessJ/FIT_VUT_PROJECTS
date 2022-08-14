#pragma once

#include <string>

class Package
{
private:
    std::string reduced_delivery[7] = {"HKK", "MSK", "VYS", "JHM", "OLK",
                                       "ZLK", "PAK"};
    std::string regions[14] = {"HKK", "LBK", "PLK", "JHC", "MSK", "Praha", "VYS", "JHM", "OLK", "STC",
                               "ZLK", "KVK", "PAK", "ULK"};

public:
    std::string region;
    Package();
};
