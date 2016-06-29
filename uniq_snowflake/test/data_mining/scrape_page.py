###########
# Imports #
###########

import unittest


###################
# Testing Library #
###################
from my_tools.data_mining.scrape_page import get_page_data, get_soup_body, extract_data


class TestScrapePage(unittest.TestCase):

    def test_get_soup_body(self):
        url = "https://docs.python.org/3/tutorial/"
        test_data = get_page_data(url)
        expected_res = []
        res = get_soup_body(test_data)

        self.assertEqual(expected_res, res)

    def test_extract_data(self):
        sample_input = ['<tr><h1>keyThis</h1><h2>\xc2</h2><h3>\xa0</h3><h4>view\xc2\xa0book\xc2\xa0info</h4><h5>Test Passes</h5></tr>']
        expected_res = 'This Test Passes'
        res = extract_data(sample_input)

        self.assertEqual(expected_res, res)


##################
# Test Functions #
##################

if __name__ == '__main__':
    unittest.main()
