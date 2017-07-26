using System;
using System.Collections.Generic;
using System.Linq;
using System.Web.Http;
using RaceService.Models;
using System.Web.OData.Builder;
using System.Web.OData.Extensions;

namespace RaceService
{
    public static class OdataConfig
    {
        public static void Register(HttpConfiguration config)
        {
            config.MapHttpAttributeRoutes(); //This has to be called before the following OData mapping, so also before WebApi mapping

            config.AddODataQueryFilter();
            config.Select().Expand().Filter().OrderBy().MaxTop(null).Count();

            ODataModelBuilder builder = new ODataConventionModelBuilder();
            builder.EntitySet<Race>("Races");
            builder.EntitySet<Event>("Events");

            config.MapODataServiceRoute(
                routeName: "ODataRoute",
                routePrefix: "odata",
                model: builder.GetEdmModel());
        }
    }
}
