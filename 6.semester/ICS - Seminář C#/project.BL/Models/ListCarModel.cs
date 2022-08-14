using AutoMapper;
using project.DAL.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace project.BL.Models
{
    public record ListCarModel : ModelBase
    {
        public string? Type { get; set; }

        public string? Manufacturer { get; set; }
        public string? ImageUrl { get; set; }
        public UserEntity? Owner { get; set; }

        public class MapperProfile : Profile
        {
            public MapperProfile()
            {
                CreateMap<CarEntity, ListCarModel>();

            }
        }
    }
}
