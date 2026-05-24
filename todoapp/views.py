from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView,FormView

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import task
# Create your views here.
class Tasklist(LoginRequiredMixin,ListView):
    model = task
    context_object_name = "tasks"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        #print(context)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        #context["programing"] = "python"
        
    

        searchInputText = self.request.GET.get("search") or ""
        if searchInputText:
            context["tasks"] = context["tasks"].filter(title__startswith=searchInputText)
        context["search"] = searchInputText
        return context

class taskdetail(LoginRequiredMixin,DetailView):
    model = task
    context_object_name = "task"

class taskcreate(LoginRequiredMixin,CreateView):
    model = task
    fields = ["title","description","completed"]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
        
class taskupdate(LoginRequiredMixin,UpdateView):
    model = task
    fields = "__all__"
    success_url = reverse_lazy("tasks")

class deletetask(LoginRequiredMixin,DeleteView):
    model = task
    fields = "__all__"
    success_url = reverse_lazy("tasks")

class tasklistloginview(LoginView):
    fields = "__all__"
    template_name = "todoapp/login.html"

    def get_success_url(self):
        return reverse_lazy("tasks")


class registertodoapp(FormView):
    template_name="todoapp/register.html"
    form_class=UserCreationForm
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super().form_valid(form)

