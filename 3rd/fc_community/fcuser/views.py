from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password #장고에서 제공하는 비밀번호 암호화
from .models import Fcuser

# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html') # 장고를 통해 보기 위해
    elif request.method == 'POST':
        username = request.POST.get('username', None) # 기본값 없으면 none
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                username=username,
                password=make_password(password) # make_password로 암호화해서 비밀번호가 들어간다.
            )

            fcuser.save()

        return render(request, 'register.html', res_data)