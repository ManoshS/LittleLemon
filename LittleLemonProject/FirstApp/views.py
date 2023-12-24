from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookingSerializer ,menuSerializer
from rest_framework import generics
from .models import Booking ,Menu
# Create your views here.
def home(request):
    return render(request,'index.html',{'current_year':2024})

class BookingView(APIView):
    def get(request,pk):
        item=Booking.objects.all()
        serializer=BookingSerializer(item,many=True)
        return Response(serializer.data)
    
    def post(request):
        serializer=BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'status':"Success",'data':serializer.data})
    
class ListMenuItemsView(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=menuSerializer