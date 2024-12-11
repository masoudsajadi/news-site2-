
from django.urls import path
from .views import home, RegisterView ,profile # Import the view here


urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),  # This is what we added
    path('profile/', profile, name='users-profile'),
    
    
]

