using System;
using Microsoft.EntityFrameworkCore;

namespace project.DAL.UnitOfWork
{

    public class UnitOfWorkFactory : IUnitOfWorkFactory
    {
        private readonly IDbContextFactory<CarPoolingDbContext> _dbContextFactory;

        public UnitOfWorkFactory(IDbContextFactory<CarPoolingDbContext> dbContextFactory)
        {
            _dbContextFactory = dbContextFactory;
        }
        
        // creates UoW
        public IUnitOfWork Create() => new UnitOfWork(_dbContextFactory.CreateDbContext());
    }
}