using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using project.DAL.Entities;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Metadata;
using project.DAL.Repositories;

namespace project.DAL.UnitOfWork
{
    // UoW inherits from IUoW
    public sealed class UnitOfWork : IUnitOfWork
    {
        private readonly DbContext _dbContext;

        // unit of work needs DB context, saves it or throw an exception
        public UnitOfWork(DbContext dbContext) => _dbContext = dbContext ?? throw new ArgumentNullException(nameof(dbContext));
        
        // create repository with DB context, generics constraint must be a class 
        public CarRepository<CarEntity> GetCarRepository<TEntity>() where TEntity : class, IEntity => new CarRepository<CarEntity>(_dbContext);
        
        public UserRepository<UserEntity> GetUserRepository<TEntity>() where TEntity : class, IEntity => new UserRepository<UserEntity>(_dbContext);
        
        public DriveRepository<DriveEntity> GetDriveRepository<TEntity>() where TEntity : class, IEntity => new DriveRepository<DriveEntity>(_dbContext);
        public IRepository<TEntity> GetRepository<TEntity>() where TEntity : class, IEntity => new Repository<TEntity>(_dbContext);

        // commit to the database
        public async Task CommitAsync() => await _dbContext.SaveChangesAsync();
        
        // end database connection
        public async ValueTask DisposeAsync() => await _dbContext.DisposeAsync();
    }
}