from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json


# Create your views here.
class RegisterView(View):
    def get(self, request):
        """
        第一个函数响应
        :param request:
        :return:
        """
        resp = {'code': 1000, 'data': None, 'message': 'success'}
        return HttpResponse(json.dumps(resp))
