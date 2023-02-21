from django.shortcuts import render
from .forms import UserReg


def reg(request):
    submit_button = request.POST.get("mark")
    name = ''
    email = ''
    password = ''

    reg_form = UserReg(request.POST or None)
    if reg_form.is_valid():
        name = reg_form.cleaned_data.get("name")
        email = reg_form.cleaned_data.get("email")
        password = reg_form.cleaned_data.get("password")
    context = {'reg_form': reg_form, 'name': name, 'email': email, 'password': password, 'submit_button': submit_button}
    return render(request, 'register.html', context)
