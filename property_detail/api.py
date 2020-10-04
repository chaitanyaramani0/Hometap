
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .mock_api import url,headers
import requests


@api_view(['GET'])
def api_septic_check(request):
    query_param_zipcode = request.GET.get('zipcode')
    response = requests.get(url.format(query_param_zipcode),headers=headers)
    septic_response = response.json()
    if response.status_code == 200:
        has_septic = septic_response["property/details"]["result"]["property"]["sewer"]

        api_response = {
            'zipcode':query_param_zipcode,
            'sewer':has_septic
        }
    else:
        api_response = septic_response
    return Response(api_response)