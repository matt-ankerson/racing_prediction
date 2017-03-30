using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using RaceService.DataAccess;
using RaceService.Models;

namespace RaceService.Controllers
{
    public class EventController : ApiController
    {
        // POST api/event
        public void Post([FromBody]Event eventViewModel)
        {
            if (eventViewModel == null) return;

            using (var context = new RaceDataContext("default"))
            {
                // Insert Event
                context.Events.Add(eventViewModel);
                context.SaveChanges();
            }
        }
    }
}
