from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django import forms as LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from mysite.models import Product
from mysite.forms import UserRegisterForm
from django.shortcuts import render, redirect
from .models import Member
from django.contrib.auth.hashers import make_password

#登入
def logins(request):
    if request.user.is_active:  # 確認用戶是否已經登入
        return redirect('home')
    msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # 驗證用戶名和密碼
        
        if user is not None:
            login(request, user)  # 登入用戶
            return redirect('home')  # 登入成功後重定向到首頁
        else:
            msg = '帳號或密碼錯誤'  # 設定錯誤訊息
            return render(request, 'login.html', {'msg': msg})  # 將錯誤訊息傳遞給模板
    return render(request, 'login.html')
    

#登出
def logout(request):
    auth.logout(request)
    message = f'成功登出'
    return redirect('login')

#搜尋
def search(request):
    kw = request.POST.get('q')#抓表單的東西(看你header的名字)
    products = Product.objects.filter(name__icontains=kw)#name__icontains 要以name這個欄位做相似查詢相似查詢
    return render(request, 'search.html', {'products': products, 'keyWord': kw})

#註冊
def register(request):
    if request.method == 'POST':
        # 從 POST 請求中獲取表單數據
        name = request.POST.get('name')
        borndate = request.POST.get('borndate')
        gender = request.POST.get('gender')
        gender = 'M' if gender == 'male' else 'W'
        phoneNum = request.POST.get('phoneNum')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # 檢查密碼是否一致
        if password != confirm_password:
            return render(request, 'register.html', {'error': '密碼與確認密碼不一致'})
        
        # 創建會員對象並保存到資料庫中
        member = Member.objects.create_user(
            username=name,
            borndate=borndate,
            gender=gender,
            phoneNum=phoneNum,
            email=email,
            password=password
        )
        
        # 重定向到註冊成功頁面或其他適當的頁面
        return redirect('/')
    else:
        # 如果不是 POST 請求，返回空的註冊表單
        return render(request, 'register.html')

def evaluate(request):
    return render(request,'evaluate.html')

#產品
def product(request):
    products = Product.objects.all()
    return render(request, "product.html", {'products': products})
def showproduct(request, id):
	try:
		product = Product.objects.get(id = id)
		if product != None:
			return render(request, 'product.html', locals())
	except:
		return redirect('/')
     
    
def home(request):
    items = Product.objects.all()
    return render(request, 'home.html', {'items': items}) 
def man(request):
    mans_products = Product.objects.filter(category='man')
    return render(request, 'man.html', {'mans_products': mans_products})
def girl(request):
    girls_products = Product.objects.filter(category='woman')
    return render(request, 'girl.html', {'girls_products': girls_products})
def child(request):
    childs_products = Product.objects.filter(category='child')
    return render(request, 'child.html', {'childs_products': childs_products})
def jewelry(request):
    jewelrys_products = Product.objects.filter(category='jewelry')
    return render(request, 'jewelry.html', {'jewelrys_products': jewelrys_products})
def shoe(request):
    shoes_products = Product.objects.filter(category='shoe')
    return render(request, 'shoe.html', {'shoes_products': shoes_products})


def mine(request):
    return render(request, "mine.html") 




def shopcar(request):
    return render(request,"shopcar.html")
def order(request):
    return render(request,"order.html")

def pay(request):
     return render(request,"pay.html")


'''我回家研究
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

@login_required(login_url='/login/') 
def profile(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            username = request.user.username
            try:
                user = User.objects.get(username=username)
                userinfo = Profile.objects.get(user=user)
                # 從 Profile 對象中提取欄位數據
                initial_data = {
                    'field1': userinfo.field1,
                    'field2': userinfo.field2,
                    # 添加更多欄位
                }
                form = {
                    'field1': userinfo.field1,
                    'field2': userinfo.field2,
                    # 添加更多欄位
                } 
            except Profile.DoesNotExist:
                form = {
                    'field1': '',
                    'field2': '',
                    # 添加更多欄位
                } 
        return render(request, 'userinfo.html', {'form': form})  # 渲染表單

    elif request.method == 'POST':
        username = request.user.username
        user = User.objects.get(username=username)
        try:
            userinfo = Profile.objects.get(user=user)
            form = {
                'field1': request.POST.get('field1'),
                'field2': request.POST.get('field2'),
                # 添加更多欄位
            }
            # 更新現有 Profile 對象
            userinfo.field1 = form['field1']
            userinfo.field2 = form['field2']
            # 更新更多欄位
            userinfo.save()
            message = '成功更新個人資料！'
        except Profile.DoesNotExist:
            form = {
                'field1': request.POST.get('field1'),
                'field2': request.POST.get('field2'),
                # 添加更多欄位
            }
            # 創建新的 Profile 對象
            userinfo = Profile(
                user=user,
                field1=form['field1'],
                field2=form['field2'],
                # 添加更多欄位
            )
            userinfo.save()
            message = '成功新增！'
        return render(request, 'userinfo.html', {'form': form, 'message': message})
    else:
        message = "ERROR"
        print('出錯回首頁')
        return redirect("/")  # 如果請求不是 GET 或 POST，則重定向到首頁
        
        
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>使用者資料</title>
</head>
<body>
    <h1>使用者資料</h1>
    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
    <form method="POST">
        {% csrf_token %}
        <label for="field1">欄位1：</label>
        <input type="text" id="field1" name="field1" value="{{ form.field1 }}"><br>
        <label for="field2">欄位2：</label>
        <input type="text" id="field2" name="field2" value="{{ form.field2 }}"><br>
        <!-- 添加更多欄位 -->
        <input type="submit" value="儲存">
    </form>
</body>
</html>

'''