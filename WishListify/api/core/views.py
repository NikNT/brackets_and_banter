from rest_framework.viewsets import ModelViewSet
from core.models import WishList
from core.serializers import WishListSerializer


# Create your views here.

class WishListView(ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer