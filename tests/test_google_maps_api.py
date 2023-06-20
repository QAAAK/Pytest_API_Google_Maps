import json
import allure

from utils.api import Google_maps_api
from requests import Response
from utils.checking import Checking

@allure.epic('Test create new location')
class Test_create_location:
    """ get, put and delete new location"""

    @allure.description('test create, delete new location')
    def test_create_new_location(self):


        print('Method POST')
        result_post: Response = Google_maps_api.create_new_location()


        check = result_post.json()
        place_id = check.get('place_id')

        Checking.check_status_code(result_post, 200)
        Checking.check_json_response(result_post, ['status', 'place_id', 'scope', 'reference', 'id',])
        Checking.check_value(result_post, 'status', 'OK')


        print('Method GET POST')
        result_get: Response = Google_maps_api.get_new_location(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_response(result_get, ['location', 'accuracy', 'name',
                                                 'phone_number', 'address', 'types',
                                                 'website', 'language',])
        Checking.check_value(result_get, 'address', '29, side layout, cohen 09')

        print('Method PUT')
        result_put: Response = Google_maps_api.put_update_location(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_response(result_put, ['msg'])
        Checking.check_value(result_put, 'msg', 'Address successfully updated')

        print('Method GET PUT')
        result_get: Response = Google_maps_api.get_new_location(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_response(result_get, ['location', 'accuracy', 'name',
                                                  'phone_number', 'address', 'types',
                                                  'website', 'language', ])
        Checking.check_value(result_get, 'address', '100 Lenina street, RU')

        print('Method DELETE')
        result_delete: Response = Google_maps_api.delete_new_location(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_response(result_delete, ['status'])
        Checking.check_value(result_delete, 'status', 'OK')

        print('Method GET DELETE')
        result_get: Response = Google_maps_api.get_new_location(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_response(result_get, ['msg'])
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')








