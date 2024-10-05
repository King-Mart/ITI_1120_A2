import unittest
from a2_part_2_300403489 import *
from unittest.mock import patch


class TestCalculateVotePercentage(unittest.TestCase):
    def test_only_yes_votes(self):
        merged_bulletins = "yes yes yes"
        self.assertEqual(calculate_vote_percentage(merged_bulletins), 1.0)

    def test_only_no_votes(self):
        merged_bulletins = "no no no"
        self.assertEqual(calculate_vote_percentage(merged_bulletins), 0.0)

    def test_both_yes_and_no_votes(self):
        merged_bulletins = "yes no yes no"
        self.assertEqual(calculate_vote_percentage(merged_bulletins), 0.5)

    def test_no_votes(self):
        merged_bulletins = ""
        self.assertEqual(calculate_vote_percentage(merged_bulletins), 0.0)

    def test_invalid_input(self):
        merged_bulletins = "maybe maybe maybe"
        self.assertEqual(calculate_vote_percentage(merged_bulletins), 0.0)

if __name__ == '__main__':
    unittest.main()

class TestVoteFunction(unittest.TestCase):

    @patch('builtins.input', return_value='yes yes yes')
    def test_unanimous_vote(self, mock_input):
        with patch('builtins.print') as mock_print:
            vote()
            mock_print.assert_called_with("proposal passes unanimously")

    @patch('builtins.input', return_value='yes yes no')
    def test_super_majority_vote(self, mock_input):
        with patch('builtins.print') as mock_print:
            vote()
            mock_print.assert_called_with("proposal passes with super majority")

    @patch('builtins.input', return_value='yes no no')
    def test_majority_vote(self, mock_input):
        with patch('builtins.print') as mock_print:
            vote()
            mock_print.assert_called_with("proposal fails")

    @patch('builtins.input', return_value='no no no')
    def test_failed_vote(self, mock_input):
        with patch('builtins.print') as mock_print:
            vote()
            mock_print.assert_called_with("proposal fails")

    @patch('builtins.input', return_value='')
    def test_edge_case_no_votes(self, mock_input):
        with patch('builtins.print') as mock_print:
            vote()
            mock_print.assert_called_with("proposal fails")

    @patch('builtins.input', return_value='invalid input')
    def test_invalid_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            vote()
            mock_print.assert_called_with("proposal fails")

if __name__ == '__main__':
    unittest.main()
class TestL2LOFunction(unittest.TestCase):

    def test_non_negative_integers(self):
        self.assertEqual(l2lo(5), (5, 0))
        self.assertEqual(l2lo(10), (10, 0))

    def test_non_negative_floats(self):
        self.assertEqual(l2lo(5.5), (5, 8))
        self.assertEqual(l2lo(10.25), (10, 4))

    # def test_negative_numbers(self):
    #     with self.assertRaises(ValueError):
    #         l2lo(-1)
    #     with self.assertRaises(ValueError):
    #         l2lo(-5.5)

    def test_zero(self):
        self.assertEqual(l2lo(0), (0, 0))

    def test_large_numbers(self):
        self.assertEqual(l2lo(1000000), (1000000, 0))
        self.assertEqual(l2lo(1000000.5), (1000000, 8))

    

if __name__ == '__main__':
    unittest.main()