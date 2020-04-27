from django.shortcuts import render
from django.views.generic import TemplateView
import datetime

# Create your views here.
class HomeView(TemplateView):
    # karena mewariskan dari TemplateView maka perlu ada template_name
    template_name = 'home.html'

    # method get untuk menampilkan halaman html
    def get(self, request):
        first_name = "John"
        today = datetime.datetime.today()
        return render(request, self.template_name, {'name':first_name, 'today':today})


class AboutView(TemplateView):
    template_name = 'about.html'
    
    def get(self, request):
        team = ['Wahyudi', 'Adit', 'Danu', 'Alex']
        return render(request, self.template_name, {'my_team':team})


# buat view untuk Contact
# tampilkan tanggal dalam bentuk Monday, April 27, 2020
class ContactView(TemplateView):
    template_name = 'contact.html'

    def get(self, request):
        today = datetime.datetime.today().strftime("%A, %B %2, %Y")
        return render(request, self.template_name,{'today':today})