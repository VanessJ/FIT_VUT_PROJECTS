using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace project.BL.Models
{
    public record ModelBase : IModel
    {
        public Guid Id { get; set; }
    }
}
