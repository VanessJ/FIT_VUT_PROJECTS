using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using AutoMapper;
using project.DAL.Entities;
using Microsoft.EntityFrameworkCore;

namespace project.DAL.UnitOfWork
{

    public interface IRepository<TEntity> where TEntity : class, IEntity
    {
        IQueryable<TEntity> Get();
        void Delete(Guid entityId);

        Task<TEntity> InsertOrUpdateAsync<TModel>(
            TModel model,
            IMapper mapper,
            CancellationToken cancellationToken = default) where TModel : class;
    }
}