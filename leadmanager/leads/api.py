from leads.models import Lead
from rest_framework import viewsets, permissions

from .serializers import LeadSerializer

# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = LeadSerializer

    def get_queryset(self):
        return self.request.user.leads.all()

    def perfrom_create(self, serializer):
        print(self)
        serializer.save(owner=self.request.user)
