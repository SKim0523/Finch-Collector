from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from .models import Finch, Comment
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse


# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"
    
#...
class About(TemplateView):
    template_name = "about.html"

class FinchList(TemplateView):
    template_name = "index.html"
     

class FinchList(TemplateView):
    template_name = "finch_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["finches"] = Finch.objects.all() # this is where we add the key into our context object for the view to use
        return context
    
class CommentCreate(View):
     def post(self,request, pk):
        content = request.POST.get('content')
        finch = Finch.objects.get(pk = pk) #req.params.id
        Comment.objects.create(content = content, finch = finch)
        return redirect('home')
    
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