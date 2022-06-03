from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
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


# Here we will be creating a class called Home and extending it from the View class
@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lists"] = List.objects.all() # this is where we add the key into our context object for the view to use
        return context
    
#...
class About(TemplateView):
    template_name = "about.html"

class FinchList(TemplateView):
    template_name = "index.html"
     
@method_decorator(login_required, name='dispatch')
class FinchList(TemplateView):
    template_name = "finch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["finches"] = Finch.objects.all() # this is where we add the key into our context object for the view to use
        return context
    
class CommentCreate(View):
     def post(self, request, pk):
        content = request.POST.get('content')
        finch = Finch.objects.get(pk = pk) #req.params.id
        Comment.objects.create(content = content, finch = finch)
        return redirect('finch_detail', pk = pk)

class CommentUpdate(UpdateView):
    model = Comment
    fields = ['content']
    template_name = "content_update.html"
    success_url = '/finches/' 
    # def get_success_url(self):
    #     return reverse('finch_detail', kwargs={'pk': self.object.pk})  
      
class CommentDelete(DeleteView):
    model = Comment
    template_name = "content_delete.html"
    success_url = '/finches/'  
  
class FinchDetails(DetailView):
    model = Finch
    template_name = "finch_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.all()
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
        # get the query param from the url
        assoc = request.GET.get("assoc") #.com/?add
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            List.objects.get(pk=pk).finches.remove(finch_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            List.objects.get(pk=pk).finches.add(finch_pk)
        return redirect('home')

class ListCreate(CreateView):
    model = List
    fields = ['name']
    template_name = 'list_create.html'
    success_url = '/'
    
class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("finch_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


# finches = [
#   Finch("Euphonia", "https://i.imgur.com/RcGBIKQ.png",
#           "Eeuphonia measures 10 cm (3.9 in). The male has entirely yellow underparts from throat to vent save for a small terminal patch of white on the undertail."),
#   Finch("Zebra Finch",
#           "https://i.imgur.com/u92r7pi.png", "The zebra finch, owl finch and Gouldian finch are originally from Australia where large flocks maybe found, mainly in arid grassland areas."),
#   Finch("Gouldian Finch", "https://i.imgur.com/kHAukWR.png",
#           "Gouldian Finches are Australia's most spectacularly coloured grassfinches, and are perhaps the most spectacularly coloured of all Australian birds."),
#   Finch("Strawberry Finch",
#           "https://i.imgur.com/4X9MswC.png", "Red Munias, Strawberry Finches or Red Avadavats (Amandava amandava) are a sparrow-sized bird of the Munia or Silverbill family."),
#   Finch("Owl Finch",
#           "https://i.imgur.com/yipEpSf.png", "Owl finches look like little owls with their distinctive markings. These are curious and social little birds."),
#   Finch("Pine Grosbeak",
#           "https://i.imgur.com/vzMexAT.png", "Locals in Newfoundland affectionately call Pine Grosbeaks 'mopes' because they can be so tame and slow moving."),
# ]


# class Finch:
#     def __init__(self, name, image, description):
#         self.name = name
#         self.image = image
#         self.description = description