from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .form import UserCreationSelfForm, RecordForm,AmountSetUpForm,AddForm,SubForm
from django.shortcuts import HttpResponseRedirect, render
from django.contrib import messages
from .models import OurRecord
from . import selfmadeform as smf
from datetime import datetime
from zoneinfo import ZoneInfo
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
fake_mail = ['nitin@gmail.com', 'nitin1@gmail.com','nitin2@gmail.com','dipendra@gmail.com','dipendra2gmail.com','dipendra2@gmail.com','unknownone@gmail.com','unknowntwo@gmail.com']


# Create your views here.
def bookeeping(request):
    return render(request, 'record/book.html')


def home(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = RecordForm(request.POST)
            if fm.is_valid():
                print("hello")
                it = fm.cleaned_data['item']
                ti = fm.cleaned_data['time']
                sh = fm.cleaned_data['shop']
                pr = fm.cleaned_data['price']

                id, ta, tc = smf.get_amount(str(request.user))

                tc += pr
                ta = round(ta, 5)
                tc = round(tc, 5)
                tl = ta - tc
                if tl < 0:
                    messages.warning(request, "You don't have that much amount")
                    return HttpResponseRedirect('/home')


                if not smf.save(ti, str(request.user), it, sh, pr):

                    print("error occur")
                    messages.warning(request, "Some error occurred")
                else:
                    fm = RecordForm()
                    data = smf.get_data(str(request.user))

                    smf.update_amount(str(request.user),ta,tc)
                    messages.success(request,"Added an record successfully")
                    tm = datetime.now(tz=ZoneInfo('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S")
                    return render(request, 'record/home.html', { 'tim':tm,  'form': fm, 'dt': data ,'total_amount': ta,'amount_consumed':tc,'amount_left':tl})
            else:
                print("not valid data")
                pass


        else:
            fm = RecordForm()

        data = smf.get_data(str(request.user))
        id,ta,tc = smf.get_amount(str(request.user))
        tl = ta-tc
        tl = round(tl,5)
        tm = datetime.now(tz=ZoneInfo('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S")
        return render(request, 'record/home.html', {'tim':tm,  'form': fm, 'dt': data ,'total_amount': ta,'amount_consumed':tc,'amount_left':tl})
    else:
        return HttpResponseRedirect("/login")


def learn_func(request):
    if request.user.is_authenticated:
        return render(request,'record/learn.html')
    return HttpResponseRedirect("/login")

def explore_func(request):
    if request.user.is_authenticated:
        return render(request,'record/explore.html')
    return HttpResponseRedirect("/login")

def about_func(request):
    return render(request,'record/about.html')

def signup_func(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = UserCreationSelfForm(request.POST)
            if fm.is_valid():

                un = fm.cleaned_data['username']

                gl = fm.cleaned_data['email']

                try:
                    validate_email(gl)
                except:
                    if gl not in fake_mail:

                        messages.warning(request, "You haven't enter the correct details")

                        print("invaid email")
                        return render(request, 'record/signup.html', {'form': fm})

                print("valid mail")
                fm.save()

                smf.create_form(str(un))
                smf.save_amount(str(un),0,0)
                return HttpResponseRedirect('/login')
            else:
                messages.warning(request, "You haven't enter the correct details")

        else:
            fm = UserCreationSelfForm()
        return render(request, 'record/signup.html', {'form': fm})
    else:
        return HttpResponseRedirect('/home')


def signin_func(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                un = fm.cleaned_data['username']
                pw = fm.cleaned_data['password']

                user = authenticate(username=un, password=pw)
                if user is not None:
                    login(request, user)

                    return HttpResponseRedirect('/home')
                else:
                    messages.success(request, "Either username or password is invalid.")
        else:
            fm = AuthenticationForm()

        return render(request, "record/signin.html", {'form': fm})
    else:
        return HttpResponseRedirect('/home')


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/login')



def set_amount_func(request):
    if request.method=="POST":
        fm = AmountSetUpForm(request.POST)
        if fm.is_valid():

            ta = fm.cleaned_data['total_amount']
            tc = fm.cleaned_data['total_consumed']
            if tc!=0:
                messages.warning(request,"Initially total consumed should be 0")
                return HttpResponseRedirect('/set_amount')

            ta,tc = round(ta,5),round(tc,5)
            smf.update_amount(str(request.user),ta,tc)
            smf.clear_data(str(request.user))
            return HttpResponseRedirect('/home')
        else:
            print("error coming")
            pass
    else:
        fm = AmountSetUpForm()
    return render(request,'record/amount.html',{'form':fm})



def modify_amount_func(request,my_id):
    if request.method=="POST":
        if my_id==1:
            fm = AddForm(request.POST)
        if my_id==2:
            fm = SubForm(request.POST)

        if fm.is_valid():
            id,ta,tc = smf.get_amount(str(request.user))
            if my_id==1:
                val = fm.cleaned_data['add_amount']
                ta += val
            if my_id==2:
                val = fm.cleaned_data['sub_amount']
                if val>(ta-tc):
                    messages.warning(request,"You can't subtract more than present")
                    return HttpResponseRedirect('/modify_amount/1')
                ta-=val
            ta = round(ta,5)
            tc = round(tc,5)
            smf.update_amount(str(request.user),ta,tc)
            return HttpResponseRedirect('/home')

    return render(request,'record/modify.html')