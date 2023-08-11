from .views import *
from django.urls import path

urlpatterns=[
    #path('',home,name='home')
    path('',CrudView.as_view(),name='home'),
    path('create/',Create.as_view(),name='create'),
    path('<int:pk>/update',Update.as_view(),name='update'),
    path('<int:pk>/delete/',Delete.as_view(),name='delete'),
    path('login/',login_page,name='login'),
    path('logout/', logout_view,name='logout')
]