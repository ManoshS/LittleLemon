from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookingSerializer ,menuSerializer,UserSerializer
from rest_framework import generics
from .models import Booking ,Menu
from rest_framework import viewsets,permissions,status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
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
 
    

#@permission_classes([permissions.IsAuthenticated])
def secrateMessage(request):
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return HttpResponse("There is No Authorization")

        # Check if the header starts with 'Bearer'
    if not auth_header.startswith('Bearer '):
        
        return HttpResponse("There is No Bearer")

        # Extract the token
    token = auth_header.split(' ')[1]

    try:
            # Get the user associated with the token
        token_obj = Token.objects.get(key=token)
        user = token_obj.user
    except Token.DoesNotExist:
        raise AuthenticationFailed('Invalid token')

    #return (user, None)
    return HttpResponse("This is Secrate message")