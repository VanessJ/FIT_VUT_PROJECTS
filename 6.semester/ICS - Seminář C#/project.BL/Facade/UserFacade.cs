using AutoMapper;
using project.BL.Models;
using project.DAL.Entities;
using project.DAL.Repositories;
using project.DAL.UnitOfWork;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;

namespace project.BL.Facade
{
    public class UserFacade : CRUDFacade<UserEntity, ListUserModel, DetailUserModel>
    {
        private readonly DriveRepository<DriveEntity> _driveRepository;
        private readonly UserRepository<UserEntity> _userRepository;
        private readonly CarRepository<CarEntity> _carRepository;
        private readonly IMapper _mapper;
        public UserFacade(IUnitOfWorkFactory unitOfWorkFactory, IMapper mapper) : base(unitOfWorkFactory, mapper)
        {
            var uow = unitOfWorkFactory.Create();
            _driveRepository = uow.GetDriveRepository<DriveEntity>();
            _userRepository = uow.GetUserRepository<UserEntity>();
            _carRepository = uow.GetCarRepository<CarEntity>();

            _mapper = mapper;
        }

        public IQueryable<ListUserModel> GetPassengers(Guid driveId)
        {
            var drive= (_driveRepository.Get().Include(x => x.Passengers).FirstOrDefault(x => x.Id == driveId));

            List<ListUserModel> returned = new List<ListUserModel>();


            foreach(var passenger in drive.Passengers)
            {
                returned.Add(_mapper.Map<ListUserModel>(passenger));
            }

            return returned.AsQueryable();
        }

    }
}
