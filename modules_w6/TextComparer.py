from typing import List
import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import pandas as pd
from pathlib import Path


class NotFoundException(ValueError):

    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)


class TextComparer():

    def __init__(self, urllist):
        self.urllist = urllist
        self.file_list = []

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i == len(self.file_list):
            raise StopIteration  # signals "the end"
        self.i += 1
        return self.file_list[self.i-1]

    def download(self, url, filename=''):
        self.file_list = []
        r = requests.get(url, allow_redirects=True)
        if (filename == ''):
            filename = url.split('/')[-1]

        if r.status_code == 404:
            raise NotFoundException(f'Oh no, {url} is not found!')

        else:
            open(filename, 'wb').write(r.content)
            self.file_list.append(filename)

    def urllist_generator(self):
        for url in self.urllist:
            yield url

    def multi_download(self):
        with ThreadPoolExecutor(max_workers=10) as ex:
            res = ex.map(self.download, self.urllist)

    def avg_vowels(self, file):
        text_file = open(file, 'r')
        text = text_file.read()
        words = len(text.split())
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for char in text:
            if char in vowels:  # check if each char in your string is in your list of vowels
                count += 1
        return (count/words, file)

    def avg_book(self):
        with ProcessPoolExecutor(multiprocessing.cpu_count()) as ex:
            res = ex.map(self.avg_vowels, self.file_list)
        return sorted(list(res))

    def hardest_read(self):
        avg_book_list = self.avg_book()
        (avg, book) = avg_book_list[-1]
        return book
