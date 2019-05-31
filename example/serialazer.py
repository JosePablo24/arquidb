#### --------------- Agregar las librerias frameworks- ---------------------------
from rest_framework from routers, serializers, viewsets

### Agregar modelos 

from example.models import Example

class ExampleSerializers(serializers.ModelSeralizer):
    class Meta:
        model = Example
        fields = ('__all__') 