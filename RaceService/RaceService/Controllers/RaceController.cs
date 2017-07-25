using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;
using System.Web.Http;
using System.Web.Http.ModelBinding;
using System.Web.Http.OData;
using System.Web.Http.OData.Query;
using System.Web.Http.OData.Routing;
using RaceService.Models;
using RaceService.DataAccess;
using Microsoft.Data.OData;

namespace RaceService.Controllers
{
    public class ProductsController : ODataController
    {
        private bool RaceExists(int key)
        {
            using (var context = new RaceDataContext("default"))
            {
                return context.Races.Any(r => r.id == key);
            }
        }

        [EnableQuery]
        public IQueryable<Race> Get()
        {
            using (var context = new RaceDataContext("default"))
            {
                return context.Races;
            }
        }

        [EnableQuery]
        public SingleResult<Race> Get([FromODataUri] int key)
        {
            using (var context = new RaceDataContext("default"))
            {
                IQueryable<Race> result = context.Races.Where(r => r.id == key);
                return SingleResult.Create(result);
            }
        }
    }
}
