using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace project.DAL.Entities
{
    public  record CarEntity : BaseEntity
    {
        public string? Manufacturer { get; set; }
        public string? Type { get; set; }
        public string? ImageUrl { get; set; }
        public DateTime DateOfRegistration { get; set; }
        public int NumberOfSeats { get; set; }
        public UserEntity? Owner { get; set; }
        public Guid? OwnerId { get; set; } = null;
        public ICollection<DriveEntity>? Drives { get; set; } = new List<DriveEntity>();

       
    }
}
