using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace RaceService.Models
{
    public class Race
    {
        public int Id { get; set; }
        public string RaceNumber { get; set; }
        public string Distance { get; set; }
        public string Stake { get; set; }
        public string TrackCondition { get; set; }
        public string Weather { get; set; }
        public string WinningMargins { get; set; }
        public string WinnerOwners { get; set; }
        public string WinnerTrainer { get; set; }
        public string WinnerBreeding { get; set; }
        public string Sub { get; set; }
        public string WinnerTime { get; set; }

        public int EventId { get; set; }

        public IList<Bet> Bets { get; set; }
        public IList<Competitor> Competitors { get; set; }
    }
}