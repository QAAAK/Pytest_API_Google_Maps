from utils.http_method import Http_method


class Google_maps_api:
    """ method test Google Maps API"""

    base_url = 'https://rahulshettyacademy.com'   # base url
    key = '?key=qaclick123'
    json_for_create_new_location = {
        "location": {
            "lat": -38.383494,
            "lng": 33.427362
        }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
        "types": [
            "shoe park",
            "shop",
        ],
            "website": "http://google.com",
            "language": "French-IN"

    }


    @staticmethod
    def create_new_location():

        post_resource = "/maps/api/place/add/json"  # Resource post method
        post_url = Google_maps_api.base_url + post_resource + Google_maps_api.key   # Post requests url
        result_post = Http_method.post(post_url, Google_maps_api.json_for_create_new_location)
        print(post_url)

        print(result_post.text)
        return result_post

    @staticmethod
    def get_new_location(place_id):
        get_resource = "/maps/api/place/get/json"  # resource get method
        get_url = Google_maps_api.base_url + get_resource + Google_maps_api.key + \
                  "&place_id=" + place_id    #  Get requests url
        print(get_url)

        result_get = Http_method.get(get_url)
        print(result_get.text)
        return (result_get)

    @staticmethod
    def put_update_location(place_id):
        put_resource = '/maps/api/place/update/json' # Resource put method
        put_url = Google_maps_api.base_url + put_resource + Google_maps_api.key
        print(put_url)

        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }


        result_put = Http_method.put(put_url,json_for_update_new_location)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_new_location(place_id):
        delete_resource = "/maps/api/place/delete/json"  # Ресурс метода Delete
        put_url = Google_maps_api.base_url + delete_resource + Google_maps_api.key
        print(put_url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = Http_method.delete(put_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete