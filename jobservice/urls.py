from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from profskills.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('profskills.urls')),
    path('users/', include('users.urls')),
]


if settings.DEBUG:
	import debug_toolbar

	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls))
					] + urlpatterns

	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)