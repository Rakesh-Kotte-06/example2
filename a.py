from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.
from .views import AssetView,AssetFormView
from .models import rkotte_assets
from .validation import AssetValidation
from django.urls import reverse
from .forms import GetAssetsForm 
from django.test import Client
from django.utils import timezone
class RkotteAssetsTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('get_assets')
        rkotte_assets.objects.create(ip_address='192.168.1.1',hostname='example1.com',creation_date='2022-01-15',end_of_life = '2023-01-15',description='Sample Entry 1')
    
    def test_case(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        qs = rkotte_assets.objects.filter(ip_address = '192.168.1.1')
        self.assertEqual(qs.count(),1)
    
    def test_post_method_success(self):
        data = {
            'ip_address':'192.168.1.2',
            'hostname':'example2.com',
            'creation_date':'2021-09-20',
            'end_of_life':'2023-09-20',
            'description':'Sample Entry 2',
            
        }
        # if AssetValidation.ipAddressValidation(data['ip_address']):
        response = self.client.post(self.url,data,format ='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_post_method_fail(self):
        # url = 'http://127.0.0.1:8000/get_assets/'
        data = {
            
            'hostname':'example2.com',
            'creation_date':'2021-09-20',
            'end_of_life':'2023-09-20',
            'description':'Sample Entry 2'
        }
        response = self.client.post(self.url,data,format ='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        
    def test_validation_false(self):
        valid_ip = '192.168.1.499'
        result = AssetValidation.ipAddressValidation(valid_ip)
        print(result)
        self.assertFalse(result)
    def test_validation_true(self):
        valid_ip = '192.168.1.2'
        result = AssetValidation.ipAddressValidation(valid_ip)
        print(result)
        self.assertTrue(result)
# class AssetFormViewTestCase(TestCase):
#     def setUp(self):
#         self.asset1 = rkotte_assets.objects.create(
#             hostname="TestHost1",
#             ip_address="127.0.0.1",
#             creation_date=timezone.now(),
#             end_of_life=timezone.now(),
#             description="Test Description 1"
#         )
#         self.asset2 = rkotte_assets.objects.create(
#             hostname="TestHost2",
#             ip_address="192.168.0.1",
#             creation_date=timezone.now(),
#             end_of_life=timezone.now(),
#             description="Test Description 2"
#         )

#     def test_assets_get_all(self):
#         # Testing the functionality when no parameters are provided in the request
#         response = self.client.get(reverse('get_all_assets'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         queryset1 = rkotte_assets.objects.all().values()
#         self.assertEqual(queryset1.count(),2)

#     def test_assets_get_all_with_start_end_dates(self):
#         # Testing the functionality when start date and end date are provided in the request
#         start_date = self.asset1.creation_date.strftime('%Y-%m-%d')
#         end_date = self.asset2.end_of_life.strftime('%Y-%m-%d')
#         response = self.client.get(reverse('get_all_assets'), {'start_date': start_date, 'end_date': end_date})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_get_all_with_search(self):
#         # Testing the functionality when search parameter is provided in the request
#         search_text = "TestHost1"
#         response = self.client.get(reverse('get_all_assets'), {'search': search_text})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         query = rkotte_assets.objects.filter(hostname__icontains = search_text).values()
#         self.assertTrue(query)

#     def test_asset_post_request_redirect(self):
#         # Testing the functionality when the code redirected with the start and end date
#         response = self.client.post(reverse('get_all_assets'), {'start_date': '2023-01-01', 'end_date': '2023-12-31', 'search': 'TestHost1'})
#         self.assertEqual(response.status_code,status.HTTP_302_FOUND)
#         self.assertRedirects(response, reverse('get_all_assets') + '?start_date=2023-01-01&end_date=2023-12-31&search=TestHost1')

#     # POST method test cases
#     def test_asset_post_with_valid_data(self):
#         # Testing assets post method with valid data
#         form_data = {
#             'ip_address': '192.168.1.1',  # Valid IP address
#             'hostname':'TestHost1',
#             'creation_date':'2021-09-20',
#             'end_of_life':'2023-09-20',
#             'description':'Sample Entry 1'
#         }
#         response = self.client.post(reverse('insert_assets'), form_data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertTrue(rkotte_assets.objects.filter(ip_address='192.168.1.1').exists())
#         # print(rkotte_assets.objects.filter(ip_address='192.168.1.1').values())

# #     def test_asset_post_with_invalid_ip_address(self):
# #         # Testing the asset post method with invalid ip address
# #         form_data = {
# #             'ip_address': 'invalid_ip',
# #             'hostname':"TestHost2",
# #             'creation_date':'2021-09-20',
# #             'end_of_life':'2023-09-20',
# #             'description':'Sample Entry 2'
# #         }
# #         error_message = AssetValidation.asset_validation(form_data['ip_address'])
# #         response = self.client.post(reverse('insert_assets'), form_data)
# #         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Assuming you render an error page
# #         print(error_message)
# #         # Add assertions to check if the 'error_message' is present in the response context
# #         self.assertContains(response, 'Invalid IP Address')
        




#     # def test_get_request(self):
#     #     # Test a GET request to the view
#     #     response = self.client.get(reverse('insert_assets'))
#     #     self.assertEqual(response.status_code, 200)  # Expect a successful GET request
