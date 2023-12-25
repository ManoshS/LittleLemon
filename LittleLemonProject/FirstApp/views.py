from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookingSerializer ,menuSerializer,UserSerializer
from rest_framework import generics
from .models import Booking ,Menu
from rest_framework import viewsets,permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your views here.
def home(request):
    return render(request,'index.html',{'current_year':2024})

class BookingView(APIView):
    def get(self,request):
        item=Booking.objects.all()
        serializer=BookingSerializer(item,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'status':"Success",'data':serializer.data})
    
class ListMenuItemsView(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView):
    queryset=Menu.objects.all()
    serializer_class=menuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes=[permissions.IsAuthenticated]

class RegisterUser(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':"something went wrong"})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        token_obj,_=Token.objects.get_or_create(user=user)
        return Response({'status':200,'payload':serializer.data,'token':str(token_obj),'message':"success"})