from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import components_provided
from components.models import component
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
import datetime
from .forms import ProviderFrom
from django.core.mail import EmailMessage
from easy_pdf.views import PDFTemplateResponseMixin

class PDF_provided(PDFTemplateResponseMixin,ListView):
    model = components_provided
    context_object_name = 'components'
    template_name = 'controller/pdf_file.html'

class PDF_returned(PDFTemplateResponseMixin,ListView):
    model = components_provided
    context_object_name = 'components'
    template_name = 'controller/returned_file.html'

@login_required
def main(request):
    return render(request,'controller/base.html')

def provided(request):
    b=components_provided.objects.filter(status=False)
    date=datetime.date.today()
    return render(request,'controller/provided.html',{'b':b,'date':date})

def returned(request):
    a=components_provided.objects.filter(status=True)
    return render(request,'controller/returned.html',{'a':a})

def List_component(request):
    a=component.objects.all()
    return render(request,'controller/component_list.html',{'a':a})



def CreateProvide(request):
    if request.method=='GET':
        form=ProviderFrom()
    else:
        form=ProviderFrom(request.POST)
        if form.is_valid():
            form.save()
            com =form.cleaned_data.get('detail')
            quan = form.cleaned_data.get('quantity')
            a = component.objects.get(name=com.name)
            a.available_quantity=a.available_quantity - quan
            a.save()
            return redirect('List_provided')
    return render(request,'controller/create_provide.html',{'form':form})

def DeleteProvide(request,pk):
    a = components_provided.objects.get(id=pk)
    a.deleted_at=datetime.datetime.now()
    a.status="True"
    b = component.objects.get(name=a.detail.name)
    b.available_quantity=b.available_quantity + a.quantity
    a.save()
    b.save()
    return redirect('List_provided')


class CreateComponent(CreateView):
    model =component
    template_name = 'controller/create_component.html'
    fields = '__all__'
    success_url = reverse_lazy('List_component')

class UpdateComponent(UpdateView):
    model = component
    template_name = 'controller/update_component.html'
    fields = '__all__'
    success_url = reverse_lazy('List_component')

def DeleteComponent(request,pk):
    a = component.objects.get(id=pk)
    a.status = "True"
    a.save()
    return redirect('List_component')

def reminder(request,pk):
    a=components_provided.objects.get(id=pk)
    address=a.email_id
    email=EmailMessage('PROJECT LAB ECE','Kindly,return the components to the lab as soon as possible.',to=[address])
    email.send()
    return redirect('List_component')
