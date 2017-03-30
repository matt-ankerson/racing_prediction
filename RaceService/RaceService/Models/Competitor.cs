using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace RaceService.Models
{
    public class Competitor
    {
        [Key]
        public int id { get; set; }
        public string number { get; set; }
        public string name { get; set; }
        public string jockey { get; set; }
        public string place { get; set; }
        public string place_in_race { get; set; }
        public string win { get; set; }

        public int race_id { get; set; }
        [ForeignKey(nameof(race_id))]
        public Race the_race { get; set; }
    }
}