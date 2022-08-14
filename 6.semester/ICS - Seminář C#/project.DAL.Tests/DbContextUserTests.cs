using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using project.Common.Tests;
using project.Common.Tests.Seeds;
using project.DAL.Entities;
using project.DAL.Tests;
using Xunit;
using Xunit.Abstractions;

namespace project.DAL.Tests
{

    public class DbContextUserTests : DbContextTestsBase
    {
        public DbContextUserTests(ITestOutputHelper output) : base(output)
        {
        }

        [Fact]
        public async Task AddNew_User_Persisted()
        {
            // Arrange
            UserEntity entity = new()
            {

                Id = Guid.Parse("C5DE45D7-64A0-4E8D-AC7F-BF5CFDFB0EFC"),
                FirstName = "Pan",
                LastName = "Y",
                Age = 33,
                //IsOnJourney = false
            };

            // Act
            CarPoolingDbContextSUT.Users.Add(entity);
            await CarPoolingDbContextSUT.SaveChangesAsync();


            // Assert
            await using var dbx = await DbContextFactory.CreateDbContextAsync();
            var actualEntities = await dbx.Users.SingleAsync(i => i.Id == entity.Id);
            DeepAssert.Equal(entity, actualEntities);

        }
    }
}