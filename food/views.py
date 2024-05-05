import json

from django.http import JsonResponse
from food.models import User, Food, Nutrient, FoodNutrient
from django.core import serializers
from django.db.models import Q
from django.core.cache import cache


def login(request):
    data = json.loads(request.body.decode('utf-8'))
    username = data.get('username')
    password = data.get('password')
    user = User.objects.filter(username=username, password=password).first()
    if not user:
        data = {
            'success': False,
            'msg': '用户不存在',
            'data': {}
        }
        return JsonResponse(data, safe=False)
    if user.username != username or user.password != password:
        data = {
            'success': False,
            'msg': '密码或密码错误',
            'data': {}
        }
        return JsonResponse(data, safe=False)
    data = {
        'success': True,
        'msg': '登录成功',
        'data': {
            'id': user.id,
        }
    }
    return JsonResponse(data, safe=False)


#  创建用户 注册
def register(request):
    data = json.loads(request.body.decode('utf-8'))
    username = data.get('username')
    password = data.get('password')
    phone = data.get('phone')
    email = data.get('email')
    user = User.objects.filter(username=username).first()
    if user:
        data = {
            'success': False,
            'msg': '用户名已存在',
            'data': {}
        }
        return JsonResponse(data, safe=False)
    user = User.objects.create(username=username, password=password, email=email, phone=phone)
    data = {
        'success': True,
        'msg': '注册成功',
        'data': {
            'id': user.id
        }
    }
    return JsonResponse(data, safe=False)


# 获取用户信息
def get_user(request):
    data = json.loads(request.body.decode('utf-8'))
    id = data.get('id')
    user = User.objects.filter(id=id).first()
    if not user:
        data = {
            'success': False,
            'msg': '用户不存在',
            'data': {}
        }
        return JsonResponse(data, safe=False)
    data = {
        'success': True,
        'msg': '获取用户信息成功',
        'data': serializers.serialize('python', [user])[0]
    }
    return JsonResponse(data, safe=False)


# 更新用户信息
def update_user(request):
    data = json.loads(request.body.decode('utf-8'))
    id = data.get('id')
    user = User.objects.filter(id=id).first()
    if not user:
        data = {
            'success': False,
            'msg': '用户不存在',
            'data': {}
        }
        return JsonResponse(data, safe=False)
    user.password = data.get('password')
    user.email = data.get('email')
    user.phone = data.get('phone')
    user.sex = data.get('sex')
    user.age = data.get('age')
    user.height = data.get('height')
    user.weight = data.get('weight')
    user.blood_pressure = data.get('blood_pressure')
    user.diabetes = data.get('diabetes')
    user.pregnancy = data.get('pregnancy')
    user.save()
    data = {
        'success': True,
        'msg': '更新用户信息成功',
        'data': serializers.serialize('python', [user])[0]
    }
    return JsonResponse(data, safe=False)
