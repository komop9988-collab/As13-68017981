from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # แก้บรรทัดนี้ให้เป็น views.form และตั้งชื่อเล่นว่า 'form'
    path('form/', views.form, name='form'), 
]