#project level urls

from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView, 
)  

urlpatterns = [
    path('admin/', admin.site.urls),

	# api urls
	path('api/v1/',include('users.urls')),
	path('api/v1/',include('jobs.urls')),
	path('api/v1/',include('articles.urls')),

	# dj-rest-auth (login-logout endpoints)
	path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),
	
	# all auth (register endpoint)
	path("api/v1/dj-rest-auth/registration/", 
          include("dj_rest_auth.registration.urls")),
	path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
	path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(
        url_name="schema"), name="swagger-ui"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)