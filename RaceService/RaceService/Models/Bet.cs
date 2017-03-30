using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace RaceService.Models
{
    public class Bet
    {
        [Key]
        public int id { get; set; }
        public string bet_type { get; set; }
        public string runners { get; set; }
        public string dividend { get; set; }

        public int race_id { get; set; }
        [ForeignKey(nameof(race_id))]
        public Race the_race { get; set; }
    }
}