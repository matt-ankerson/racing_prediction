using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace RaceService.Models
{
    public class Bet
    {
        public int Id { get; set; }
        public string BetType { get; set; }
        public string Runners { get; set; }
        public string Dividend { get; set; }

        public int RaceId { get; set; }
    }
}