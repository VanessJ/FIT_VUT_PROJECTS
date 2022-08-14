using AutoMapper;
using project.Common.Tests;
using project.DAL.UnitOfWork;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xunit;
using Xunit.Abstractions;
using Microsoft.EntityFrameworkCore;
using project.DAL;
using AutoMapper.EquivalencyExpression;
using project.BL;

namespace BL.Tests
{
    public class CRUDFacadeTestsBase : IAsyncLifetime
    {
        protected CRUDFacadeTestsBase(ITestOutputHelper output)
        {
            XUnitTestOutputConverter converter = new(output);
            Console.SetOut(converter);

            // DbContextFactory = new DbContextTestingInMemoryFactory(GetType().Name, seedTestingData: true);
            // DbContextFactory = new DbContextLocalDBTestingFactory(GetType().FullName!, seedTestingData: true);
            DbContextFactory = new DbContextSqLiteTestingFactory(GetType().FullName!, seedTestingData: true);

            UnitOfWorkFactory = new UnitOfWorkFactory(DbContextFactory);

            var configuration = new MapperConfiguration(cfg =>
            {
                cfg.AddMaps(new[]
                {
                    typeof(BusinessLogic),
                });
                cfg.AddCollectionMappers();

                using var dbContext = DbContextFactory.CreateDbContext();
                cfg.UseEntityFrameworkCoreModel<CarPoolingDbContext>(dbContext.Model);
            }
            );
            Mapper = new Mapper(configuration);
            Mapper.ConfigurationProvider.AssertConfigurationIsValid();
        }

        protected IDbContextFactory<CarPoolingDbContext> DbContextFactory { get; }

        protected Mapper Mapper { get; }

        protected UnitOfWorkFactory UnitOfWorkFactory { get; }

        public async Task InitializeAsync()
        {
            await using var dbx = await DbContextFactory.CreateDbContextAsync();
            await dbx.Database.EnsureDeletedAsync();
            await dbx.Database.EnsureCreatedAsync();
        }

        public async Task DisposeAsync()
        {
            await using var dbx = await DbContextFactory.CreateDbContextAsync();
            await dbx.Database.EnsureDeletedAsync();
        }
    }
}
