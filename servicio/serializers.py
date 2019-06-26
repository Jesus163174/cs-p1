from rest_framework import routers, serializers, viewsets
from servicio.models import Servicio

class ServicioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ('__all__')