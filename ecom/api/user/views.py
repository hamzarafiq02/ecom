from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import userSerializer
from .models import customuser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
import re



import random
# Create your views here.

def genrate_session_token(lenght=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in range(lenght))


@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error':'send post request with valid parameter'})
        
    username = request.POST['email']
    password = request.POST['password']

    # valdation part
    if not re.match('^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$', username):
        return JsonResponse({'error': 'Enter a Valid Email'})    

    if len(password) < 3:
        return JsonResponse({'error':'Password need to atleast 3'}) 
    
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)
        if user.check_password(password):
           usr_dict = UserModel.objects.filter(email=username).values().first()
           usr_dict.pop('password')

           if user.session_token != '0':
            user.session_token = '0'
            user.save()
            return JsonResponse({'error': 'previous session exists'})

           token = genrate_session_token()
           user.session_token = token
           user.save()
           login(request, user)
           return JsonResponse({'token': token, 'user': usr_dict})
        else:
            return JsonResponse({'error': 'Invalid Password'})

    except UserModel.DoesNotExit:
           return JsonResponse({'error': 'Invalid Email'})

def signout(request, id):
    logout(request)

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user ID'})

    return JsonResponse({'success': 'Logout success'})

class userViewSet(viewsets.ModelViewSet):
    permission_class_by_action = {'create': [AllowAny]}
    queryset = customuser.objects.all().order_by('id')
    serializers_class = userSerializer
    def get_permission(self):
        try:
            return[permission() for permission in self.permission_classes_by_action[self.action]] 
        except KeyError:
            return[permission() for permission in self.permission_classe]

