from django.urls import path
from . import views
app_name='app1'
urlpatterns=[
    path('hello',views.hello,name='hello'),
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('showusers/',views.showusers,name='showusers'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('changepassword/<int:id>',views.changepassword,name='changepassword'),
    path('image/',views.image,name='image'),
    path('gallery/',views.gallery,name='gallery'),
    path('logout/',views.logout,name='logout'),
    path('showdetails/',views.showdetails,name='showdetails'),
]