using System;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using project.Common.Tests;
using project.Common.Tests.Seeds;
using project.DAL.Entities;
using project.DAL.Tests;
using Xunit;
using Xunit.Abstractions;

namespace project.DAL.Tests{

    public class DbContextCarTests : DbContextTestsBase
    {
        public DbContextCarTests(ITestOutputHelper output) : base(output)
        {
        }

        [Fact]
        public async Task AddNew_Car_Persisted()
        {
            // Arrange
            CarEntity entity = new()
            {

                Id = Guid.Parse("C5DE45D7-64A0-4E8D-AC7F-BF5CFDFB0EFC"),
                Manufacturer = "Ford",
                Type = "Focus",
                NumberOfSeats = 4,
                ImageUrl = "ff",
                //Owner = UserSeeds.User1
                //OwnerId = UserSeeds.User1.Id
            };
            // Act
            CarPoolingDbContextSUT.Cars.Add(entity);
            await CarPoolingDbContextSUT.SaveChangesAsync();
            

            // Assert
            await using var dbx = await DbContextFactory.CreateDbContextAsync();
            var actualEntities = await dbx.Cars
                .SingleAsync(i => i.Id == entity.Id);
            DeepAssert.Equal(entity, actualEntities);

        }


        [Fact]
        public async Task GetAll_Cars_ContainsSeededCar()
        {
            //Act
            var entities = await CarPoolingDbContextSUT.Cars.ToArrayAsync();

            //Assert
            Assert.Contains(CarSeeds.CarEntity1.Id, entities.Select(x => x.Id));
        }

        [Fact]
        public async Task GetById_Car()
        {
            //Act
            var entity = await CarPoolingDbContextSUT.Cars
                .SingleAsync(i => i.Id == CarSeeds.CarEntity1.Id);
            Fix(entity, CarSeeds.CarEntity1);


            //Assert
            DeepAssert.Equal(CarSeeds.CarEntity1, entity);
        }

        [Fact]
        public async Task Delete_Cars_Car1Deleted()
        {
            //Arrange
            var entityBase = CarSeeds.CarEntity1;

            //Act
            CarPoolingDbContextSUT.Cars.Remove(entityBase);
            await CarPoolingDbContextSUT.SaveChangesAsync();

            //Assert
            Assert.False(await CarPoolingDbContextSUT.Cars.AnyAsync(i => i.Id == entityBase.Id));
        }

        [Fact]
        public async Task DeleteById_Cars_Car1Deleted()
        {
            //Arrange
            var entityBase = CarSeeds.CarEntity1;

            //Act
            CarPoolingDbContextSUT.Remove(
                CarPoolingDbContextSUT.Cars.Include(x => x.Drives).Single(i => i.Id == entityBase.Id));
            await CarPoolingDbContextSUT.SaveChangesAsync();

            //Assert
            Assert.False(await CarPoolingDbContextSUT.Cars.AnyAsync(i => i.Id == entityBase.Id));
        }


        private void Fix(CarEntity actuall, CarEntity notActuall)
        {
            actuall.Drives = notActuall.Drives;
        }

    }
}
