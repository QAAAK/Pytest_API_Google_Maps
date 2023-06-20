import datetime
import os

from requests import Response


class Log:
    """Saving test data to a log"""


    file_name = f'logs/log_'+ str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name,'a',encoding='utf-8') as logs_file:
            logs_file.write(data)

    @classmethod
    def add_requests(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_add = f'\n-----\n'
        data_add +=f'test: {test_name}\n'
        data_add += f'time: {str(datetime.datetime.now())}\n'
        data_add += f'Request method: {method}\n'
        data_add += f'Request URL: {url}\n'
        data_add += '\n'

        cls.write_log_to_file(data_add)

    @classmethod
    def add_response(cls,result: Response):
        cookies = dict(result.cookies)
        headers = dict(result.headers)

        data_add = f"Response code: {result.status_code}\n"
        data_add += f"Response text: {result.text}\n"
        data_add += f"Response headers: {headers}\n"
        data_add += f"Response cookies: {cookies}\n"
        data_add += f"\n-----\n"

        cls.write_log_to_file(data_add)


