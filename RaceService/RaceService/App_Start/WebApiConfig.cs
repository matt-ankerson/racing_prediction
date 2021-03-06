﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Web.Http;
using RaceService.Models;
using System.Web.OData.Builder;
using System.Web.OData.Extensions;

namespace RaceService
{
    public static class WebApiConfig
    {
        public static void Register(HttpConfiguration config)
        {
            // Web API configuration and services


            config.Routes.MapHttpRoute(
                name: "DefaultApi",
                routeTemplate: "api/{controller}/{id}",
                defaults: new { id = RouteParameter.Optional }
            );
        }
    }
}
