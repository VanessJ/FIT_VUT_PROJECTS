using AutoMapper;
using project.DAL.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace project.BL.Models
{
    public record ListDriveModel : ModelBase
    {
        public string? JourneyBeginning { get; set; }
        public string? Destination { get; set; }
        public DateTime DepartureTime { get; set; }
        public DateTime ArrivalTime { get; set; }
        public bool IsFull { get; set; }

        public string departureTime
        {
            get { return DepartureTime.ToString("HH:mm"); }
        }
        public string arrivalTime
        {
            get { return ArrivalTime.ToString("HH:mm"); }
        }

        public class MapperProfile : Profile
        {
            public MapperProfile()
            {
                CreateMap<DriveEntity, ListDriveModel>();

            }
        }
    }
}