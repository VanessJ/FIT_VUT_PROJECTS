using System;
using System.Linq;
using System.Linq.Expressions;
using System.Threading;
using System.Threading.Tasks;
using AutoMapper;
using AutoMapper.EntityFrameworkCore;
using project.DAL.Entities;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;
using project.DAL.UnitOfWork;

namespace project.DAL.Repositories
{

    public class UserRepository<TEntity> : IRepository<TEntity> where TEntity : class, IEntity
    {
        private readonly DbSet<TEntity> _dbSet;
        private readonly IModel _model;

        public UserRepository(DbContext dbContext)
        {
            _dbSet = dbContext.Set<TEntity>();
            _model = dbContext.Model;
        }
        
        // get repository
        public IQueryable<TEntity> Get() => _dbSet;

        public async Task<TEntity> InsertOrUpdateAsync<TModel>(
            TModel model,
            IMapper mapper,
            CancellationToken cancellationToken = default) where TModel : class
        {
            await _dbSet.PreLoadChangeTracker(mapper.Map<TEntity>(model).Id, _model, cancellationToken);

            return await _dbSet.Persist(mapper).InsertOrUpdateAsync(model, cancellationToken);
        }
        
        // deletes element
        public void Delete(Guid entityId) => _dbSet.Remove(_dbSet.Single(i => i.Id == entityId));
    }
}