from django.shortcuts import render,HttpResponse,redirect
from .forms import BookingForm
from django.http import HttpResponseRedirect
from .models import Booking
from django.contrib import messages

# Create your views here.
def carbooking(request):
    form = BookingForm()
    return render(request, 'car/form.html',{'form': form})


def car_booking_submission(request):
    print("Hello form is submitted")
    sapno = request.POST["sapno"]
    your_name = request.POST["your_name"]
    #mobileNumber = request.POST["mobileNumber"]
    guestsapno=request.POST["guestsapno"]
    email=request.POST["email"]
    time=request.POST["time"]
    #mobilenumber=request.POST["mobilenumber"]
    booking = Booking(sapno=sapno, your_name=your_name,guestsapno=guestsapno,email=email,time=time)
    booking.save()
    messages.success(request, 'Form submission successful')
    return render(request, 'car/form.html')




'''def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BookingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            requestedBy = form.save(commit=False)
            requestedBy.user = request.user
            requestedBy.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('form:form')
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookingForm()

    return render(request, 'car/form.html', {'form': form})'''


