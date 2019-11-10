# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         fibonacci = esconjugator.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""

import logging
import requests

from bs4 import BeautifulSoup
import pandas as pd


__author__ = "Pavlo Lysytsya"
__copyright__ = "Pavlo Lysytsya"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def conjugate(word, _type=None):
    if _type is None:
        print(f"Please provide the type of the conjugation. Type must be in {Conjugator().types}.")
    else:
        return Conjugator().conjugate(word, _type)


class Conjugator:

    def __init__(self):
        self.base_url = "https://www.spanishdict.com/conjugate/"
        self.types = [
            "Indicative",
            "Subjunctive",
            "Imperative",
            "Continuous (Progressive)",
            "Perfect",
            "Perfect Subjunctive",
        ]

    def conjugate(self, word, _type):
        html = self.get_html(word)
        assert _type in self.types, f"Type must be in {self.types}"
        assert self.is_spanish(html), f"{word} is not spanish"
        html_tables = self.get_tables(html)
        html_table = html_tables[self.types.index(_type)]
        df = self.make_dataframe(self.extract_table(html_table))
        return df

    def get_html(self, word):
        return requests.get(self.base_url + word).text

    def is_spanish(self, html):
        results = [True for indicator in self.types if indicator in html]
        if len(results) == len(self.types):
            return True
        else:
            return False

    def get_tables(self, html):
        soup = BeautifulSoup(html, features="html.parser")
        tables = soup.find_all("table", {"class": "vtable"})
        return tables

    def extract_table(self, html):
        data = []
        rows = html.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])  # Get rid of empty values
        return data

    def make_dataframe(self, conjugations):
        header = ["Person"] + conjugations[0]
        body = conjugations[1:]
        df = pd.DataFrame(body)
        df.columns = header
        return df
