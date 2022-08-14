
using project.DAL;
using Microsoft.EntityFrameworkCore;

namespace project.Common.Tests
{

    public class DbContextSqLiteTestingFactory : IDbContextFactory<CarPoolingDbContext>
    {
        private readonly string _databaseName;
        private readonly bool _seedTestingData;

        public DbContextSqLiteTestingFactory(string databaseName, bool seedTestingData = false)
        {
            _databaseName = databaseName;
            _seedTestingData = seedTestingData;
        }

        public CarPoolingDbContext CreateDbContext()
        {
            DbContextOptionsBuilder<CarPoolingDbContext> builder = new();
            
            builder.UseSqlite($"Data Source={_databaseName};Cache=Shared");

            builder.LogTo(System.Console.WriteLine); //Enable in case you want to see tests details, enabled may cause some inconsistencies in tests
            builder.EnableSensitiveDataLogging();

            return new CarPoolingTestingDbContext(builder.Options, _seedTestingData);
        }
    }
}