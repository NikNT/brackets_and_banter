from django.urls import path
from core.views import WishListView

urlpatterns = [
    path('wishlist/', WishListView.as_view({
        'get': 'list', 'post': 'create'
    })),
]