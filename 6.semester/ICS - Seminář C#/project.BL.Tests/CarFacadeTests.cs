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
    public class CarFacadeTests : CRUDFacadeTestsBase
    {
        private readonly CarFacade _carFacadeSUT;

        public CarFacadeTests(ITestOutputHelper output) : base(output)
        {
            _carFacadeSUT = new CarFacade(UnitOfWorkFactory, Mapper);
        }

        [Fact]
        public async Task CreateModel()
        {
            //Arrange
            var model = new DetailCarModel
            ()
            {
                Manufacturer = "BMW",
                ImageUrl = "CCC",
                NumberOfSeats = 4,
                Type = "te",
                DateOfRegistration = DateTime.Now,
                OwnerId = UserSeeds.User2.Id
            };

            //Act
            var returnedModel = await _carFacadeSUT.SaveAsync(model);

            FixIds(model, returnedModel);
            //Assert
            Assert.Equal(model, returnedModel);
        }



        [Fact]
        public async Task SeedIsEqualToDb()
        {
            //Arrange
            var detailModel = Mapper.Map<DetailCarModel>(CarSeeds.CarEntity1);

            //Act
            var returnedModel = await _carFacadeSUT.GetAsync(detailModel.Id);
            FixIds(detailModel, returnedModel);

            //Assert
            DeepAssert.Equal(detailModel, returnedModel);
        }

        [Fact]
        public async Task DeleteFromSeeded()
        {
            //Arrange
            var detailModel = Mapper.Map<DetailCarModel>(CarSeeds.CarEntity1);

            //Act & Assert
            await _carFacadeSUT.DeleteAsync(detailModel);
        }

        [Fact]
        public async Task UpdateFromSeeded()
        {
            //Arrange
            var detailModel = Mapper.Map<DetailCarModel>(CarSeeds.CarEntity1);
            detailModel.Manufacturer = "Changed";

            //Act & Assert
            await _carFacadeSUT.SaveAsync(detailModel);
        }

        [Fact]
        public async Task UpdateManufacturerFromSeededCheckUpdated()
        {
            //Arrange
            //var detailModel = Mapper.Map<DetailCarModel>(CarSeeds.CarEntity1);
            var test1 = await _carFacadeSUT.GetAsync();
            var detailModel = Mapper.Map<DetailCarModel>(await _carFacadeSUT.GetAsync(CarSeeds.CarEntity2.Id));
            detailModel.Type = "Changed";

            //Act


            //Assert
            var returnedModel = await _carFacadeSUT.SaveAsync(detailModel);
            var test2 = await _carFacadeSUT.GetAsync();
            FixIds(detailModel, returnedModel);
            DeepAssert.Equal(detailModel, returnedModel);
        }


        [Fact]
        public async Task DeleteByIdFromSeeded()
        {
            //Arrange & Act & Assert
            await _carFacadeSUT.DeleteAsync(CarSeeds.CarEntity1.Id);
            Assert.Null(await _carFacadeSUT.GetAsync(CarSeeds.CarEntity1.Id));
        }

        private static void FixIds(DetailCarModel expectedModel, DetailCarModel returnedModel)
        {
            returnedModel.Id = expectedModel.Id;
            returnedModel.Owner = expectedModel.Owner;

        }
    }
}
