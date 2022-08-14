using AutoMapper;
using Microsoft.EntityFrameworkCore;
using project.BL.Models;
using project.DAL.Entities;
using project.DAL.UnitOfWork;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace project.BL
{
    public class CRUDFacade<TEntity, TListModel, TDetailModel>
        where TEntity : class, IEntity
        where TListModel : IModel
        where TDetailModel : class, IModel
    {
        private readonly IMapper _mapper;
        private readonly IUnitOfWorkFactory _unitOfWorkFactory;

        protected CRUDFacade(IUnitOfWorkFactory unitOfWorkFactory, IMapper mapper)
        {
            _unitOfWorkFactory = unitOfWorkFactory;
            _mapper = mapper;
        }

        public async Task DeleteAsync(TDetailModel model) => await this.DeleteAsync(model.Id);

        public async Task DeleteAsync(Guid id)
        {
            await using var uow = _unitOfWorkFactory.Create();
            uow.GetRepository<TEntity>().Delete(id);
            await uow.CommitAsync().ConfigureAwait(false);
        }

        public async Task<TDetailModel?> GetAsync(Guid id)
        {
            await using var uow = _unitOfWorkFactory.Create();
            var query = uow
                .GetRepository<TEntity>()
                .Get()
                .Where(e => e.Id == id);
            return await _mapper.ProjectTo<TDetailModel>(query).SingleOrDefaultAsync().ConfigureAwait(false);
        }

        public async Task<IEnumerable<TListModel>> GetAsync()
        {
            await using var uow = _unitOfWorkFactory.Create();
            var query = uow
                .GetRepository<TEntity>()
                .Get();
            return await _mapper.ProjectTo<TListModel>(query).ToArrayAsync().ConfigureAwait(false);
        }

        public async Task<TDetailModel> SaveAsync(TDetailModel model)
        {
            await using var uow = _unitOfWorkFactory.Create();

            var entity = uow
                .GetRepository<TEntity>();

            var entity2 = await entity.InsertOrUpdateAsync(model, _mapper)
                .ConfigureAwait(false);
            await uow.CommitAsync();
            

            return (await GetAsync(entity2.Id).ConfigureAwait(false))!;
        }
    }
}
