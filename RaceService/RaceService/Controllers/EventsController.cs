using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;
using System.Web.Http;
using System.Web.Http.ModelBinding;
using System.Web.OData;
using System.Web.Http.OData.Query;
using System.Web.Http.OData.Routing;
using RaceService.Models;
using RaceService.DataAccess;
using Microsoft.Data.OData;

namespace RaceService.Controllers
{
    public class EventsController : ODataController
    {
        RaceDataContext context = new RaceDataContext("default");

        private bool EventExists(int key)
        {
            return context.Events.Any(e => e.id == key);
        }

        // The POSTed parameter is always null - why is this?
        [HttpPost]
        public IHttpActionResult Post(Event eventViewModel)
        {
            if (eventViewModel == null) return BadRequest();

            // Insert Event
            context.Events.Add(eventViewModel);
            context.SaveChanges();

            return Created(eventViewModel);
        }

        protected override void Dispose(bool disposing)
        {
            context.Dispose();
            base.Dispose(disposing);
        }
    }
}
