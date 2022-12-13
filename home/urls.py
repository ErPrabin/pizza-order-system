from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index,name='index'),
    path('checkout/<id>', views.checkout,name='checkout'),
    # path('my-book', views.myBook,name='mybook'),
    # path('add-book', views.addBook,name='addbook'),
    # path('my-book-list', views.myBookList,name='addbooklist'),
    # path('release/<id>', views.releaseBook,name='release'),
]