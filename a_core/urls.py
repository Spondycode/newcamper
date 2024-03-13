"""
URL configuration for a_core project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from a_users.views import profile_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', include('a_home.urls')),
    path('', include("a_plot.urls")),
    path('profile/', include('a_users.urls')),
    path('@<username>/', profile_view, name="profile"),
]

# Only used in Development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

