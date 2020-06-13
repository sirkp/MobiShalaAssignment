from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.serializers import UserCreateSerializer
# Create your views here.

class UserRegistrationApi(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            user_serializer = UserCreateSerializer(data=request.data)
            if user_serializer.is_valid():
                user = user_serializer.save()
                return Response({
                    'status': True,
                    'msg': 'Registration Successful!',
                }, status=status.HTTP_200_OK)
            else:
                message = ''
                for error in user_serializer.errors.values():
                    message += " "
                    message += error[0]
                return Response({'status': False,
                                 'message': message},
                                status=status.HTTP_400_BAD_REQUEST)    
        except Exception as e:
            return Response({'status': False,
                             'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

# class LoginApi(APIView):

#     def post(self, request, *args, **kwargs):
#         try:
#             username = request.data.get('username')
#             password = request.data.get('password')

#             data = {
#                 'username': username,
#                 'password': password
#             }


#         except Exception as e:
#             return Response({'status': False,
#                              'message': str(e)},
#                             status=status.HTTP_400_BAD_REQUEST)
    