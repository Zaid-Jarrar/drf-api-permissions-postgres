from rest_framework.generics import (
                            ListCreateAPIView,    
                            RetrieveUpdateDestroyAPIView,)
from snacks.models import Snack 
from .serializers import SnackSerializer    
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated            

class SnackListView(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = (IsAuthenticated,)
    
    
class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)


    