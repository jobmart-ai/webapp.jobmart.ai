import json
import base64
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from webapi.models import UserProfile
from serializers.user_profile_serializer import UserProfileRegistrationSerializer
from json.decoder import JSONDecodeError
from django.db.utils import IntegrityError
from django.contrib.auth import login, logout
from django.forms.models import model_to_dict
from rest_framework.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt

filters = ['id', 'username', 'email', 'enablePdfToImage', 'enableJobApplicationTracker']

def blob_to_dict(blob):
    return {
        'name': blob.name,
        'content': base64.b64encode(blob.content).decode('utf-8')
    }

def get(request):
    user = request.user
    if user.is_authenticated:
        getProfileImage = request.GET.get('profileImage')
        object = model_to_dict(user)
        data = {key: value for key, value in object.items() if key in filters}
        
        if getProfileImage == "1" and user.profileImage:
            blob = user.profileImage
            print(blob)
            data['profileImage'] = blob_to_dict(blob)
        
        print('User is authenticated')
        return JsonResponse(data)
    else:
        return HttpResponse('User Unauthorized', status=401)
    

# @csrf_exempt
def register(request):
    user = request.user
    print(user)
    if user.is_authenticated:
        return HttpResponse('User already logged in. Please logout to register a new user', status=400)
    else:
        try:
            model = json.loads(request.body.decode('utf-8'))
            entity = UserProfileRegistrationSerializer(data=model)
            if entity.is_valid(raise_exception=True):
                entity.save()
                login(request, entity.instance)
                data = model_to_dict(entity.instance)
                data = {key: value for key, value in data.items() if key in filters}
                
                if entity.validated_data['profileImage']:
                    blob = entity.validated_data['profileImage']['name']
                    data['profileImage'] = {
                        'name': entity.validated_data['profileImage']['name'],
                        'content': base64.b64encode(entity.validated_data['profileImage']['content']).decode('utf-8')
                    }

                print('User registered successfully')
                return JsonResponse(data)
            else:
                return BadRequestHandler("Request payload failed schema validation")
        except JSONDecodeError as e:
            print(e)
            return BadRequestHandler(e.args[0])
        except IntegrityError as e:
            return BadRequestHandler(e.args[1])
        except ValidationError as e:
            return BadRequestHandler(e.args[0])
        except AttributeError as e:
            return BadRequestHandler(e.args[0])


def delete(request):
    user = request.user
    if user.is_authenticated:
        user.delete()
        data = model_to_dict(user)
        data = {key: value for key, value in data.items() if key in filters}
        print('User deleted successfully')
        return JsonResponse(data)
    else:
        return HttpResponse('User Unauthorized', status=401)
    

def signout(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        data = model_to_dict(user)
        data = {key: value for key, value in data.items() if key in filters}
        print('User logged out successfully')
        return JsonResponse(data)
    else:
        return HttpResponse('User Unauthorized', status=401)
        

# @csrf_exempt  
def signin(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse('User already logged in. Please logout to login with a different user', status=400)
    else:
        try:
            username = request.GET.get('username')
            password = request.GET.get('password')
            print(username, password)

            entity = UserProfile.objects.filter(username=username)
            if len(entity) == 0:
                return HttpResponseNotFound("Username does not exist")
            elif entity[0].password != password:
                return HttpResponseNotFound("Incorrect Password")
            
            login(request, entity[0])
            data = model_to_dict(entity[0])
            data = {key: value for key, value in data.items() if key in filters}
            
            print('User logged in successfully')
            return JsonResponse(data)
        
        except JSONDecodeError as e:
            return BadRequestHandler(e.args[0])
        except IntegrityError as e:
            return BadRequestHandler(e.args[1])

    
def BadRequestHandler(e):
    error = {
        "message": e,
        "schema": {
            "username" : "",
            "email": "",
            "password": "",
            "enablePdfToImage": False,
            "enableJobApplicationTracker": False
        }
    }
    return JsonResponse(error, status=400)
    