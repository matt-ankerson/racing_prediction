using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.ComponentModel.DataAnnotations;

namespace RaceService.Models
{
    public class Event
    {
        [Key]
        public int id { get; set; }
        public string name { get; set; }
        public string date { get; set; }
        public IList<Race> races { get; set; }
    }
}