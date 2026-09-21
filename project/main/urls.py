from django.urls import path
from .views import advertisements, advertisement_detail, login_view, logout_view, add_advertisement, edit_advertisement, delete_advertisement, favorite_advertisement, favorite_advertisements

urlpatterns = [
    path('', advertisements, name='advertisements'),
    path('ad/<int:id>/', advertisement_detail, name='advertisement_detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('ad/add/', add_advertisement, name='add_advertisement'),
    path('ad/<int:id>/edit/', edit_advertisement, name='edit_advertisement'),
    path('ad/<int:id>/delete/', delete_advertisement, name='delete_advertisement'),
    path('ad/<int:id>/favorite/', favorite_advertisement, name='favorite_advertisement'),
    path('favorites/', favorite_advertisements, name='favorite_advertisements'),
]