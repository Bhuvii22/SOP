from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import UserProfileForm

def login(request):
    return render(request,'login.html')

def registration_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # The form is valid, save the data to the database
            form.save()
            
            # Redirect to the 'Next.html' page after successful form submission
            return redirect('nextpage')  # Replace 'next_page_name' with the actual URL name for 'Next.html'
    else:
        form = UserProfileForm()

    return render(request, 'register.html', {'form': form})

def nextpage(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # The form is valid, save the data to the database
            form.save()
            
            # Redirect to the 'Next.html' page after successful form submission
            return redirect('submit')  # Replace 'next_page_name' with the actual URL name for 'Next.html'
    else:
        form = UserProfileForm()

    return render(request, 'Next.html', {'form': form})

def submit(request):
    if request.method == 'POST':
        form=UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form=UserProfileForm()
    return render(request,'regform.html',{'form':form})
def success(request):
    return render(request,'success.html')






def favicon_view(request):
    # Handle favicon requests here
    # You can return an empty response or your custom favicon image
    return HttpResponse(status=204)
