
from django.conf.urls import url
from django.contrib import admin


from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('products/',include('products.urls')),
    path('accounts/',include('accounts.urls')),
    #path
]  +static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
