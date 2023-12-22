using Grand.Business.Core.Interfaces.Catalog.Products;
using Grand.Business.Core.Interfaces.Common.Directory;
using Grand.Business.Core.Interfaces.Common.Localization;
using Grand.Business.Core.Interfaces.Common.Logging;
using Grand.Business.Core.Interfaces.Common.Seo;
using Grand.Business.Core.Interfaces.Customers;
using Grand.Business.Core.Interfaces.Storage;
using Grand.Domain.Catalog;
using Grand.Domain.Common;
using Grand.Domain.Customers;
using Grand.Domain.Seo;
using Grand.Infrastructure;
using Grand.Web.Admin.Extensions;
using Grand.Web.Admin.Interfaces;
using Grand.Web.Admin.Models.Catalog;
using Grand.Web.Common.DataSource;
using Grand.Web.Common.Extensions;
using Grand.Web.Common.Filters;
using Grand.Web.Common.Security.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;



```csharp
using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;

namespace YourNamespace
{
    public class ProductController : Controller
    {
        private readonly IProductService _productService;
        private readonly ITranslationService _translationService;
        private readonly