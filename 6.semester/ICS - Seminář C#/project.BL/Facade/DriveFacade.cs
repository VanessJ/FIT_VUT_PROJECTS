using AutoMapper;
using project.BL.Models;
using project.DAL.Entities;
using project.DAL.Repositories;
using project.DAL.UnitOfWork;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace project.BL.Facade
{
    public class DriveFacade : CRUDFacade<DriveEntity, ListDriveModel, DetailDriveModel>
    {
        private readonly DriveRepository<DriveEntity> _driveRepository;
        private readonly UserRepository<UserEntity> _userRepository;
        private readonly CarRepository<CarEntity> _carRepository;
        private readonly IMapper _mapper;
        public DriveFacade(IUnitOfWorkFactory unitOfWorkFactory, IMapper mapper) : base(unitOfWorkFactory, mapper)
        {

            var uow = unitOfWorkFactory.Create();
            _driveRepository = uow.GetDriveRepository<DriveEntity>();
            _userRepository = uow.GetUserRepository<UserEntity>();
            _carRepository= uow.GetCarRepository<CarEntity>();
            
            _mapper = mapper;

        }

        public IQueryable<ListDriveModel> GetAllNotFullDrives()
        {
            return _mapper.ProjectTo<ListDriveModel>(_driveRepository.Get().Where(x => x.IsFull == false).AsQueryable());
        }

        public IQueryable<ListDriveModel> GetDrivesWithDriver(Guid driverId)
        {
            return _mapper.ProjectTo<ListDriveModel>(_driveRepository.Get().Where(x => x.DriverId == driverId));
        }

        public IQueryable<ListDriveModel> GetDrivesWithCar(Guid carId)
        {
            return _mapper.ProjectTo<ListDriveModel>(_driveRepository.Get().Where(x => x.CarId == carId));
        }

        public DetailDriveModel GetDrive(Guid id)
        {
            return _mapper.Map<DetailDriveModel>(_driveRepository.Get().FirstOrDefault(x => x.Id == id));
        }

        public async Task AddPassengerToDrive(Guid driveId, Guid userId)
        {
            var drive = _mapper.Map<DetailDriveModel>(_driveRepository.Get().FirstOrDefault(x => x.Id == driveId));
            drive.Car = _carRepository.Get().FirstOrDefault(x => x.Id == drive.CarId);
            var user = _userRepository.Get().FirstOrDefault(x => x.Id == userId);
            
            if(user != null && drive != null)
            {
                drive.Passengers?.Add(user);
                
                if(drive.Passengers.Count == drive.Car.NumberOfSeats)
                {
                    drive.IsFull = true;
                }
                else
                {
                    drive.IsFull = false;

                }

                await _driveRepository.InsertOrUpdateAsync(drive, _mapper);
                SaveAsync(drive);
                

            }
        }

        public async Task AddDriverToDrive(Guid driveId, Guid driverId)
        {
            var drive = _mapper.Map<DetailDriveModel>(_driveRepository.Get().FirstOrDefault(x => x.Id == driveId));
            var user = _userRepository.Get().FirstOrDefault(x => x.Id == driverId);
            if (user != null && drive != null)
            {
                drive.Driver = user;
                await _driveRepository.InsertOrUpdateAsync(drive, _mapper);
                await SaveAsync(drive);
            }
        }
        
        public async Task<int> NumberOfAvaliableSeats(Guid driveId)
        {
            var drive = _driveRepository.Get().FirstOrDefault(x => x.Id == driveId);
            var car = _carRepository.Get().FirstOrDefault(x => x.Id == drive.CarId);
            if (drive?.Passengers == null || car == default)
            {
                return -1;
            }
            return (car.NumberOfSeats - drive.Passengers.Count);
        } 

        public IQueryable<ListDriveModel> GetAllDrivesWhereUserIsPassenger(Guid userId)
        {
            return _mapper.ProjectTo<ListDriveModel>(_driveRepository.Get().ToList().Where(x => x.Passengers.Any(y => y.Id == userId && x.DriverId != null)).AsQueryable());
        }

        public async Task<IQueryable<ListDriveModel>> GetAllDrivesUserIsNotIn(Guid userId)
        {

            var drives = _mapper.ProjectTo<ListDriveModel>(_driveRepository.Get().ToList().Where(x => x.Passengers.All(y => y.Id != userId) && x.DriverId != userId && x.DriverId != null).AsQueryable());
            List<ListDriveModel> returnedDrives = new List<ListDriveModel>();
            foreach(var drive in drives)
            {
                if (await NumberOfAvaliableSeats(drive.Id) > 0)
                {
                    returnedDrives.Add(drive);
                }
            }

            return returnedDrives.AsQueryable();
        }

        public async Task<bool> IsUserInDrive(Guid userId, Guid driveId)
        {
            var drives =
                _mapper.ProjectTo<ListDriveModel>(_driveRepository.Get().ToList().Where(x => x.Passengers.Any(y => (y.Id == userId || x.DriverId == userId) && x.DriverId != null)).AsQueryable());

            var conflictDrive = _driveRepository.Get().FirstOrDefault(x => x.Id == driveId);
            
            foreach (var drive in drives)
            {   
                if (!((conflictDrive.DepartureTime > drive.ArrivalTime)
                    || (conflictDrive.ArrivalTime < drive.DepartureTime)))
                {
                    return true;
                }
            }

            return false;
        }

        public async Task RemovePassengerFromDrive(Guid driveId, Guid userId)
        {
            var drive = _mapper.Map<DetailDriveModel>(_driveRepository.Get().FirstOrDefault(x => x.Id == driveId));
            var user = _userRepository.Get().FirstOrDefault(x => x.Id == userId);
            if (user != null && drive != null)
            {
                drive.Passengers.Remove(user);
                await _driveRepository.InsertOrUpdateAsync(drive, _mapper);
                await SaveAsync(drive);
            }
        }

        /// <summary>
        /// Usage: nefiltrovat nic: Filter(DateTime.MinValue);
        ///        filtrovat jizdy koncici pouze v Praze: Filter(DateTime.MinValue, true/false(je to jedno), null, "Praha");
        ///        filtrovat jizdy zacinajici pred datem: Filter(Datum, true);
        ///        filtrovat jizdy zacinajici v Praze: Filter(DateTime.MinValue, true/false, "Praha");
        ///        filtrovat jizdy zacinajici v Olomouci a koncici v Praze po datu: Filter(Datum, false, "Olomouc", "Praha");
        /// </summary>
        /// <param name="dateAndTime">Datum a čas od kdy/do kdy filtrovat, pokud nechcete podle tohoto filtrovat nastavte na hodnotu DateTime.MinValue</param>
        /// <param name="beforeDate">pokud je true budou se brát jizdy pouze před datem z prvního parametru, jinak po datu. Pokud se nefiltruje podle data, tak je jedno jakou ma hodnotu, jen musi byt explicitne nastavena na true nebo false</param>
        /// <param name="beginning">pokud neni null, bude se filtrovat podle jizd, jejichz nazev pocatecniho mista obsahuje tento parametr</param>
        /// <param name="destination">pokud neni null, bude se filtrovat podle jizd, jejich nazev konecneho mista obsahuje tento parametr</param>
        /// <returns></returns>
        public async Task<List<ListDriveModel>> Filter(DateTime dateAndTime, bool? beforeDate = true, string? beginning = null, string? destination = null, Guid? userId = null)
        {
            List<ListDriveModel> drives = new List<ListDriveModel>();

            if (userId != null)
            {
                drives = (await GetAllDrivesUserIsNotIn(userId.Value)).ToList();

            }
            else
            {
                drives = _mapper.ProjectTo<ListDriveModel>(_driveRepository.Get()).ToList();

            }
            if(dateAndTime != DateTime.MinValue)
            {
                if (beforeDate.Value)
                {
                    drives = drives.Where(x => x.DepartureTime >= dateAndTime).ToList();

                }
                else
                {
                    drives = drives.Where(x => x.DepartureTime <= dateAndTime).ToList();
                }
            }
            if(destination != null)
            {
                drives = drives.Where(x => x.Destination.Contains(destination)).ToList();
            }

            if (beginning != null)
            {
                drives = drives.Where(x => x.JourneyBeginning.Contains(beginning)).ToList();
            }

            return drives;


        }
    }
}
