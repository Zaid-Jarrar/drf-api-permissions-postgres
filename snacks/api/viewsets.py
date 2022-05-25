from rest_framework.generics import (
                            ListCreateAPIView,    
                            RetrieveUpdateDestroyAPIView,)
from snacks.models import Snack 
from .serializers import SnackSerializer    
from .permissions import IsOwnerOrReadOnly            

class SnackListView(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    


class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = (IsOwnerOrReadOnly,)