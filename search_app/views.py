from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
# Create your views here.
def SearchForm(request):
    products=None
    query=request.GET.get('q')
    if query:
        products=Product.objects.filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request,'search.html',{'query':query,'products':products})

def SearchResult(request):
    query = request.GET.get('q', '')
    search_results = Product.objects.filter(name__icontains=query)
    context = {
        'query': query,
        'search_results': search_results,
    }

    return render(request, 'search.html', context)