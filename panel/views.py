from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewMsgeForm
from .models import Msge
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from django.views import generic
from django.views.generic.edit import FormMixin
from django.urls import reverse

# Create your views here.
class MsgeView(FormMixin, generic.ListView):
    model = Msge
    form_class = NewMsgeForm

    def get_context_data(self, **kwargs):
        context = super(MsgeView, self).get_context_data(**kwargs)
        context['form'] = NewMsgeForm()
        return context
    
    def get_queryset(self):
       return Msge.objects.order_by('?')

    def get_success_url(self):
        return reverse('index')

    def post(self, request):
        form = NewMsgeForm(request.POST)
        if form.is_valid():
            msge_ = form.save(commit=False)
            msge_.timestamp = timezone.now()
            msge_.status = 'pendiente'
            msge_.save()
            return super(MsgeView, self).form_valid(form)



def index(request):
    if request.method == "POST":
        form = NewMsgeForm(request.POST)
        if form.is_valid():
            msge_ = form.save(commit=False)
            msge_.timestamp = timezone.now()
            msge_.status = 'pendiente'
            msge_.save()
            return redirect('index')
    else:
        form = NewMsgeForm()
        
    return render(request, 'panel/panel.html')
