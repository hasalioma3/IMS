
from django.contrib import admin
from django.urls import path,include

# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("inventory/", include("inventory.urls"), name="inventory"),
    path("", LoginView.as_view(template_name = "src/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name = "src/logout.html"), name="logout")
]
