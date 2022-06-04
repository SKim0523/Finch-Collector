from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from .models import Finch, Comment, List
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lists"] = List.objects.all() 
        return context
     
@method_decorator(login_required, name='dispatch')
class FinchList(TemplateView):
    template_name = "finch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["finches"] = Finch.objects.filter(name__icontains=name)
        else:
            context["finches"] = Finch.objects.all()
        return context
    
class CommentCreate(View):
     def post(self, request, pk):
        content = request.POST.get('content')
        finch = Finch.objects.get(pk = pk)
        Comment.objects.create(content = content, finch = finch)
        return redirect('finch_detail', pk = pk)

class CommentUpdate(UpdateView):
    model = Comment
    fields = ['content']
    template_name = "content_update.html"
    success_url = '/finches/'  
      
class CommentDelete(DeleteView):
    model = Comment
    template_name = "content_delete.html"
    success_url = '/finches/'  
  
class FinchDetails(DetailView):
    model = Finch
    template_name = "finch_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lists"] = List.objects.all()
        return context
    
class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'img', 'description']
    template_name = "finch_create.html"
    success_url = '/finches/'      

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'img', 'description']
    template_name = "finch_update.html"
    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})  
    
class FinchDelete(DeleteView):
    model = Finch
    template_name = "finch_delete.html"
    success_url = '/finches/'  

class ListFinchAssoc(View):

    def get(self, request, pk, finch_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            List.objects.get(pk=pk).finches.remove(finch_pk)
        if assoc == "add":
            List.objects.get(pk=pk).finches.add(finch_pk)
        return redirect('home')

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("finch_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
