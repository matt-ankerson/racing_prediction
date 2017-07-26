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
    public class RacesController : ODataController
    {
        RaceDataContext context = new RaceDataContext("default");

        private bool RaceExists(int key)
        {
            return context.Races.Any(r => r.id == key);
        }

        [EnableQuery]
        public IQueryable<Race> Get()
        {
            return context.Races;
        }

        [EnableQuery]
        public SingleResult<Race> Get([FromODataUri] int key)
        {
            IQueryable<Race> result = context.Races.Where(r => r.id == key);
            return SingleResult.Create(result);
        }

        protected override void Dispose(bool disposing)
        {
            context.Dispose();
            base.Dispose(disposing);
        }
    }
}
