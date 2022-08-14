using AutoMapper;
using project.DAL.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace project.BL.Models
{
    public record DetailCarModel : ModelBase
    {
        public string? Manufacturer { get; set; }
        public string? Type { get; set; }
        public string? ImageUrl { get; set; }
        public DateTime DateOfRegistration { get; set; }
        public int NumberOfSeats { get; set; }
        public UserEntity? Owner { get; set; }
        public Guid OwnerId { get; set; }

        public class MapperProfile : Profile
        {
            public MapperProfile()
            {
                CreateMap<CarEntity, DetailCarModel>()
                    .ReverseMap()
                    .ForMember(entity => entity.Owner, expression => expression.Ignore());

            }
        }

        public static DetailCarModel Empty => new();

    }
}
