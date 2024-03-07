from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('AuthenticationSystem.urls')),  # This line of code is going to use or import all the urls from
    # the Authentication System Page

    path("__reload__/", include("django_browser_reload.urls")),  # Declares the path for tailwind
]
