﻿using AutoMapper;
using project.DAL.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace project.BL.Models
{
    public record ListUserModel : ModelBase
    {

        public string? FirstName { get; set; }
        public string? LastName { get; set; }
        public string? ImageUrl { get; set; }
      

        public class MapperProfile : Profile
        {
            public MapperProfile()
            {
                CreateMap<UserEntity, ListUserModel>();
            }
        }
    }
}