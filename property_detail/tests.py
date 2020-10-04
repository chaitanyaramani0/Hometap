from django.test import TestCase,Client
from django.urls import reverse,resolve
from property_detail.views import septic_check
import requests


# Create your tests here.
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('get_property_data')
        self.api = 'https://a64475c2-edfb-4dc2-bca8-eb7eac3b3843.mock.pstmn.io/api?zipcode={}'
        self.headers = {'x-api-key' : 'PMAK-5f78fababe2069003cf7f2bc-49986c4f557236cb8ef0180c4f7788ce64'}
        self.zipcode = '98423'

    def test_url_is_resolve(self):
        ''' Test Case is checking the url is 
        resolve the correct function.'''

        self.assertEquals(resolve(self.url).func, septic_check)

    def test_property_detail_template(self):
        ''' Check wheather function is rending the right template'''

        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')

    def test_api_key_authorization_without_key(self):
        ''' Api test without api key'''

        response_code = requests.get(self.api.format(self.zipcode))
        self.assertEquals(response_code.status_code,404)

    def test_api_key_authorization_with_key(self):
        ''' Api test with api key'''

        response_code = requests.get(self.api.format(self.zipcode),headers=self.headers)
        self.assertEquals(response_code.status_code,200)

    def test_api_response_data_with_zipcode_98243(self):
        ''' Api response data check with zipcode '''

        response = requests.get(self.api.format(self.zipcode),headers=self.headers).json()
        data = response["property/details"]["result"]["property"]["sewer"]
        self.assertEquals(data,'municipal')

    

      


