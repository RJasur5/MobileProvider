from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProvidersCreateForm(ModelForm):
    class Meta:
        model = Providers
        fields = "__all__"


class DealersCreateForm(ModelForm):
    class Meta:
        model = Dealers
        fields = "__all__"


class DealersForm(ModelForm):
    class Meta:
        model = Dealers
        fields = "__all__"


class NumberCodeCreateForm(ModelForm):
    class Meta:
        model = NumberCodes
        fields = "__all__"


class NumberCodeForm(ModelForm):
    class Meta:
        model = NumberCodes
        fields = "__all__"


class PhoneNumbersCreateForm(ModelForm):
    class Meta:
        model = PhoneNumbers
        fields = "__all__"


class PhoneNumbersform(ModelForm):
    class Meta:
        model = PhoneNumbers
        fields = "__all__"


class CustomerCreateForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class CategoryCreateForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class TariffCreateForm(ModelForm):
    class Meta:
        model = Tarif
        fields = "__all__"


class TariffForm(ModelForm):
    class Meta:
        model = Tarif
        fields = "__all__"


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

