from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Complaint
from django.contrib import messages
from django.utils.text import slugify
from .forms import ComplaintForm
from scripts.zemberek import run

def complaint_index(request):
    if not request.user.is_authenticated:
        return Http404

    complaints = Complaint.objects.filter(user=request.user)
    context = {'complaints':complaints}
    return render(request, 'complaint/index.html', context)

def complaint_create(request):
    if not request.user.is_authenticated:
        return Http404()
   
    form = ComplaintForm(request.POST or None)
    if form.is_valid():
        complaint=form.save(commit=False)
        complaint.user = request.user
        complaint.save()
        comp=complaint.text
        tit=complaint.title  
        run(comp,tit)
        return HttpResponseRedirect(complaint.get_absolute_url())
    context = {
        'form':form,
    }
    
    return render(request, 'complaint/form.html', context)

    
def complaint_delete(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    complaint = get_object_or_404(Complaint, slug=slug)
    complaint.delete()
    return redirect('complaint:index')    


def complaint_detail(request, slug):
    complaint = get_object_or_404(Complaint, slug=slug)
    context={
        'complaint':complaint,
    }
    return render(request, 'complaint/detail.html', context)