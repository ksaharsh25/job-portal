from django.shortcuts import render
# from rest_framework.views import APIView
# from django.http.response import JsonResponse
# from .models import *

# class StateList(APIView):
#     #permission_classes = [IsAuthenticated, ]

#     def post(self, request, format=None):
#         country = request.data['country']
#         State = {}
#         if country:
#             States = Country.objects.get(id=country).States.all()
#             State = {p.name: p.id for p in States}
#         return JsonResponse(data=State, safe=False)


# class CityList(APIView):
#     #permission_classes = [IsAuthenticated, ]

#     def post(self, request, format=None):
#         State = request.data['State']
#         City = {}
#         if State:
#             Citys = State.objects.get(id=State).Citys.all()
#             City = {p.name: p.id for p in Citys}
#         return JsonResponse(data=City, safe=False)

