import json
from requests import Response


class Checking:
    """method checking requests"""

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f'status code: OK = {str(response.status_code)}')

    @staticmethod
    def check_json_response(response: Response, expected):
        token = json.loads(response.text)
        assert list(token) == expected
        print('All fields: OK')

    @staticmethod
    def check_value(response: Response, field, expected):
        check = response.json()
        info = check[field]
        assert info == expected
        print(f'{field} = OK')

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == check.get(field_name)
        if search_word in check_info:
            print('the word is present')
        else:
            print("the word is missing")




