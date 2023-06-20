import requests
import allure

from utils.log import Log

""" List HTTP methods"""

@allure.epic('HTTP-methods')
class Http_method:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step('GET request'):
            Log.add_requests(url, method='GET')
            result = requests.get(url, headers=Http_method.headers, cookies=Http_method.cookie)
            Log.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step('POST requests'):
            Log.add_requests(url, method='POST')
            result = requests.post(url, headers=Http_method.headers,
                                        json=body, cookies=Http_method.cookie)
            Log.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step('PUT requests'):
            Log.add_requests(url, method='PUT')
            result = requests.put(url, headers=Http_method.headers,json=body,
                                       cookies=Http_method.cookie)
            Log.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step('DELETE requests'):
            Log.add_requests(url, method='DELETE')
            result = requests.delete(url, headers=Http_method.headers, json=body,
                                          cookies=Http_method.cookie)
            Log.add_response(result)
            return result
