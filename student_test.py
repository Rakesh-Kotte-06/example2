# from django.test import TestCase
# from django.urls import reverse
# from .models import rkotte_assets
# from myapp.forms import GetAssetsForm

# class AssetFormViewTest(TestCase):
#     def test_get_request_no_parameters(self):
#         url = reverse('get_all_assets')  # Replace 'get_all' with the actual URL name
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)  # Check that the view responds with a 200 status code
#         self.assertTemplateUsed(response, 'get_all_assets.html')  # Check the template used
#         self.assertIn('form', response.context)

#         # self.assertIsInstance(response.context['form'], GetAssetsForm)  # Check that the form is in the context

        
#     def test_get_request_with_parameters(self):
#         url = reverse('get_all_assets')  # Replace 'get_all' with the actual URL name
#         response = self.client.get(url, {'start_date': '2023-01-01', 'end_date': '2023-12-31'})
#         self.assertEqual(response.status_code, 200)  # Check that the view responds with a 200 status code

#     def test_post_request(self):
#         url = reverse('get_all_assets')  # Replace 'get_all' with the actual URL name
#         data = {'start_date': '2023-01-01', 'end_date': '2023-12-31', 'search': 'example'}
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, 302)  # Check that the view redirects (HTTP 302 status code)
#         self.assertIn('start_date=2023-01-01', response.url)  # Check the redirected URL for query parameters

#     def test_post_request_empty_data(self):
#         url = reverse('get_all_assets')  # Replace 'get_all' with the actual URL name
#         data = {'start_date': '', 'end_date': '','search': ''}
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, 400)  # Check that the view responds with a 200 status code



# # from django.test import TestCase
# # from rest_framework.test import APITestCase
# # from rest_framework import status
# # Create your tests here.
# # from .views import AssetView,AssetFormView
# # from .models import rkotte_assets
# # from .validation import AssetValidation
# # from django.urls import reverse
# # from .forms import GetAssetsForm 
# def test_get_request_without_query_parameters(self):
#     url = reverse('get_all_assets')
#     response = self.client.get(url)
#     self.assertEqual(response.status_code, 200)  # Check that the view responds with a 200 status code
#     self.assertTemplateUsed(response, 'get_all_assets.html')  # Check the template used
#     self.assertIsInstance(response.context['form'], GetAssetsForm)  # Check that the form is in the context



# # class RkotteAssetsTestCase(APITestCase):
# #     def setUp(self):
# #         self.url = reverse('get_assets')
# #         rkotte_assets.objects.create(ip_address='192.168.1.1',hostname='example1.com',creation_date='2022-01-15',end_of_life = '2023-01-15',description='Sample Entry 1')
    
# #     def test_case(self):
# #         # url = 'http://127.0.0.1:8000/get_assets/'
# #         response = self.client.get(self.url)
# #         qs1 = rkotte_assets.objects.all()
# #         print(qs1.values())
# #         self.assertEqual(response.status_code,status.HTTP_200_OK)
# #         qs = rkotte_assets.objects.filter(ip_address = '192.168.1.1')
# #         self.assertEqual(qs.count(),1)
    
# #     def test_post_method_success(self):
# #         # url = 'http://127.0.0.1:8000/get_assets/'
# #         data = {
# #             'ip_address':'192.168.1.2',
# #             'hostname':'example2.com',
# #             'creation_date':'2021-09-20',
# #             'end_of_life':'2023-09-20',
# #             'description':'Sample Entry 2'
# #         }
# #         response = self.client.post(self.url,data,format ='json')
# #         self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
# #     def test_post_method_fail(self):
# #         # url = 'http://127.0.0.1:8000/get_assets/'
# #         data = {
            
# #             'hostname':'example2.com',
# #             'creation_date':'2021-09-20',
# #             'end_of_life':'2023-09-20',
# #             'description':'Sample Entry 2'
# #         }
# #         response = self.client.post(self.url,data,format ='json')
# #         self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        
# #     def test_validation_false(self):
# #         valid_ip = '192.168.1.499'
# #         result = AssetValidation.ipAddressValidation(valid_ip)
# #         self.assertFalse(result)
# #     def test_validation_true(self):
# #         valid_ip = '192.168.1.2'
# #         result = AssetValidation.ipAddressValidation(valid_ip)
# #         self.assertTrue(result)
    
# # class AssetFormViewTestCases(TestCase):
# #     def setUp(self):
# #         rkotte_assets.objects.create(ip_address='192.168.1.1',hostname='example1.com',creation_date='2022-01-15',end_of_life = '2023-01-15',description='Sample Entry 1')
# #     def get_all_testCases(self):
# #         url = 'http://127.0.0.1:8000/get_assets/'
# #         response = self.client.get(url)
# #         qs1 = rkotte_assets.objects.all()
# #         # print(qs1.values())
# #         self.assertEqual(response.status_code,status.HTTP_200_OK)
# #         qs = rkotte_assets.objects.filter(ip_address = '192.168.1.1')
# #         self.assertEqual(qs.count(),1)
# #     # def tearDown(self):
numbers = [1980,1,0,1]
if all(0 <= i <= 255 for i in numbers):
    print(True)
else:
    print(False)