using Microsoft.EntityFrameworkCore;

namespace project.DAL.Factories
{
    public class SqlServerDbContextFactory : IDbContextFactory<CarPoolingDbContext>
    {
        private readonly string _connectionString;
        private readonly bool _seedDemoData;

        public SqlServerDbContextFactory(string connectionString, bool seedDemoData = false)
        {
            _connectionString = connectionString;
            _seedDemoData = seedDemoData;
        }

        public CarPoolingDbContext CreateDbContext()
        {
            var optionsBuilder = new DbContextOptionsBuilder<CarPoolingDbContext>();
            optionsBuilder.UseSqlServer(_connectionString);

            optionsBuilder.LogTo(System.Console.WriteLine); //Enable in case you want to see tests details, enabled may cause some inconsistencies in tests
            optionsBuilder.EnableSensitiveDataLogging();

            return new CarPoolingDbContext(optionsBuilder.Options, true);
        }
    }
}