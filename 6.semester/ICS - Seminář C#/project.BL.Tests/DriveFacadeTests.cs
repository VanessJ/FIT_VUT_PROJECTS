using BL.Tests;
using Microsoft.EntityFrameworkCore;
using project.BL.Facade;
using project.BL.Models;
using project.Common.Tests;
using project.Common.Tests.Seeds;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xunit;
using Xunit.Abstractions;

namespace project.BL.Tests
{
    public class DriveFacadeTests : CRUDFacadeTestsBase
    {
        private readonly DriveFacade _driveFacadeSUT;
        private readonly UserFacade _userFacadeSUT;

        public DriveFacadeTests(ITestOutputHelper output) : base(output)
        {
            _driveFacadeSUT = new DriveFacade(UnitOfWorkFactory, Mapper);
            _userFacadeSUT = new UserFacade(UnitOfWorkFactory, Mapper);
        }

        [Fact]
        public async Task CreateDrive()
        {
            var model = new DetailDriveModel()
            {
                JourneyBeginning = "Brno",
                Destination = "Praha",
                DriverId = UserSeeds.User1.Id,
                CarId = CarSeeds.CarEntity2.Id,
                ArrivalTime = DateTime.Now.AddDays(1),
                DepartureTime = DateTime.Now

            };

            var returned = await _driveFacadeSUT.SaveAsync(model);

            FixIds(model, returned);
            model.Passengers = returned.Passengers;
            Assert.Equal(model, returned);
        }

        [Fact]
        public async Task AddPassengerToDrive()
        {
            await _driveFacadeSUT.AddPassengerToDrive(DriverSeeds.DriveEntityBrnoBratislava.Id, UserSeeds.User1.Id);
            var drive = _driveFacadeSUT.GetDrive(DriverSeeds.DriveEntityBrnoBratislava.Id);

            Assert.Equal(drive.Passengers.Count, 1);
        }

        [Fact]
        public async Task AddDriverToDrive()
        {
            await _driveFacadeSUT.AddDriverToDrive(DriverSeeds.DriveEntityBrnoBratislava.Id, UserSeeds.User1.Id);
            var drive = _driveFacadeSUT.GetDrive(DriverSeeds.DriveEntityBrnoBratislava.Id);

            Assert.Equal(drive.DriverId, UserSeeds.User1.Id);

        }

        [Fact]
        public async Task RemoveDriverWithDrive()
        {
            await _driveFacadeSUT.AddDriverToDrive(DriverSeeds.DriveEntityBrnoBratislava.Id, UserSeeds.User1.Id);
            var drive = _driveFacadeSUT.GetDrive(DriverSeeds.DriveEntityBrnoBratislava.Id);
            await _userFacadeSUT.DeleteAsync(UserSeeds.User1.Id);

            Assert.Equal(default, _driveFacadeSUT.GetDrive(DriverSeeds.DriveEntityBrnoBratislava.Id));
        }

        [Fact]
        public async Task GetByIdNonExistent()
        {
            var drive = await _driveFacadeSUT.GetAsync(new Guid());

            Assert.Null(drive);
        }

        [Fact]
        public async Task GetDrivesByDriver()
        {

            var drives = _driveFacadeSUT.GetDrivesWithDriver(UserSeeds.User1.Id);

            Assert.NotNull(drives);

        }

        [Fact]
        public async Task GetDrivesByCar()
        {
            var drives = _driveFacadeSUT.GetDrivesWithCar(CarSeeds.CarEntity1.Id);

            Assert.NotNull(drives);
        }

        [Fact]
        public async Task Filter()
        {
            var drives = await _driveFacadeSUT.Filter(DateTime.MinValue, true, "Praha", "Brno");
            Assert.NotEmpty(drives);
        }

        [Fact]
        public async Task NumberOfSeats()
        {
            await _driveFacadeSUT.AddPassengerToDrive(DriverSeeds.DriveEntityBrnoBratislava.Id, UserSeeds.User1.Id);
            int numberOfSeats = await _driveFacadeSUT.NumberOfAvaliableSeats(DriverSeeds.DriveEntityBrnoBratislava.Id);
            
            Assert.Equal(numberOfSeats, 4);
        }

        [Fact]
        public async Task GetAllDrivesUserIsNotIn()
        {
            await _driveFacadeSUT.AddPassengerToDrive(DriverSeeds.DriveEntityBrnoBratislava.Id, UserSeeds.User2.Id);

            var test = await _driveFacadeSUT.GetAllDrivesUserIsNotIn(UserSeeds.User1.Id);

            Assert.NotEmpty(test);
        }

        [Fact]
        public async Task GetAllDrivesWithPassenger()
        {
            await _driveFacadeSUT.AddPassengerToDrive(DriverSeeds.DriveEntityBrnoBratislava.Id, UserSeeds.User1.Id);

            var test = _driveFacadeSUT.GetAllDrivesWhereUserIsPassenger(UserSeeds.User1.Id);

            Assert.NotNull(test);
        }

        [Fact]
        public async Task IsUserInDriveAtTheMoment()
        {
            await _driveFacadeSUT.AddPassengerToDrive(DriverSeeds.DriveEntityBrnoBratislava.Id, UserSeeds.User1.Id);

            Assert.False(await _driveFacadeSUT.IsUserInDrive(UserSeeds.User1.Id, DriverSeeds.DriveEntityBrnoBratislava.Id));
        }

        [Fact]
        public async Task RemoveUserFromRide()
        {
            await _driveFacadeSUT.RemovePassengerFromDrive(DriverSeeds.DriveEntityPrahaBrno.Id, UserSeeds.User1.Id);

            var test = _driveFacadeSUT.GetAllDrivesWhereUserIsPassenger(UserSeeds.User1.Id);

            Assert.Empty(test);
        }

        private static void FixIds(DetailDriveModel expectedModel, DetailDriveModel returnedModel)
        {
            returnedModel.Id = expectedModel.Id;
            returnedModel.Car = expectedModel.Car;
            returnedModel.Driver = expectedModel.Driver;

        }
    }
}
