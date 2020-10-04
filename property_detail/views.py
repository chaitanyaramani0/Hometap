from django.contrib import messages
from django.shortcuts import render,redirect
from .mock_api import url,headers
import requests

# Create your views here.



def septic_check(request):
    """
    Fuction checks the whether a property has septic system or not based on zipcode.
    it uses the Postman mock server api which is provate server and required the api-key 

    here api key is visible to every one which is not a recommend. api key should be in envornment variable 
    but since it is just a mock server and uses the same api key for everyone.api key is just to demostrat how 
    we can use the authentiacion third party api.

    Mock server is replica of Homecenery api it takes address and zipcode as api param. here in this mock api it
    only takes zipcode. 

    """
    
    if request.method == 'POST':
        address = request.POST['address']
        zipcode = request.POST['zipcode']

        if address != '' and zipcode != '':
            if zipcode.isdigit():
                response = requests.get(url.format(zipcode),headers=headers)
                response_code = response.status_code

                if response_code == 200:
                    septic_response = response.json()
                    has_septic = septic_response["property/details"]["result"]["property"]["sewer"]
                
                    if has_septic == 'Septic':
                        messages.success(request, 'Your Property has Septic system')
                        return redirect('get_property_data')
                    else:
                        sewer_type = 'your property has {} system'.format(has_septic)
                        messages.error(request, sewer_type)
                        return redirect('get_property_data')
                elif response_code == 500:
                    messages.error(request, 'Authentication failed please check your api key.')
            else:
                messages.error(request, 'Please enter valid zipcode For eg 98243,11223...')
        else:
            messages.error(request, 'We required your address and zipcode to check the septic system presence.')
        
    return render(request,'index.html')




