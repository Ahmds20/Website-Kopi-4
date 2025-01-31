from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', include('admin_honeypot.urls')),
    path('admin12/', admin.site.urls),
    path('products/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('search/', include('search.urls')),
    path('payment/', include('payment.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
