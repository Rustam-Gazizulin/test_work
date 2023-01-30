from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from commercial_network import views


urlpatterns = [
    path('', views.ProviderListView.as_view()),
    path('<int:pk>/', views.ProviderRetrieveView.as_view()),
    path('create/', views.ProviderCreateView.as_view()),
    path('update/<int:pk>/', views.ProviderUpdateView.as_view()),
    path('delete/<int:pk>/', views.ProviderDestroyView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    ]
