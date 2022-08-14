using AutoMapper;
using project.DAL.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace project.BL.Models
{
    public record DetailDriveModel : ModelBase
    {
        public string? JourneyBeginning { get; set; }
        public string? Destination { get; set; }
        public DateTime DepartureTime { get; set; }
        public DateTime ArrivalTime { get; set; }
        public bool IsFull { get; set; }
        public UserEntity? Driver { get; set; }
        public Guid DriverId { get; set; }
        public List<UserEntity>? Passengers { get; set; }
        public CarEntity? Car { get; set; }
        public Guid CarId { get; set; }

        public class MapperProfile : Profile
        {
            public MapperProfile()
            {
                CreateMap<DriveEntity, DetailDriveModel>()
                    .ReverseMap()
                    .ForMember(entity => entity.Car, expression => expression.Ignore())
                    .ForMember(entity => entity.Driver, expression => expression.Ignore());
            }
        }
        public static DetailDriveModel Empty => new();
    }
}
