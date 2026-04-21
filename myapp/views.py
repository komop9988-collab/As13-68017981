from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Person

def index(request):
    # 1. รับค่าจากช่องค้นหา (name="q" จากไฟล์ index.html)
    search_query = request.GET.get('q')
    
    if search_query:
        # 2. ถ้ามีการค้นหา ให้กรองข้อมูลจากชื่อ (name)
        all_Person = Person.objects.filter(name__icontains=search_query)
    else:
        # 3. ถ้าไม่มีการค้นหา ให้ดึงข้อมูลทั้งหมดมาแสดงปกติ
        all_Person = Person.objects.all()
        
    return render(request, "index.html", {"all_person": all_Person})

def about(request):
    return render(request,"about.html")


from django.shortcuts import render, redirect 
from django.http import HttpResponse
from myapp.models import Person


# 2. แก้ไขฟังก์ชัน form ให้รับข้อมูล POST
def form(request):
    if request.method == "POST":
        # ดึงค่าจากช่อง Input ใน HTML
        name = request.POST.get('fname')
        age = request.POST.get('fage')
        
        # สั่งบันทึกลงฐานข้อมูล
        Person.objects.create(name=name, age=age)
        
        # บันทึกเสร็จแล้วให้เด้งกลับไปหน้าแรก
        return redirect('index')
    
    return render(request, "form.html")