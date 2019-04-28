from django.contrib import admin
from django.urls import path, include
from django.conf import settings                         # 추가 1
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('pizzas/', include('pizzas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:                                       # 추가 2
    import debug_toolbar                                 # 추가 2
    urlpatterns += [                                     # 추가 2
        path('__debug__/', include(debug_toolbar.urls)), # 추가 2
    ]                                                    # 추가 2
