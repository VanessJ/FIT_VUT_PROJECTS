using System;
using project.DAL.Entities;

using Microsoft.EntityFrameworkCore;

namespace project.Common.Tests.Seeds
{
    public static class CarSeeds
    {
     
        
        public static readonly CarEntity CarEntity1 = new()
        {   
            Id = Guid.Parse("C5DE45D7-64A0-4E83-AC7F-BF5CFDFB0EeC"),
            Manufacturer = "Škoda",
            Type =  "Octavia",
            NumberOfSeats = 5,
            ImageUrl = "ff",
            DateOfRegistration = default,
            OwnerId = UserSeeds.User1.Id
        };

        public static readonly CarEntity CarEntity2 = new()
        {
            Id = Guid.Parse("06a8a2cf-ea03-4095-a3e4-aa0291fe9c75"),
            Manufacturer = "Škoda",
            Type = "Superb",
            NumberOfSeats = 5,
            ImageUrl = "ff",
            DateOfRegistration = default,
            OwnerId = UserSeeds.User2.Id,
        };
        
        static CarSeeds()
        {
            CarEntity1.Drives?.Add(DriverSeeds.DriveEntityBrnoBratislava);
            CarEntity2.Drives?.Add(DriverSeeds.DriveEntityPrahaBrno);
        }

        public static void Seed(this ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<CarEntity>().HasData(
                CarEntity1 with { Drives = Array.Empty<DriveEntity>() },
                CarEntity2 with { Drives = Array.Empty<DriveEntity>() }
            );
        }
    }
}

