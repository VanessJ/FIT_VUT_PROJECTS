using System;
using System.Threading.Tasks;
using project.DAL.Entities;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Metadata;
using project.DAL.Repositories;

namespace project.DAL.UnitOfWork
{

    public interface IUnitOfWork : IAsyncDisposable
    {

        CarRepository<CarEntity> GetCarRepository<TEntity>() where TEntity : class, IEntity;
        UserRepository<UserEntity> GetUserRepository<TEntity>() where TEntity : class, IEntity;
        DriveRepository<DriveEntity> GetDriveRepository<TEntity>() where TEntity : class, IEntity;
        IRepository<TEntity> GetRepository<TEntity>() where TEntity : class, IEntity;
        Task CommitAsync();
    }
}