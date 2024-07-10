from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    order_field = request.GET.get('sort', 'id')
    if order_field == 'name':
        phones = Phone.objects.order_by('name').all()
    elif order_field == 'min_price':
        phones = Phone.objects.order_by('price').all()
    elif order_field == 'max_price':
        phones = Phone.objects.order_by('-price').all()
    elif order_field == 'id':
        phones = Phone.objects.order_by('id').all()

    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones_obj = Phone.objects.filter(slug=slug)
    phone = phones_obj[0]
    context = {'phone': phone}
    return render(request, template, context)


