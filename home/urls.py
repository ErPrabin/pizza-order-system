from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index,name='index'),
    path('checkout/<id>', views.checkout,name='checkout'),
    path('order', views.order,name='order'),
    path('success/<id>', views.success,name='success'),
    # path('my-book', views.myBook,name='mybook'),
    # path('add-book', views.addBook,name='addbook'),
    # path('my-book-list', views.myBookList,name='addbooklist'),
    # path('release/<id>', views.releaseBook,name='release'),
]