from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'director', DirectorViewSet, basename='director_list')
router.register(r'actor', ActorViewSet, basename='actor_list')
router.register(r'favorite', FavoriteViewSet, basename='favorite_list')
router.register(r'user', ProfileViewSet, basename='user_list')
router.register(r'rating', RatingViewSet, basename='rating_list' )


urlpatterns = [
    path('', include(router.urls)),
    path('movie/', MovieListViewSet.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailViewSet.as_view(), name='movie_detail'),

    path('country/', CountryListViewSet.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailViewSet.as_view(), name='country_detail'),

    path('genre/', GenreListViewSet.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailViewSet.as_view(), name='genre_detail'),

    path('favorite/', FavoriteViewSet.as_view({'get': 'list'}), name='favorite_list'),
    path('favorite_movie/', FavoriteMovieViewSet.as_view({'get': 'list', 'delete': 'destroy'}), name='favorite_movie_list'),
    path('favorite_movie/<int:pk>/', FavoriteMovieViewSet.as_view({'get': 'list'}), name='favorite_movie_detail'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')

]