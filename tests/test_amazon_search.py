"""
These tests cover Amazon searches.
Test Escenario:
	Add Item “Laptop” to the cart

Test Cases:
	Validate that the web page domain belongs to www.amazon.com
	search the item “laptop” in the searching box
	validate that the “laptop” exist in the result page

"""

from pages.result import AmazonResultPage
from pages.search import AmazonSearchPage


def test_main_amazon_search(browser):
    search_page = AmazonSearchPage(browser)
    result_page = AmazonResultPage(browser)
    PHRASE = "laptop"

    # When amazon home page is displayed
    search_page.load()

    # When the user searches for "laptpo"
    search_page.search(PHRASE)

    # Validate if the search result title contains "laptop"
    assert PHRASE in result_page.title()

    # Validate if  the search result query  "laptop" exist
    assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to "laptop"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0

    raise Exception("Incomplete Test")
