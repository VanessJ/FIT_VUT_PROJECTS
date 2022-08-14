#include <iostream>
#include "package.hpp"
#include "simlib.h"

#define REDUCED_DELIVERY false

using namespace std;

Package::Package()
{
    srand(time(NULL));
    // this->region = "ZLK";
    int random_region;
    if (REDUCED_DELIVERY)
    {
        random_region = Uniform(0, 7);
        this->region = this->reduced_delivery[random_region];
    }
    else
    {
        int random_region = Uniform(0, 14);
        this->region = this->regions[random_region];
    }
#ifdef VERBOSE
    cout << this->region << "\n";
#endif
}
