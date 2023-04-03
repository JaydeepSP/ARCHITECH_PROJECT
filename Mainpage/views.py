from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import AccountData,DesignData,AppointmentData,contactform,Temp_appointment,PaymentData,TempPayment
import stripe


def Homepage(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("pass")
        acctype = request.POST.get("acctype")
        print(acctype)
        cpass = request.POST.get("cpass")
        if password == cpass:
            myuser = User.objects.create_user(email,mobile,password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            user = authenticate(username = email,password = password)
            login(request,user)
            account_data = AccountData(acc_id = request.user.id,email = email,acc_type = acctype)
            account_data.save()
            messages.success(request,"You are Logged in successfully")
            type = acctype
            return render(request,"Mainpage/index.html",{"type":type})
        else:
            messages.warning(request,"Password is not matched ")
            return redirect("/password/")
    if request.user.is_authenticated == True:
        accout_data = AccountData.objects.filter(email = request.user).values()[0]
        type = accout_data["acc_type"]
        return render(request,"Mainpage/index.html",{"type":type})
    else:
        return render(request,"Mainpage/index.html")

def AboutPage(request):
    if request.user.is_authenticated == True:
        accout_data = AccountData.objects.filter(email = request.user).values()[0]
        type = accout_data["acc_type"]
        return render(request,"Mainpage/about.html",{"type":type})
    else:
        return render(request,"Mainpage/about.html")

def DesignPage(request):
    if request.user.is_authenticated == True:
        accout_data = AccountData.objects.filter(email = request.user).values()[0]
        type = accout_data["acc_type"]
        design_data = DesignData.objects.filter(user_type = "Architech").all().values()
        return render(request,"Mainpage/design.html",{"type":type,"design_data":design_data})
    else:
        return redirect("/login/")

def ProfilePage(request):
    if request.user.is_authenticated==True:
        accout_data = AccountData.objects.filter(email = request.user).values()[0]
        type = accout_data["acc_type"]
        designs = DesignData.objects.filter(user_id = request.user.id).values()
        return render(request,"Mainpage/profile.html",{"type":type,"designs":designs})
    else:
        return redirect("/login/")

def AddDesignPage(request):
    if request.user.is_authenticated == True:
        accout_data = AccountData.objects.filter(email = request.user).values()[0]
        type = accout_data["acc_type"]
        if request.method == "POST":
            design_type = request.POST.get("design_type")
            design_desc = request.POST.get("design_desc")
            project_name = request.POST.get("project_name")
            design_data = DesignData()
            design_data.user_id = request.user.id
            design_data.design_type = design_type
            design_data.design_desc = design_desc
            design_data.project_name = project_name
            design_data.user_type = type
            if len(request.FILES) != 0:
                design_data.design_img = request.FILES['design_img']
            design_data.save()
        customer_data = AccountData.objects.filter(acc_type = "Consumer").all().values()
        users_data = []
        for i in customer_data:
            mydic = {}
            user_data = User.objects.filter(username = i["email"]).values()[0]
            mydic["id"] = user_data["id"]
            mydic["first_name"] = user_data["first_name"]
            mydic["last_name"] = user_data["last_name"]
            mydic["email"] = user_data["username"]
            mydic["mobile"] = user_data["email"]
            users_data.append(mydic)
        return render(request,"Mainpage/add-design.html",{"type":type,"customer_data":users_data})
    else:
        messages.warning(request,"First login after then book the consulatation")
        return redirect("/login/")

def MyDesignPage(request,id):
    if request.user.is_authenticated == True:
        accout_data = AccountData.objects.filter(email = request.user).values()[0]
        type = accout_data["acc_type"]
        design_data = DesignData.objects.filter(id = id).values()
        design_list = []
        for i in design_data:
            mydic = {}
            mydic["id"] = i["id"]
            mydic["design_img"] = i["design_img"]
            mydic["design_type"] = i["design_type"]
            mydic["project_name"] = i["project_name"]
            mydic["design_desc"] = i["design_desc"]
            mydic["user_type"] = i["user_type"]
            user_id = i["user_id"]
            user_data = User.objects.filter(id = user_id).values()[0]
            mydic["user_id"] = i["user_id"]
            mydic["email"] = user_data["username"]
            mydic["first_name"] = user_data["first_name"]
            mydic["last_name"] = user_data["last_name"]
            mydic["mobile"] = user_data["email"]
            design_list.append(mydic)
        return render(request,"Mainpage/mydesign.html",{"design_data":design_list,"type":type})
    else:
        return redirect("/login/")

def UserInformation(request,id):
    if request.user.is_authenticated==True:
        accout_data = AccountData.objects.filter(acc_id = request.user.id).values()[0]
        type = accout_data["acc_type"]
        user_data = User.objects.filter(id = id).values()
        designs = DesignData.objects.filter(user_id = id).values()
        type_data = AccountData.objects.filter(acc_id = id).values()[0]
        account_type = type_data["acc_type"]
        fees = type_data["architech_fees"]
        return render(request,"Mainpage/user-info.html",{"type":type,"accounts_data":user_data,"account_type":account_type,"designs":designs,"user_id":id,"fees":fees})
    else:
        return redirect("/login/")

def MainUserInfo(request,id):
    if request.user.is_authenticated==True:
        accout_data = AccountData.objects.filter(acc_id = request.user.id).values()[0]
        type = accout_data["acc_type"]
        user_data = User.objects.filter(id = id).values()
        designs = DesignData.objects.filter(user_id = id).values()
        type_data = AccountData.objects.filter(acc_id = id).values()[0]
        account_type = type_data["acc_type"]
        fees = type_data["architech_fees"]
        return render(request,"Mainpage/main-user-info.html",{"type":type,"accounts_data":user_data,"account_type":account_type,"designs":designs,"user_id":id,"fees":fees})
    else:
        return redirect("/login/")

def All_User(request):
    if request.user.is_authenticated:
        accout_data = AccountData.objects.filter(acc_id = request.user.id).values()[0]
        type = accout_data["acc_type"]
        user_type = AccountData.objects.filter(acc_id = request.user.id).values()[0]["acc_type"]
        if user_type == "Architech":
            account_data = AccountData.objects.filter(acc_type = "Consumer").all().values()
            user_list = []
            for i in account_data:
                mydic = {}
                id = i["acc_id"]
                mydic["id"] = id
                user_data = User.objects.filter(id = id).values()[0]
                mydic["first_name"] = user_data["first_name"]
                mydic["last_name"] = user_data["last_name"]
                mydic["number"] = user_data["email"]
                mydic["email"] = user_data["username"]
                mydic["acc_type"] = i["acc_type"]
                user_list.append(mydic)
            return render(request,"Mainpage/all_user.html",{"user_list":user_list,"type":type})
        else:
            account_data = AccountData.objects.filter(acc_type = "Architech").all().values()
            user_list = []
            for i in account_data:
                mydic = {}
                id = i["acc_id"]
                mydic["id"] = id
                user_data = User.objects.filter(id = id).values()[0]
                mydic["first_name"] = user_data["first_name"]
                mydic["last_name"] = user_data["last_name"]
                mydic["number"] = user_data["email"]
                mydic["email"] = user_data["username"]
                user_list.append(mydic)
            return render(request,"Mainpage/all_user.html",{"user_list":user_list,"type":type})
    else:
        return redirect("/login/")

def Appointments(request):
    if request.user.is_authenticated:
        accout_data = AccountData.objects.filter(acc_id = request.user.id).values()[0]
        payment_data = PaymentData.objects.all()
        type = accout_data["acc_type"]
        appointment_data = AppointmentData.objects.filter(user_id = request.user.id).all().values()
        return render(request,"Mainpage/appointment.html",{"appointment_data":appointment_data,"type":type,"payment_data":payment_data})
    else:
        return redirect("/login/")

def PendingAppointment(request):
    if request.user.is_authenticated:
        accout_data = AccountData.objects.filter(acc_id = request.user.id).values()[0]
        type = accout_data["acc_type"]
        appointments = AppointmentData.objects.filter(architech_id = request.user.id).all().values()
        if request.method == "POST":
            id = request.POST.get("id")
            data = id.split(" ")
            AppointmentData.objects.filter(id = data[0]).update(status = data[1])
            return redirect("/pending-app/")
        return render(request,"Mainpage/pending-app.html",{"appointment_data":appointments,"type":type})
    else:
        return redirect("/login/")
    
def Contract_Status(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id = request.POST.get("id")
            data = id.split(" ")
            AppointmentData.objects.filter(id = data[0]).update(status = data[1])
            return redirect("/pending-app/")
    else:
        return redirect("/login/")
    
def PaymentManager(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            appointment_id = int(request.POST.get("appointment_id"))
            user_id = int(request.POST.get("user_id"))
            architech_id = int(request.POST.get("architech_id"))
            payment = request.POST.get("payment")
            payments_data = PaymentData(appointment_id = appointment_id,user_id = user_id,architech_id = architech_id,payment = payment)
            payments_data.save()
            AppointmentData.objects.filter(id = appointment_id).update(status = "Payment-Pending")
            return redirect("/pending-app/")
    else:
        return redirect("/login/")

def Edit_Profile(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        AccountData.objects.filter(email = request.user).update(email = email)
        User.objects.filter(username = request.user).update(first_name = fname)
        User.objects.filter(username = request.user).update(last_name = lname)
        User.objects.filter(username = request.user).update(username = email)
        messages.success(request,"Your profile succeessfully updated")
        return redirect("/profile/")
    return render(request,"Mainpage/edit-profile.html")

def ContactPage(request):
    if request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")
        contactforms = contactform(email_id = email,message=message)
        contactforms.save()
    return render(request,"Mainpage/contact.html")

stripe.api_key = 'sk_test_51MedHmSHJDFuPL5cnRItHVU94xOAzKltL5vuoADjGI0wZfVNRtCwU3I3eKgvtQUF0z3w2yl5IuQ5rRZcOs9m2ytj00YSZRJhjw'
def Checkout(request):
    if request.user.is_authenticated:
        temp_data = Temp_appointment()
        if request.method == "POST":
            app_date = request.POST.get("app_date")
            start_time = request.POST.get("start_time")
            end_time = request.POST.get("end_time")
            app_desc = request.POST.get("design_desc")
            architech_id = request.POST.get("user_id")
            appointment_fees = int(request.POST.get("architech_fees"))
            user_id = request.user.id
            temp_data.user_id = user_id
            temp_data.appointment_date = app_date
            temp_data.start_time = start_time
            temp_data.end_time = end_time
            temp_data.appointment_desc = app_desc
            temp_data.architech_id = architech_id
            temp_data.save()
            full_name = User.objects.filter(id = architech_id).values()[0]["first_name"] + " " + User.objects.filter(id = architech_id).values()[0]["last_name"]
            session = stripe.checkout.Session.create(
            line_items=[{
              'price_data': {
                'currency': 'inr',
                'product_data': {
                  'name': full_name,
                },
                'unit_amount': int(appointment_fees*100),
              },
              'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/success',
            cancel_url='http://127.0.0.1:8000/cancel',
            )
            return redirect(session.url, code=303)
    else:
        return redirect("/login/")
    

def PaymentCheckout(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            amount = int(request.POST.get("amount"))/2
            app_id = request.POST.get("app_id")
            arc_id = request.POST.get("arc_id")
            temp_payment = TempPayment(amount = amount,app_id = app_id,architech_id = arc_id)
            temp_payment.save()
            architech_name = request.POST.get("architech_name")
            session = stripe.checkout.Session.create(
            line_items=[{
              'price_data': {
                'currency': 'inr',
                'product_data': {
                  'name': architech_name,
                },
                'unit_amount': int(amount*100),
              },
              'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/paymentsuccess',
            cancel_url='http://127.0.0.1:8000/cancel',
            )
            return redirect(session.url, code=303)
    else:
        return redirect("/login/")

def Paymentsuccess(request):
    accout_data = AccountData.objects.filter(acc_id = request.user.id).values()[0]
    type = accout_data["acc_type"]
    temp_data = TempPayment.objects.values()[0]
    payment_data = PaymentData(appointment_id = temp_data["app_id"],user_id = request.user.id,architech_id = temp_data["architech_id"],payment = temp_data["amount"])
    payment_data.save()
    AppointmentData.objects.filter(id = temp_data["app_id"]).update(status = "Payment Successfull")
    TempPayment.objects.all().delete()
    return render(request,"Mainpage/success.html",{"type":type})

def success_page(request):
    user = request.user
    accout_data = AccountData.objects.filter(acc_id = request.user.id).values()[0]
    type = accout_data["acc_type"]
    temp_data = Temp_appointment.objects.filter(user_id = user.id).values()[0]
    appointment = AppointmentData()
    appointments_data = AppointmentData.objects.filter()
    user_id = request.user.id
    appointment.appointment_date = temp_data["appointment_date"]
    appointment.start_time = temp_data["start_time"]
    appointment.end_time = temp_data["end_time"]
    appointment.appointment_desc = temp_data["appointment_desc"]
    appointment.architech_id = temp_data["architech_id"]
    appointment.user_id = user_id
    full_name = User.objects.filter(id = temp_data["architech_id"]).values()[0]["first_name"] + " " + User.objects.filter(id = temp_data["architech_id"]).values()[0]["last_name"]
    appointment.architech_name = full_name
    appointment.consumer_name = request.user.first_name + " " + request.user.last_name
    appointment.save()
    Temp_appointment.objects.filter(user_id = user.id).delete()
    return render(request,"Mainpage/success.html",{"type":type})

def cancle_page(request):
    accout_data = AccountData.objects.filter(acc_id = request.user.id).values()[0]
    type = accout_data["acc_type"]
    return render(request,"Mainpage/cancle.html",{"type":type})

def Logout(request):
    logout(request)
    return redirect("/")