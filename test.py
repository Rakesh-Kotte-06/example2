import unittest

class TestCaseDemo1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass method executed...')
    def setUp(self):
        print('Executed setUp method')
    def test_method1(self):                 #setUp --> test_method1 --> tearDown
        print('Test method 1 executed')
    def test_method2(self):                 #setUp --> test_method2 --> tearDown
        print('Test metod 2 executed')
    def tearDown(self):
        print('Executed tearDown method')
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass method executed...')

unittest.main()


# class AssetFormViewTest(TestCase):

#     def test_get_method(self):
#         client = Client()
#         url = reverse('get_all_assets')
#         response = client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'get_all_assets.html')
#         self.assertIn('form', response.context)
#         # self.assertIsInstance(response.context['form'], GetAssetsForm)

#     def test_post_method_success(self):
#         client = Client()
#         url = reverse('insert_assets')
#         post_data = {
#             'ip_address': '192.168.1.2',
#             'hostname': 'example2.com',
#             'creation_date': '2021-09-20',
#             'end_of_life': '2023-09-20',
#             'description': 'Sample Entry 2'
#         }
#         response = client.post(url, post_data)
#         self.assertEqual(response.status_code,status.HTTP_200_OK)
#         qs1 = rkotte_assets.objects.all()
#         self.assertEqual(qs1.count(),1)

#     def test_post_method_failure(self):
#         client = Client()
#         url = reverse('insert_assets')
#         post_data = {
#             'hostname': 'example2.com',
#             'creation_date': '2021-09-20',
#             'end_of_life': '2023-09-20',
#             'description': 'Sample Entry 2'
#         }
#         response = client.post(url, post_data)
#         qs1 = rkotte_assets.objects.all()
#         self.assertEqual(qs1.count(),1)

