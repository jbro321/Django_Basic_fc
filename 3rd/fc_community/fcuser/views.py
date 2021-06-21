from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password #장고에서 제공하는 비밀번호 암호화
from .models import Fcuser
from .forms import LoginForm

# Create your views here.

def home(request):
    user_id = request.session.get('user') # 유저키로 값이 들어있으면 로그인

    if user_id: # user키로 확인해본다.
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)

    return HttpResponse('Home!')

def logout(request):
    if request.session.get('user'):
        # 값이 있는지 없는지 판단.
        del(request.session['user'])
    
    return redirect('/')

def login(request): # 로그인 페이지 연결
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            # session
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form' : form})

    # if request.method == 'GET':
    #     return render(request, 'login.html')
    # elif request.method == 'POST':
    #     username = request.POST.get('username', None)
    #     password = request.POST.get('password', None)
        
    #     res_data = {}
    #     if not (username and password):
    #         res_data['error'] = '모든 값을 입력해야합니다.'
    #     else:
    #         fcuser = Fcuser.objects.get(username=username)
    #         if check_password(password, fcuser.password):
    #             request.session['user'] = fcuser.id
    #             return redirect('/') # / 만 써주면 홈으로 간다.
    #             # 비밀번호 일치, 로그인 처리를!
    #             # 세션!
    #             # 홈으로 가는, 리다이렉트
    #         else:
    #             res_data['error'] = '비밀번호가 틀렸습니다.'

    #     return render(request, 'login.html', res_data)

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