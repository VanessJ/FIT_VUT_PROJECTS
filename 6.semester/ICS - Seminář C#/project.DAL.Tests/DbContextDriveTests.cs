using System;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using project.Common.Tests;
using project.Common.Tests.Seeds;
using project.DAL.Entities;
using Xunit;
using Xunit.Abstractions;

namespace project.DAL.Tests
{

    public class DbContextDriveTests : DbContextTestsBase
    {
        public DbContextDriveTests(ITestOutputHelper output) : base(output)
        {
        }

        [Fact]
        public async Task AddNew_DriveWithoutDriverAndCar_Persisted()
        {
            DriveEntity entity = new()
            {
                JourneyBeginning = "Brno",
                Destination = "Ostrava",
                DepartureTime = new DateTime(2022, 02, 02, 10, 0, 0),
                ArrivalTime = new DateTime(2022, 02, 02, 12, 0, 0),
                IsFull = true
            };

            CarPoolingDbContextSUT.Add(entity);
            await CarPoolingDbContextSUT.SaveChangesAsync();

            await using var dbx = await DbContextFactory.CreateDbContextAsync();
            var actualEntity = await dbx.Drives
                .SingleAsync(i => i.Id == entity.Id);
            DeepAssert.Equal(entity, actualEntity);
        }

        [Fact]
        public async Task AddNew_DriveWithDriveAndCar_Persisted()
        {
            DriveEntity entity = new()
            {
                JourneyBeginning = "Vienna",
                Destination = "Bratislava",
                DepartureTime = new DateTime(2022, 04, 02, 10, 0, 0),
                ArrivalTime = new DateTime(2022, 04, 02, 11, 30, 0),
                IsFull = false,
                //DriverId = UserSeeds.User1.Id,
                //Driver = UserSeeds.User1,
                //CarId = CarSeeds.CarEntity1.Id,
                //Car = CarSeeds.CarEntity1
            };
            
            CarPoolingDbContextSUT.Add(entity);
            await CarPoolingDbContextSUT.SaveChangesAsync();
            
            await using var dbx = await DbContextFactory.CreateDbContextAsync();
            var actualEntity = await dbx.Drives
                .SingleAsync(i => i.Id == entity.Id);
            DeepAssert.Equal(entity, actualEntity);
            
        }

        [Fact]
        public async Task Update_Drive_Persisted()
        {
            var baseEntity = DriverSeeds.DriveEntityBrnoBratislava;
            var entity = baseEntity with
            {
                Destination = baseEntity.Destination + "Updated",
            };
            CarPoolingDbContextSUT.Update(entity);
            await CarPoolingDbContextSUT.SaveChangesAsync();

            await using var dbx = await DbContextFactory.CreateDbContextAsync();
            var actualEntity = await dbx.Drives.SingleAsync(i => i.Id == entity.Id);
            DeepAssert.Equal(entity, actualEntity);
        }
        

        [Fact]
        public async Task GetById_Drive()
        {
            var entity = await CarPoolingDbContextSUT.Drives
                .SingleAsync((i => i.Id == DriverSeeds.DriveEntityPrahaBrno.Id));
            
            DeepAssert.Equal(DriverSeeds.DriveEntityPrahaBrno.Id, entity.Id);
        }
        
        [Fact]
        public async Task DeleteById_Drive_Deleted()
        {
            //Arrange
            var baseEntity = DriverSeeds.DriveEntityBrnoBratislava;

            //Act
            CarPoolingDbContextSUT.Remove(
                CarPoolingDbContextSUT.Drives.Single(i => i.Id == baseEntity.Id));
            await CarPoolingDbContextSUT.SaveChangesAsync();

            //Assert
            Assert.False(await CarPoolingDbContextSUT.Drives.AnyAsync(i => i.Id == baseEntity.Id));
        }
        
        
    }
}