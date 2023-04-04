import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from apps.users.models import User


class UserNameCountView(View):
    def get(self, request, username):
        count = User.objects.filter(username=username).count()
        return JsonResponse({'code': 0, 'count': count, 'errorMsg': 'ok'})


# Create your views here.  22
class RegisterView(View):
    def get(self, request):
        """
        第一个函数响应
        :param request:
        :return:
        """
        resp = {'code': 1000, 'data': None, 'message': 'success', 'total': 2011}
        return HttpResponse(json.dumps(resp))
