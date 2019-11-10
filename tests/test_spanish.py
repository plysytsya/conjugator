# -*- coding: utf-8 -*-

import logging
import unittest

import pandas as pd

from conjugator.spanish import Conjugator

__author__ = "Pavlo Lysytsya"
__copyright__ = "Pavlo Lysytsya"
__license__ = "mit"


class TestConjugator(unittest.TestCase):
    def setup_method(self, test_method):
        self.conjugator = Conjugator()

    def teardown_method(self, test_method):
        logging.info("tearing down")

    def test_get_html(self):
        words = ["hacer", ""]
        for word in words:
            html = self.conjugator.get_html(word)
            self.assertIsInstance(html, str)

    def test_is_spanish(self):
        words = ["hacer", "tener", "levantar"]
        for word in words:
            html = self.conjugator.get_html(word)
            self.assertEqual(
                True,
                self.conjugator.is_spanish(html),
                f"Spanish word '{word}' is not recognized as spanish.",
            )

    def test_is_not_spanish(self):
        words = ["eat", ""]
        for word in words:
            html = self.conjugator.get_html(word)
            self.assertEqual(
                False,
                self.conjugator.is_spanish(html),
                f"Not word '{word}' is recognized as spanish.",
            )

    def test_has_types(self):
        types = [
            "Indicative",
            "Subjunctive",
            "Imperative",
            "Continuous (Progressive)",
            "Perfect",
            "Perfect Subjunctive",
        ]
        self.assertEqual(types, self.conjugator.types)

    def test_get_tables(self):
        html = self.conjugator.get_html("hacer")
        tables = self.conjugator.get_tables(html)
        self.assertIsInstance(tables, list)
        self.assertEqual(6, len(tables))

    def test_extract_table(self):
        html = self.conjugator.get_html("hacer")
        tables = self.conjugator.get_tables(html)
        table = self.conjugator.extract_table(tables[1])
        self.assertIsInstance(table, list)

    def test_make_dataframe(self):
        test_list = [
            ["Present", "Imperfect", "Imperfect 2", "Future"],
            ["yo", "haga", "hiciera", "hiciese", "hiciere"],
            ["tú", "hagas", "hicieras", "hicieses", "hicieres"],
            ["él/ella/Ud.", "haga", "hiciera", "hiciese", "hiciere"],
            ["nosotros", "hagamos", "hiciéramos", "hiciésemos", "hiciéremos"],
            ["vosotros", "hagáis", "hicierais", "hicieseis", "hiciereis"],
            ["ellos/ellas/Uds.", "hagan", "hicieran", "hiciesen", "hicieren"],
        ]
        df = self.conjugator.make_dataframe(test_list)
        self.assertIsInstance(df, pd.core.frame.DataFrame)

    def test_conjugate(self):
        conjugation = self.conjugator.conjugate("hacer", "Perfect")
        self.assertIsInstance(conjugation, pd.core.frame.DataFrame)
