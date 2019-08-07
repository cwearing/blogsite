from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
	path('create', views.CreateView.as_view(), name='create'),
	path('<int:pk>/', views.DetailsView.as_view(), name='details'),
    path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
	path('<int:pk>/author/', views.AuthorView.as_view(), name='author'),
]

