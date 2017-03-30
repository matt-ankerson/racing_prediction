using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace RaceService.Models
{
    public class Race
    {
        [Key]
        public int id { get; set; }
        public string race_number { get; set; }
        public string distance { get; set; }
        public string stake { get; set; }
        public string track_condition { get; set; }
        public string weather { get; set; }
        public string winning_margins { get; set; }
        public string winner_owners { get; set; }
        public string winner_trainer { get; set; }
        public string winner_breeding { get; set; }
        public string sub { get; set; }
        public string winner_time { get; set; }

        public int event_id { get; set; }
        [ForeignKey(nameof(event_id))]
        public Event the_event { get; set; }

        public IList<Bet> bets { get; set; }
        public IList<Competitor> competitors { get; set; }
    }
}