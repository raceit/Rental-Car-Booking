from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from phonenumber_field.formfields import PhoneNumberField


class BookingForm(forms.Form):
    '''name = forms.CharField(label='Your name', max_length=100)
    sapno=forms.IntegerField(label='SAP No')
    sender = forms.EmailField()
    #date= forms.DateField(label='What is your birth date?', widget=forms.SelectDateWidget)
    #date=forms.DateField
    #date = DateField(widget=AdminDateWidget)
    #date=forms.DateField(widget = forms.SelectDateWidget())
    #end_date=forms.DateField(widget = forms.SelectDateWidget())
    date = forms.DateField(widget = forms.SelectDateWidget)
    #time = forms.TimeField(widget = forms.SelectTimeWidget)
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    #company = forms.ChoiceField(choices=["10,000", "entries", "here"])
    my_choice_field = forms.ChoiceField(choices=MY_CHOICES)'''
    sapno = forms.IntegerField(label='SAP Number')
    requestedBy = forms.CharField(label='Requested By')
    #mobileNumber = forms.IntegerField(label='Mobile Number')
    mobileNumber = PhoneNumberField()
    companyName = forms.CharField(label=' Company Name')
    costCentre = forms.CharField(label=' Cost Centre')
    debitTo = forms.CharField(label=' Debit To')
    departmnet = forms.CharField(label='Department')
    designation = forms.CharField(label='Designation')
    grade = forms.CharField(label='Grade')
    rentalcity = forms.CharField(label='Rental city')
    rentaltype = forms.ChoiceField(choices=[('fullday','Full Day'),('outstation','Outstation'),('pickanddrop','Pick and drop')])
    date = forms.DateField(widget = forms.SelectDateWidget)
    time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    carType = forms.ChoiceField(choices=[('1','1'),('2','2'),('3','3')])
    noOfCars = forms.IntegerField(label='No. Of Cars')
    repAddress = forms.CharField(widget=forms.Textarea)
    finalAddress = forms.CharField(widget=forms.Textarea)
    guestsapno = forms.IntegerField(label='SAP Number')
    guestType = forms.ChoiceField(choices=[('ceat','CEAT'),('dealer','Dealer'),('nonceat','NON CEAT')])
    guestname = forms.CharField(label='Guest Name')
    guestgrade = forms.CharField(label='Grade')
    guestmobileNumber = forms.IntegerField(label='Mobile Number')
    guestdesignation = forms.CharField(label='Designation')
    email = forms.EmailField()
    location = forms.CharField(label='Location')
    pickupPoint = forms.CharField(label='Pickup Point')
    dropPoint = forms.CharField(label='Drop Point')
    otherDetails = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)
    reason = forms.CharField(widget=forms.Textarea)


