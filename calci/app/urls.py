from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.signlogin),
    path('',views.index),
    path('',views.s17s),
    path('',views.s18s),
    path('',views.cgpa),
    path('',views.s17s1),
    path('',views.s17s2),
    path('',views.s17s3),
    path('',views.s17s4),
    path('',views.s17s5),
    path('',views.s17s6),
    path('',views.s17s7),
    path('',views.s17s8),
    path('sgpa/',views.sgpa,name='sgpa'),

]
