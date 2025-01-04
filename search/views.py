from django.shortcuts import render
from .models import Item  # Model yang akan dicari

def search(request):
    q = request.GET.get('q', '')  # Default ke string kosong jika 'q' tidak ada
    results = []

    if q:  # Jika parameter 'q' memiliki nilai
        results = Product.objects.filter(name__icontains=q)  # Cari produk berdasarkan nama
    return render(request, 'search/search_results.html', {
        'query': q,
        'results': results,
    })