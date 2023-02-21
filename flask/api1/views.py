from rest_framework.generics import ListCreateAPIView
from woow.models import User
from .serializers import UserSerializer

class UserApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


