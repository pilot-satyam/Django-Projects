from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator
# Create your views here.
def MovieList(request):
   movie_objects = Movies.objects.all()
   movie_name = request.GET.get('movie_name') #here movie_name in paranthesis isthe form input name in template
   if movie_name !='' and movie_name is not None:
     # movie_objects = movie_objects.filter(name = movie_name) #here name is from the model we have inheritate
     movie_objects = movie_objects.filter(name__icontains = movie_name)
   

   paginator = Paginator(movie_objects,3) #creating the instance of Paginator,this will have 3 movies in one page and rest in next
   page = request.GET.get('page') #give access to the page number
   movie_objects = paginator.get_page(page) #fetch object on current page and not all the objects
   return render(request,'newApp/movie_list.html',{'movie_objects':movie_objects})