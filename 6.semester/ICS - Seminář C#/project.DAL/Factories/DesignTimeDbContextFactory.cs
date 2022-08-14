using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;
// aby fungovaly migrace tak potrebujeme bezparametrovy konsturktor na db kontextu nebo tuto implementaci design db factory

namespace project.DAL.Factories
{
    /// <summary>
    /// EF Core CLI migration generation uses this DbContext to create model and migration
    /// </summary>
    public class DesignTimeDbContextFactory : IDesignTimeDbContextFactory<CarPoolingDbContext>
    {
        public CarPoolingDbContext CreateDbContext(string[] args)
        {
            DbContextOptionsBuilder<CarPoolingDbContext> builder = new();
            builder.UseSqlServer(
                    @"Data Source=(LocalDB)\MSSQLLocalDB;
                Initial Catalog = CookBook;
                MultipleActiveResultSets = True;
                Integrated Security = True; ");

            return new CarPoolingDbContext(builder.Options);
        }
    }
}