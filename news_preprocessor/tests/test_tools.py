import unittest
from news_preprocessor.pipes import clear_text


class TestPipes(unittest.TestCase):

    def test_clear_text(self):
        case1 = '"більше",."з’їжджаються" туристи'
        case2 = "I'd like to..."
        self.assertEqual(clear_text(case1), 'більше з’їжджаються туристи')
        self.assertEqual(clear_text(case2), "I'd like to")
