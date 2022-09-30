from . import views #to import from current directory in order to connect view with urls
from django.urls import path

app_name = 'food' #so that django knows which project refer to when there are multiple projects present

urlpatterns = [
    #/food/
    path('',views.IndexClassView.as_view(),name='index'), #updated with class based view
    #path('',views.index,name='index'),
    #/food/1
    # path('<int:item_id>/',views.detail,name='detail'), ---> earlier fn
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    path('item/',views.item,name='item'),
    #add items
    # path('add',views.create_item,name='create_item'),
    #class based adding view
    path('add',views.CreateItem.as_view(),name='create_item'),
    #update 
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete
    path('delete/<int:id>/',views.delete_item,name='delete_item'), 
]
