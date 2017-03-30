using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Data.Entity;
using RaceService.Models;

namespace RaceService.DataAccess
{
    public class RaceDataContext : DbContext
    {
        public RaceDataContext(string connString) : base(connString)
        {

        }

        public DbSet<Event> Events { get; set; }
        public DbSet<Race> Races { get; set; }
        public DbSet<Competitor> Competitors { get; set; }
        public DbSet<Bet> Bets { get; set; }
    }
}