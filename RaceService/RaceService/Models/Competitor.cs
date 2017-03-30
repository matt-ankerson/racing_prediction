using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace RaceService.Models
{
    public class Competitor
    {
        public int Id { get; set; }
        public string Number { get; set; }
        public string Name { get; set; }
        public string Jockey { get; set; }
        public string Place { get; set; }
        public string Win { get; set; }

        public int RaceId { get; set; }
    }
}