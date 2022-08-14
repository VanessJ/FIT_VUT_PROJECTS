using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace project.DAL.Entities
{   
    
    public record DriveEntity : BaseEntity
    {
        public string? JourneyBeginning { get; set; }
        public string? Destination { get; set; }
        public DateTime DepartureTime { get; set; }
        public DateTime ArrivalTime { get; set; }
        public bool IsFull { get; set; }
        public UserEntity? Driver { get; set; }
        public Guid? DriverId { get; set; } = null;
        public ICollection<UserEntity>? Passengers { get; set; } = new List<UserEntity>();
        public CarEntity? Car { get; set; }
        public Guid? CarId { get; set; } = null;
    }
}
