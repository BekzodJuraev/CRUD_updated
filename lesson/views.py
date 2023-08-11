from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import logout
from .forms import MakeForm,LoginForm
from .models import CRUD
class CrudView(LoginRequiredMixin,ListView):
    model=CRUD
    template_name = 'list_view.html'
    login_url = reverse_lazy('login')




class Create(LoginRequiredMixin,CreateView):
    template_name='form_view.html'
    form_class=MakeForm
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')



class Update(LoginRequiredMixin,UpdateView):
    model = CRUD
    form_class = MakeForm
    template_name = 'updated_view.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

class Delete(LoginRequiredMixin,DeleteView):
    model = CRUD
    success_url = reverse_lazy("home")
    template_name = 'delete_view.html'
    login_url = reverse_lazy('login')








def login_page(request):
    next = request.GET.get('next')
    form = LoginForm(request.POST or None)
    logout(request)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }


    return render(request, "login.html", context)



def logout_view(request):
    logout(request)
    return redirect('login')