from django.shortcuts import render,redirect
from django.contrib import messages
import requests

# Create your views here.


def get_address(request):
    
    url = 'https://a64475c2-edfb-4dc2-bca8-eb7eac3b3843.mock.pstmn.io/api?zipcode={}'
    if request.method == 'POST':
        address = request.POST['address']
        zipcode = request.POST['zipcode']

        if address != '' and zipcode != '':
            septic_response = requests.get(url.format(zipcode)).json()
            print(septic_response)
            print(url.format(zipcode))
            has_septic = septic_response["property/details"]["result"]["property"]["sewer"]
           
            if has_septic == 'Septic':
                messages.success(request, 'Your Property has Septic system')
                return redirect('get_property_data')
            else:
                sewer_type = 'your property has {} system'.format(has_septic)
                messages.error(request, sewer_type)
                return redirect('get_property_data')
        else:
            messages.error(request, 'We required your address and zipcode to check the septic system presence.')
        
    return render(request,'index.html')