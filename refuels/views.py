from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Refuel
from .serializer import RefuelSerializer

@api_view(['GET'])
def getAllRefuels(request):
    refuels = Refuel.objects.all().order_by('-date')
    serialized = RefuelSerializer(refuels, many = True)
    return Response(serialized.data)
