from django.urls import path
from .views import home, dynamic_route  # Import both views

urlpatterns = [
    path("", home, name="home"),  # Default homepage
    path("<str:name>/", dynamic_route, name="dynamic"),  # Dynamic route
]
