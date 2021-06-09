from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *


@unathenticated_user
def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        users = CreateUserForm()

        if request.method == 'POST':
            users = CreateUserForm(request.POST)
            if users.is_valid():
                users.save()
                messages.success(request, "Account is created successfully")
                return redirect('login')
        return render(request, 'mobile_company/RegisterPage.html', {'users': users})


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
        return render(request, 'mobile_company/LoginPage.html')


def Logout(request):
    logout(request)
    return redirect('login')


@allowed_users(allowed_users=['admin', 'users', 'manager', ''])
@login_required(login_url='login')
def home(request):

    providers = Providers.objects.all()

    context = {'providers': providers}

    return render(request, 'mobile_company/home.html', context)


@allowed_users(allowed_users=['admin', 'manager'])
def ProvidersCreate(request):

    p_forms = ProvidersCreateForm()

    if request.method == 'POST':
        p_form = ProvidersCreateForm(request.POST)
        if p_form.is_valid():
            p_form.save()
            return redirect('/')
    return render(request, 'mobile_company/providers_create.html', {'p_forms': p_forms})


@login_required(login_url='login')
@allowed_users(allowed_users=['admin', 'manager'])
def dealers(request):

    dealers = Dealers.objects.all()

    return render(request, 'mobile_company/dealers.html', {'dealers': dealers})


@allowed_users(allowed_users=['admin', 'manager'])
def dealersCreate(request):

    d_forms = DealersCreateForm()

    if request.method == 'POST':
        d_form = DealersCreateForm(request.POST)
        if d_form.is_valid():
            d_form.save()
            return redirect('dealers')
    return render(request, 'mobile_company/dealers_create.html', {'d_forms': d_forms})


@allowed_users(allowed_users=['admin', 'manager'])
def dealersUpdate(request, pk):

    dealers = Dealers.objects.get(id=pk)
    d_forms = DealersForm(instance=dealers)

    if request.method == 'POST':
        d_form = DealersForm(request.POST, instance=dealers)
        if d_form.is_valid():
            d_form.save()
            return redirect('dealers')
    return render(request, 'mobile_company/dealers_update.html', {'d_forms': d_forms})


@allowed_users(allowed_users=['admin'])
def dealersDelete(request, pk):

    dealers = Dealers.objects.get(id=pk)
    if request.method == 'POST':
        dealers.delete()
        return redirect('dealers')
    return render(request, 'mobile_company/dealers_delete.html', {'dealers': dealers})


@allowed_users(allowed_users=['admin', 'manager'])
@login_required(login_url='login')
def NumberCode(request):

    number_code = NumberCodes.objects.all()

    return render(request, 'mobile_company/number_code.html', {'number_code': number_code})


@allowed_users(allowed_users=['admin', 'manager'])
def NumberCodeCreate(request):

    n_c_forms = NumberCodeCreateForm()

    if request.method == 'POST':
        n_c_form = NumberCodeCreateForm(request.POST)
        if n_c_form.is_valid():
            n_c_form.save()
            return redirect('NumberCode')
    return render(request, 'mobile_company/number_code_create.html', {'n_c_forms': n_c_forms})


@allowed_users(allowed_users=['admin', 'manager'])
def NumberCodeUpdate(request, pk):

    number_code = NumberCodes.objects.get(id=pk)
    n_c_form = NumberCodeForm(instance=number_code)

    if request.method == 'POST':
        n_c_form = NumberCodeForm(request.POST, instance=number_code)
        if n_c_form.is_valid():
            n_c_form.save()
            return redirect('NumberCode')
    return render(request, 'mobile_company/number_code_update.html', {'n_c_form': n_c_form})


@allowed_users(allowed_users=['admin'])
def NumberCodeDelete(request, pk):

    number_code = NumberCodes.objects.get(id=pk)
    if request.method == 'POST':
        number_code.delete()
        return redirect('NumberCode')
    return render(request, 'mobile_company/number_code_delete.html', {'number_code': number_code})


@allowed_users(allowed_users=['admin', 'manager'])
def phonenumbers(request, pk):

    number_codes = NumberCodes.objects.get(id=pk)
    phone_numbers = PhoneNumbers.objects.filter(numbercode=number_codes)

    context = {'phone_numbers': phone_numbers, 'number_codes': number_codes}
    
    return render(request, 'mobile_company/phone_numbers.html', context)


@allowed_users(allowed_users=['admin', 'manager'])
def PhoneNumbersCreate(request, pk):

    PhoneNumbersFormSet = inlineformset_factory(NumberCodes, PhoneNumbers, fields=('phonenumber', 'categoryname',), extra=5)
    numbercode = NumberCodes.objects.get(id=pk)
    p_n_forms = PhoneNumbersFormSet(queryset=PhoneNumbers.objects.none(), instance=numbercode)

    # p_n_forms = PhoneNumbersCreateForm(initial={'numbercode': numbercode})

    if request.method == 'POST':
        p_n_forms = PhoneNumbersFormSet(request.POST, instance=numbercode)
        # p_n_forms = PhoneNumbersCreateForm(request.POST)
        if p_n_forms.is_valid():
            p_n_forms.save()
            return redirect('NumberCode')
    return render(request, 'mobile_company/phone_numbers_create.html', {'p_n_forms': p_n_forms})


@allowed_users(allowed_users=['admin', 'manager'])
def PhoneNumbersUpdate(request, pk):

    phonenumbers = PhoneNumbers.objects.get(id=pk)
    p_n_forms = PhoneNumbersform(instance=phonenumbers)

    if request.method == 'POST':
        p_n_form = PhoneNumbersform(request.POST, instance=phonenumbers)
        if p_n_form.is_valid():
            p_n_form.save()
            return redirect('NumberCode')
    return render(request, 'mobile_company/phone_numbers_update.html', {'p_n_forms': p_n_forms})


@allowed_users(allowed_users=['admin'])
def PhoneNumbersDelete(request, pk):

    phone_numbers = PhoneNumbers.objects.get(id=pk)
    if request.method == 'POST':
        phone_numbers.delete()
        return redirect('NumberCode')
    return render(request, 'mobile_company/phone_numbers_delete.html', {'phone_numbers': phone_numbers})


@allowed_users(allowed_users=['admin', 'manager'])
@login_required(login_url='login')
def customer(request):

    customer = Customer.objects.all()

    return render(request, 'mobile_company/customer.html', {'customer': customer,})


@allowed_users(allowed_users=['admin', 'manager'])
def CustomerCreate(request):

    c_forms = CustomerCreateForm()

    if request.method == 'POST':
        c_form = CustomerCreateForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            return redirect('customer')
    return render(request, 'mobile_company/customer_create.html', {'c_forms': c_forms})


@allowed_users(allowed_users=['admin', 'manager'])
def CustomerUpdate(request, pk):

    customer = Customer.objects.get(id=pk)
    c_forms = CustomerForm(instance=customer)

    if request.method == 'POST':
        c_form = CustomerForm(request.POST, instance=customer)
        if c_form.is_valid():
            c_form.save()
            return redirect('customer')
    return render(request, 'mobile_company/customer_update.html', {'c_forms': c_forms})


@allowed_users(allowed_users=['admin'])
def CustomerDelete(request, pk):

    customer = Customer.objects.get(id=pk)

    if request.method == 'POST':
        customer.delete()
        return redirect('customer')
    return render(request, 'mobile_company/customer_delete.html', {'customer': customer})


@allowed_users(allowed_users=['admin', 'manager'])
@login_required(login_url='login')
def category(request):

    category = Category.objects.all()

    return render(request, 'mobile_company/category.html', {'category': category})


@allowed_users(allowed_users=['admin', 'manager'])
def CategoryCreate(request):

    c_forms = CategoryCreateForm()

    if request.method == 'POST':
        c_form = CategoryCreateForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            return redirect('category')
    return render(request, 'mobile_company/category_create.html', {'c_forms': c_forms})


@allowed_users(allowed_users=['admin', 'manager'])
def CategoryUpdate(request, pk):

    category = Category.objects.get(id=pk)
    c_forms = CategoryForm(instance=category)

    if request.method == 'POST':
        c_form = CategoryForm(request.POST, instance=category)
        if c_form.is_valid():
            c_form.save()
            return redirect('category')
    return render(request, 'mobile_company/category_update.html', {'c_forms': c_forms})


@allowed_users(allowed_users=['admin'])
def CategoryDelete(request, pk):

    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category')
    return render(request, 'mobile_company/category_delete.html', {'category': category})


@allowed_users(allowed_users=['admin', 'manager'])
def tariff(request, pk):

    providers = Providers.objects.get(id=pk)
    tariff = Tarif.objects.filter(tarifprovider=providers)

    return render(request, 'mobile_company/tariff.html', {'tariff': tariff, 'providers': providers})


@allowed_users(allowed_users=['admin', 'manager'])
def TariffCreate(request, pk):

    provider = Providers.objects.get(id=pk)

    t_forms = TariffCreateForm(initial={'provider': provider})

    if request.method == 'POST':
        t_form = TariffCreateForm(request.POST)
        if t_form.is_valid():
            t_form.save()
            return redirect('home')
    return render(request, 'mobile_company/tariff_create.html', {'t_forms': t_forms})


@allowed_users(allowed_users=['admin', 'manager'])
def TariffUpdate(request, pk):

    tariff = Tarif.objects.get(id=pk)
    t_forms = TariffForm(instance=tariff)

    if request.method == 'POST':
        c_form = TariffForm(request.POST, instance=tariff)
        if c_form.is_valid():
            c_form.save()
            return redirect('/')
    return render(request, 'mobile_company/tariff_update.html', {'t_forms': t_forms})


@allowed_users(allowed_users=['admin'])
def TariffDelete(request, pk):

    tariff = Tarif.objects.get(id=pk)
    if request.method == 'POST':
        tariff.delete()
        return redirect('home')
    return render(request, 'mobile_company/tariff_delete.html', {'tariff': tariff})


def UserPage(request):

    return render(request, 'mobile_company/UserPage.html')


def BeelinePage(request):

    numbers1 = NumberCodes.objects.get(code='90')
    phonenumbers = PhoneNumbers.objects.filter(numbercode=numbers1)

    return render(request, 'mobile_company/BeelinePage.html', {'phonenumbers': phonenumbers, 'numbers1': numbers1})


def UzmobilePage(request):

    numbers1 = NumberCodes.objects.get(code='99')
    phonenumbers = PhoneNumbers.objects.filter(numbercode=numbers1)

    return render(request, 'mobile_company/UzmobilePage.html', {'phonenumbers': phonenumbers})


def UcellPage(request):

    numbers1 = NumberCodes.objects.get(code='93')
    phonenumbers = PhoneNumbers.objects.filter(numbercode=numbers1)

    return render(request, 'mobile_company/UcellPage.html', {'phonenumbers': phonenumbers})


def MobiuzPage(request):

    numbers1 = NumberCodes.objects.get(code='97')
    phonenumbers = PhoneNumbers.objects.filter(numbercode=numbers1)

    return render(request, 'mobile_company/MobiuzPage.html', {'phonenumbers': phonenumbers})


def HumansPage(request):

    numbers1 = NumberCodes.objects.get(code='33')
    phonenumbers = PhoneNumbers.objects.filter(numbercode=numbers1)

    return render(request, 'mobile_company/HumansPage.html', {'phonenumbers': phonenumbers,})


def BuyNumber(request, pk):

    phonenumbers = PhoneNumbers.objects.get(id=pk)


    o_forms = OrderForm(initial={'phonenumber': phonenumbers})

    if request.method == 'POST':
        o_form = OrderForm(request.POST)
        if o_form.is_valid():
            o_form.status = True
            o_form.save()
            p = PhoneNumbers.objects.get(id=pk)
            p.status = True
            p.save()
            return redirect('UserPage')

    return render(request, 'mobile_company/BuyNumber.html', {'o_forms': o_forms, 'phonenumbers': phonenumbers,})

    # def PhoneNumbersUpdate(request, pk):

    # phonenumbers = PhoneNumbers.objects.get(id=pk)
    # p_n_forms = PhoneNumbersform(instance=phonenumbers)

    # if request.method == 'POST':
    #     p_n_form = PhoneNumbersform(request.POST, instance=phonenumbers)
    #     if p_n_form.is_valid():
    #         p_n_form.save()
    #         return redirect('NumberCode')
    # return render(request, 'mobile_company/phone_numbers_update.html', {'p_n_forms': p_n_forms})





