from django.shortcuts import render
from .models import Person, District, Division, Upazila
from .forms import PersonForm

# Create your views here.
def load_district(request):
    division_id = request.GET.get('division')
    district = District.objects.filter(division_id=division_id).order_by('name')

    district_id = request.GET.get('district')
    upazila = Upazila.objects.filter(district_id=district_id).order_by('name')
    context = {
        'district': district,
        'upazila': upazila
    }
    return render(request, 'district_dropdown_list_options.html', context)
def Index(request):
    form = PersonForm

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
         'form': form
     }
    return render(request, 'index.html', context)