# from django.views.generic import ListView,DetailView,render
from django.shortcuts import get_object_or_404, render
# Create your views here.
from . models import Muju,Muju_date111

# class MujuListView(ListView):
#     model = Muju
#     template_name = 'home.html'

# class MujuDetailView(ListView):
#     model = Muju_date111
#     template_name = 'Muju_detail.html'
def index(request):
    latest_muju_list = Muju.objects.order_by('muju_date')[:12]
    context = {'latest_muju_list': latest_muju_list}
    return render(request, 'home.html', context)

def detail(request, muju_id):
    muju = get_object_or_404(Muju, pk=muju_id)
    return render(request, 'Muju_detail.html', {'muju': muju})


# def detail1(request):
#     muju111 = Muju_date111.objects.order_by('muju_date1')[:12]
#     context = {'muju111': muju111}
#     return render(request, 'Muju_detail.html', context)