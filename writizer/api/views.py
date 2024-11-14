from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from writizer.api.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            # Okuma işlemleri için herkese izin ver
            return [permissions.AllowAny()]
        else:
            # Yazma işlemleri için sadece giriş yapmış kullanıcılara izin ver
            return [permissions.IsAuthenticated()]