using BL.Tests;
using Microsoft.EntityFrameworkCore;
using project.BL.Facade;
using project.BL.Models;
using project.Common.Tests;
using project.Common.Tests.Seeds;
using project.DAL.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xunit;
using Xunit.Abstractions;

namespace project.BL.Tests
{
    public class UserFacadeTests : CRUDFacadeTestsBase
    {
        private readonly UserFacade _userFacadeSUT;
        private readonly DriveFacade _driveFacadeSUT;

        public UserFacadeTests(ITestOutputHelper output) : base(output)
        {
            _userFacadeSUT = new UserFacade(UnitOfWorkFactory, Mapper);
            _driveFacadeSUT = new DriveFacade(UnitOfWorkFactory, Mapper);
        }

        [Fact]
        public async Task CreateUser()
        {
            //Arrange
            var model = new DetailUserModel
            ()
            {
                FirstName = "Pepa",
                LastName = "Pepik",
                Age = 18,
                ImageUrl = "aaa"
            };

            //Act
            var returnedModel = await _userFacadeSUT.SaveAsync(model);
            FixIdsAndLists(model, returnedModel);

            //Assert
            Assert.Equal(model, returnedModel);
        }

        [Fact]
        public async Task DeleteUser()
        {
            //Arrange
            await _userFacadeSUT.DeleteAsync(UserSeeds.User1.Id);

            var model = await _userFacadeSUT.GetAsync(UserSeeds.User1.Id);

            Assert.Null(model);

        }

        [Fact]
        public async Task DummyTest()
        {
            //Arrange
            var user = new DetailUserModel()
            {
                Age = 11,
                FirstName = "a",
                ImageUrl = "aaa",
                LastName = "aa"
            };
            var returned = await _userFacadeSUT.SaveAsync(user);
            var drive = await _driveFacadeSUT.GetAsync();
            await _driveFacadeSUT.AddDriverToDrive(DriverSeeds.DriveEntityBrnoBratislava.Id, returned.Id);
            var test = _driveFacadeSUT.GetAsync(DriverSeeds.DriveEntityBrnoBratislava.Id);

            await _userFacadeSUT.DeleteAsync(returned);


        }

        [Fact]
        public async Task DeleteNonExistentUser()
        {
            //Arrange
            try
            {
                await _userFacadeSUT.DeleteAsync(Guid.Empty);
                Assert.True(false, "Assert Fail");

            }
            catch (Exception ex) { }
        }

        [Fact]
        public async Task GetNonExistentUser()
        {
            //Arrange
            var model = await _userFacadeSUT.GetAsync(Guid.Empty);

            Assert.Null(model);
        }


        [Fact]
        public async Task GetByIdFromSeededDoesNotThrowAndEqualsSeeded()
        {
            //Arrange
            var detailModel = Mapper.Map<DetailUserModel>(UserSeeds.User1);

            //Act
            var returnedModel = await _userFacadeSUT.GetAsync(detailModel.Id);
            FixIdsAndLists(detailModel, returnedModel, false);

            //Assert
            DeepAssert.Equal(detailModel, returnedModel);
        }

        [Fact]
        public async Task DeleteFromSeededDoesNotThrow()
        {
            //Arrange
            var detailModel = Mapper.Map<DetailUserModel>(UserSeeds.User1);

            //Act & Assert
            await _userFacadeSUT.DeleteAsync(detailModel);
        }

        [Fact]
        public async Task Update()
        {
            //Arrange
            var detailModel = await _userFacadeSUT.GetAsync(UserSeeds.User1.Id);
            detailModel.FirstName = "Changed user name";
            //Workaround for exception with carId in drivesAsDriver being already tracked
            detailModel = await _userFacadeSUT.SaveAsync(detailModel);

            var returnedModel = await _userFacadeSUT.GetAsync(detailModel.Id);

            DeepAssert.Equal(detailModel, returnedModel);
            //Act & Assert
        }


        [Fact]
        public async Task DeleteById_FromSeeded_DoesNotThrow()
        {
            //Arrange & Act & Assert
            await _userFacadeSUT.DeleteAsync(UserSeeds.User1.Id);
        }


        private static void FixIdsAndLists(DetailUserModel expectedModel, DetailUserModel returnedModel, bool fixId = true)
        {
            if (fixId)
            {
                returnedModel.Id = expectedModel.Id;
            }

        }
    }
}

