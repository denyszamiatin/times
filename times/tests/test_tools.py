import unittest
from times.tools.text_format import scrap_words


class TestTools(unittest.TestCase):

    def test_scrap_words(self):
        case1 = '"більше",."з’їжджаються" туристи'
        case2 = "I'd like to..."
        self.assertEqual(scrap_words(case1), ['більше',
                                              'з’їжджаються',
                                              'туристи'
                                              ])
        self.assertEqual(scrap_words(case2), ["I'd", "like", "to"])
