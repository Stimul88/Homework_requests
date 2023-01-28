from pprint import pprint

import requests

from Homework_requests_2_task import YandexDisk

TOKEN = ""


if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    ya.upload_file_to_disk("netology/test23.txt", "test.txt")
