from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Refuel
from .serializer import RefuelSerializer

@api_view(['GET'])
def getAllRefuels(request):
    refuels = Refuel.objects.all().order_by('-date')
    serialized = RefuelSerializer(refuels, many = True)
    return Response(serialized.data)

@api_view(['GET'])
def getLastConsumption(request):
    refuels = Refuel.objects.all().order_by('-date')
    if len(refuels) < 2:
        return Response({'consumption': None})
    last = refuels[0]
    before = refuels[1]
    distance = last.distance - before.distance
    consumption = round((last.amount/distance)*100, 1)
    return Response({'consumption': consumption})