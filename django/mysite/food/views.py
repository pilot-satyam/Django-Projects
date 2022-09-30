from re import template
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ItemForm
from .models import Item
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
#incoming is a request for server and http response is response which the view will show
def index(request):
    #return HttpResponse('Satyam Srivastava Captain of Boeing737 very soon') 
    item_list = Item.objects.all() #data extracted from database and is a context means anything which we obtain from db
    template = loader.get_template('food/index.html')
    context = {
     'item_list' : item_list,
    }
     # return HttpResponse(item_list)
    return HttpResponse(template.render(context,request))  #---> To render the template

class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'
    
def item(request):
    return HttpResponse('<h1>This is an item view</h1>')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id) #getting the id's from only database
    context ={
    'item' : item,
    }
    # return HttpResponse("This is item no %s" % item_id)
    return render(request,'food/detail.html',context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item' #if you don't want to write context then in the template file replace item with 'object' it will work

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form})

class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image'] #we are not including the username field,as it needs to get updated automatically
    template_name = 'food/item-form.html'
     # to accept a form
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None,instance=item)  # writing instance so that previous data is also passed for the edit
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item=Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item' : item})

