from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from accounts.api import views
from knox.views import LogoutView

urlpatterns = [
    path('signup/', views.RegisterAPI.as_view()),
    path('login/', views.LoginAPI.as_view()),
    path('c/',include('accounts.api.urls')),
    path('logout/', LogoutView.as_view(), name='knox_logout')
]

urlpatterns = format_suffix_patterns(urlpatterns)