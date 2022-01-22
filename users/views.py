from multiprocessing import AuthenticationError
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerial
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

import jwt , datetime
class HomeView(APIView):
    def get(self , request):
        return Response({
            'message':"Welcome"
        })


class RegisterView(APIView):
    def post(self , request):
        serial = UserSerial(date =request.data)
        serial.is_valid(raise_exception=True)
        serial.save()
        return Response({'message':'USer Created'})



class LoginView(APIView):
    def post(self , request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email= email)[0]
        message = "Welcome"
        if user is None:
            raise AuthenticationFailed    #Raise Exception
        if not user.check_password(password):
            raise AuthenticationFailed#Raise Exception first override the save method in serializer method
        
        payload = {
            'id':user.id,
            'exp':datetime.datetime.now()+ datetime.timedelta(minutes=60),
            'iat':datetime.datetime.now()
        }
        token = jwt.encode(payload , 'secret' , algorithm = 'HS256')
        response = Response()
        response.set_cookie(key='jwt', value =token , httponly=True)
        response.data = token
        return response



class UserView(APIView):
    def get(self , request):
        cookie = request.COOKIES.get('jwt')
        if not cookie:
            raise AuthenticationFailed
        token = jwt.decode(cookie , 'secret', algorithms= ['HS256'])
        
        user = User.objects.get(id=token['id'])
        
        return Response(user.name)

            

class LogoutView(APIView):
    def post(self , request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':"Logout Complete"
        }
        return response
        

