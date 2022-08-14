using System;
using System.Threading.Tasks;
using System.Collections.Generic;
using project.DAL.Entities;
using Microsoft.EntityFrameworkCore;
using project.Common.Tests.Seeds;
using Xunit;
using Xunit.Abstractions;

namespace project.Common.Tests.Seeds
{

    public static class DriverSeeds
    {

        public static readonly DriveEntity DriveEntityPrahaBrno = new()
        {
            Id = Guid.Parse("5DCA4CEA-B8A8-4C86-A0B3-FFB78FBA1A09"),
            JourneyBeginning = "Praha",
            Destination = "Brno",
            DepartureTime = new DateTime(2022, 1, 24, 9, 0, 0),
            ArrivalTime = new DateTime(2022, 1, 24, 11, 0, 0),
            IsFull = true,
            //CarId = CarSeeds.CarEntity2.Id,
            DriverId = UserSeeds.User2.Id,
            CarId = CarSeeds.CarEntity2.Id



        };

        public static readonly DriveEntity DriveEntityBrnoBratislava = new()
        {
            Id = Guid.Parse("0953F3CE-7B1A-48C1-9796-D2BAC7F67868"),
            JourneyBeginning = "Brno",
            Destination = "Bratislava",
            DepartureTime = new DateTime(2022, 1, 26, 12, 0, 0),
            ArrivalTime = new DateTime(2022, 1, 26, 14, 30, 0),
            IsFull = false,
            //CarId = CarSeeds.CarEntity1.Id,
            DriverId = UserSeeds.User1.Id,
            CarId = CarSeeds.CarEntity1.Id,


        };

        static DriverSeeds()
        {
            DriveEntityBrnoBratislava.Passengers?.Add(UserSeeds.User2);
            DriveEntityPrahaBrno.Passengers?.Add(UserSeeds.User1);
            
        }


        public static void Seed(this ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<DriveEntity>().HasData(

                DriveEntityBrnoBratislava with { Passengers = Array.Empty<UserEntity>() },
                DriveEntityPrahaBrno with { Passengers = Array.Empty<UserEntity>() }
            );
        }
    }
}