# from django.shortcuts import render
# 
# from django.http import HttpResponse
# from datetime import datetime
# 
# # Create your views here.
# 
# 
# def home(request):
#     # return HttpResponse('Hello, world')
#     return render(request, 'home/welcome.html', {'today': datetime.today()})
#     # return render(request, 'home/welcome.html', {})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

# def home(request):
#     return render(request, 'home/welcome.html', {'today': datetime.today()})
# 
# 
# # back to admin (log in) page if you are not authorized
# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})
