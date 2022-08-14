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

namespace project.BL.Facade
{
    public class CarFacade : CRUDFacade<CarEntity, ListCarModel, DetailCarModel>
    {
        private readonly DriveRepository<DriveEntity> _driveRepository;
        private readonly UserRepository<UserEntity> _userRepository;
        private readonly CarRepository<CarEntity> _carRepository;
        private readonly IMapper _mapper;
        public CarFacade(IUnitOfWorkFactory unitOfWorkFactory, IMapper mapper) : base(unitOfWorkFactory, mapper)
        {
            var uow = unitOfWorkFactory.Create();
            _driveRepository = uow.GetDriveRepository<DriveEntity>();
            _userRepository = uow.GetUserRepository<UserEntity>();
            _carRepository = uow.GetCarRepository<CarEntity>();

            _mapper = mapper;
        }

        public async Task AddCarOwner(Guid userId, Guid carId)
        {
            var car = _carRepository.Get().FirstOrDefault(x => x.Id == carId);
            car.OwnerId = userId;

            var returned = await _carRepository.InsertOrUpdateAsync(car, _mapper);

        }

        public async Task RemoveCarOwner(Guid carId)
        {
            var car = _carRepository.Get().FirstOrDefault(x => x.Id == carId);
            car.Owner = null;
            car.OwnerId = Guid.Empty;

            await _carRepository.InsertOrUpdateAsync(car, _mapper);
        }

        public IQueryable<ListCarModel> GetCarsOfDriver(Guid ownerId)
        {
            return _mapper.ProjectTo<ListCarModel>(_carRepository.Get().Where(x => x.OwnerId == ownerId));
        }
    }
}
