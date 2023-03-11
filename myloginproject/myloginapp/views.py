from django.http import HttpResponse
from django.shortcuts import redirect, render

from myloginapp.forms import MyuserForm
from myloginapp.models import MyUser
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


# def my_loginrequired(func):
#     import pdb
#     pdb.set_trace()

#     def inner(request):
#         print("inside my_loginrequired: ")
#         credentials = request.session.get("credentials")
#         print("type", type(credentials))
#         username = credentials.get("username")
#         password = credentials.get("password")
#         get_user = MyUser.objects.filter(username=username).first()
#         print("get_user: ", get_user)
#         if check_password(password, get_user.password):
#             credentials = {}
#             credentials["username"] = username
#             credentials["password"] = password
#             request.session["credentials"] = credentials
#             func()
#             return inner
#         return render(request, "myloginapp/login.html")
#     return inner


# @my_loginrequired
def home_info(request):
    credentials = request.session.get("credentials")
    print("type", type(credentials))

    print("credentials: ", credentials)
    return render(request, 'myloginapp/home.html')


def user_signup(request):
    if request.method == 'POST':
        form_dict = {}
        form_dict["username"] = request.POST.get('username')
        form_dict["email"] = request.POST.get('email')
        form_dict["phone"] = request.POST.get('phone')
        form_dict["fullname"] = request.POST.get('fullname')
        form_dict["password"] = make_password(request.POST.get('password'))
        print("form_dict: ", form_dict)

        import pdb
        pdb.set_trace()
        form = MyuserForm(form_dict)
        if form.is_valid():
            user = form.save()
            return render(request, "myloginapp/login.html")
    else:
        form = MyuserForm()
    return render(request, 'myloginapp/signup.html', {'form': form})


# def userlogin(request):
#     if request.method == 'POST':

#     return render(request, "myloginapp/login.html")

def login_view(request):
    if request.method == 'POST':
        import pdb
        pdb.set_trace()
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print("password: ", password)
        get_user = MyUser.objects.filter(username=username).first()
        print("get_user: ", get_user)
        if check_password(password, get_user.password):
            credentials = {}
            credentials["username"] = username
            credentials["password"] = password
            request.session["credentials"] = credentials

            print(password)
            return HttpResponse("<h3>login Success</h3>")
        return HttpResponse("<h3>login failed</h3>")

    return render(request, 'myloginapp/login.html')


# user = auth.authenticate(request, username=username, password=password)
#       print(user)
#        if user is not None:
#             auth.login(request, user)
#             # return redirect(request.GET.get('next', "home"))
#             return redirect("home")
#         else:
#             error_message = 'Invalid username or password'
#             return render(request, 'signin.html', {'error_message': error_message})
