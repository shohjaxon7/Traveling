


from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from sqlparse.sql import Comment

from blog.forms import PostForms
from blog.models import *

#
# # Create your views here.

def a404(request):
    return render(request,"404.html",context={})

def about(request):
    return render(request,"about.html",context={})

def booking(request):
    return render(request,"booking.html",context={})

def contact(request):
    return render(request,"contact.html",context={})

def destination(request):
    return render(request,"destination.html",context={})

def index(request):
    contact = PostForms(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2> MALUMOTLAR MUVOFIQIYATLI YUBORILDI QONG'IROQNI KUTING !!! <h2/>")
    about = About.objects.all()
    service = Service.objects.all()
    lenov = Lenov.objects.all()
    shadow = Shadow.objects.all()
    context = {
        'about':about,
        'service':service,
        'lenov':lenov,
        'shadow':shadow

    }

    return render(request,"index.html",context=context)

def package(request):
    return render(request,"package.html",context={})

def service(request):
    return render(request,"service.html",context={})

def team(request):
    return render(request,"team.html",context={})

def testimonial(request):
    return render(request,"testimonial.html",context={})

def aboutdetailview(request,id):
    try:
        about=About.objects.get(id=id)
        context ={
            "about":about
        }
    except about.DoesNotExidst:
        raise Http404("No about found")
    return render(request,"about_detail.html",context=context)

def lenovdetailview(request,id):
    try:
        lenov=Lenov.objects.get(id=id)
        context ={
            "lenov":lenov
        }
    except lenov.DoesNotExidst:
        raise Http404("No lenov found")
    return render(request,"lenov_detail.html",context=context)


def shadowdetailview(request,id):
    try:
        shadow=Shadow.objects.get(id=id)
        context ={
            "shadow":shadow
        }
    except shadow.DoesNotExidst:
        raise Http404("No shadow found")
    return render(request,"shadow_detail.html",context=context)



def shadow_detail(request, pk):
    shadow = get_object_or_404(Shadow, pk=pk)
    comments = shadow.comment.all()
    return render(request,'comments_detail_page/shadow_detail.html',{'shadow':shadow, 'comments':comments})


@login_required
def add_comment(request, shadow_id):
    shadow = get_object_or_404(Shadow, id=shadow_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        if not text:
            return HttpResponseForbidden("Izoh bo'sh bolishi mumkin emas!")

        # Izohni yaratish
        Comment.objects.create(
            shadow=shadow,
            user=request.user,
            text=text
        )
        return redirect('shadow_detail', pk=shadow.id) # Izoh qo'ilgandan keyin shadow_detail sahifasiga qaytish

    return HttpResponseForbidden("Boshqa metodda ruhsat berilgan.")




# ruhsatdef index(request,id):
#     form = PostForm(request.POST or None)
#     if request.method == "POST" and form.is.valid():
#         form.save()
#         raise HttpResponse("<h2> MA'LUMOTLAR MUVOFAQIYATLI YUBORILDI !!! <h2/> ")
#
#    about = About.objects.all()







# def search_view(request):
#     query = request.GET.get('q', '')  # URL'dan qidiruv so'zini olamiz
#     about = About.objects.filter(name__icontains=query)
#
#     context = {
#         'query': query,
#         'about': about,
#         'contact': contact
#
#     }
#     return render(request, 'search/search_result.html', context)




def search_view(request):
    query = request.GET.get('q', '')  # URL'dan qidiruv so'zini olamiz
    about = About.objects.filter(name__icontains=query)

    context = {
        'query': query,
        'about': about,
    }
    return render(request, 'search/search_result.html', context)




def add_comment(request, abo_id):
    about = get_object_or_404(About, id=abo_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        if not text:
            return HttpResponseForbidden("Izoh bo'sh bo'lishi mumkin emas!")

        # Izohni yaratish
        Comment.objects.create(
            about=about,
            user=request.user,
            text=text
        )
        return redirect('about  _detail', id=about.id)

    return HttpResponseForbidden("Boshqa methodda ruxsad berilmagan.")







def about_detail(request, pk):
    about = get_object_or_404(About, pk=pk)  # Berilgan ID bo'yicha ob'ektni olish
    return render(request, 'myapp/about_detail.html', {'about': about})





















































































































