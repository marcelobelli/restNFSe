import json

from django.shortcuts import resolve_url as r

from rest_framework import status
from rest_framework.test import APITestCase
from model_mommy import mommy

from ..models import RPS


class RestBaseTest(APITestCase):

    def setUp(self):
        self.url = r('rps:index')
        self.user = mommy.make('accounts.User', is_active=True)
        self.user_password = '123456'
        self.user.set_password(self.user_password)
        self.user.save()


class RestRPSAuthenticationTest(RestBaseTest):

    def test_authentication_error(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authentication_success(self):
        self.client.login(username=self.user.email, password=self.user_password)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RestRPSPostTest(RestBaseTest):

    def setUp(self):
        super(RestRPSPostTest, self).setUp()
        self.client.login(username=self.user.email, password=self.user_password)

    def test_post_success_status_code(self):
        data = json_to_dict('rps.json')
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_success_content(self):
        data = json_to_dict('rps.json')
        response = self.client.post(self.url, data, format='json')
        data_expected = json_to_dict('rps_response.json')

        self.assertEqual(response.data, data_expected)

    def test_post_missing_field(self):
        data = json_to_dict('rps_with_error.json')
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RestRPSDetailTest(RestBaseTest):

    def setUp(self):
        super(RestRPSDetailTest, self).setUp()
        self.url = r('rps:detail', 1)
        self.client.login(username=self.user.email, password=self.user_password)

        data = json_to_dict('rps.json')
        url_post = r('rps:index')
        self.client.post(url_post, data, format='json')

    def test_rps_detail_response(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_rps_detail_content(self):
        response = self.client.get(self.url)
        data_expected = json_to_dict('rps_response.json')

        self.assertEqual(response.data, data_expected)

    def test_rps_put_response(self):
        data = json_to_dict('rps_put.json')
        response = self.client.put(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_rps_put_content(self):
        data = json_to_dict('rps_put.json')
        response = self.client.put(self.url, data, format='json')
        data_expected = json_to_dict('rps_put_response.json')

        self.assertEqual(response.data, data_expected)

    def test_rps_delete_response(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


def json_to_dict(json_file):
    with open('restNFSe/rps/tests/json_examples/{}'.format(json_file)) as j:
        dict_expected = json.load(j)

    return dict_expected
