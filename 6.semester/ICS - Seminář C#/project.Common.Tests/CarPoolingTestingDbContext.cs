using project.DAL;
using Microsoft.EntityFrameworkCore;
using project.Common.Tests.Seeds;

namespace project.Common.Tests
{
    
    public class CarPoolingTestingDbContext : CarPoolingDbContext
    {
        private readonly bool _seedTestingData;

        public CarPoolingTestingDbContext(DbContextOptions contextOptions, bool seedTestingData = false)
            : base(contextOptions, seedDemoData:false)
        {
            _seedTestingData = seedTestingData;
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            if (_seedTestingData)
            {   
                UserSeeds.Seed(modelBuilder);
                DriverSeeds.Seed(modelBuilder);
                CarSeeds.Seed(modelBuilder);



            }
        }
    }
}