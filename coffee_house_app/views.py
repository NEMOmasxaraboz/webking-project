from django.shortcuts import render, redirect

from django.views.generic import ListView

from .models import Complaints, Coffees, Cakes


def index(request):

    return render(request, 'base.html')


def menu_view(request):
    coffees = Coffees.objects.all()
    cakes = Cakes.objects.all()
    return render(request, 'menu.html', {'coffees': coffees, 'cakes': cakes})


def shikoyatlar_create(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        if description:
            Complaints.objects.create(description=description)
            return redirect('complaints')
    return render(request, 'complaints.html')


class ComplaintListView(ListView):
    model = Complaints
    template_name = 'complaints_list.html'
    context_object_name = 'Complaints'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Complaints.objects.all()



def about(request):
    return render(request, 'about.html')




