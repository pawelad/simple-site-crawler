import asyncio
import random
from collections import OrderedDict

from simple_site_crawler.site_crawler import SiteCrawler


# Tests
def test_initialization(mocker):
    """Test class initialization"""
    mocked_add_page = mocker.patch(
        'simple_site_crawler.site_crawler.SiteCrawler.add_page',
    )

    url = 'http://example.co.uk/subpage'
    max_tasks = random.randint(0, 100)

    site_crawler = SiteCrawler(
        url=url,
        max_tasks=max_tasks,
    )

    assert site_crawler.root_url == 'http://example.co.uk/'
    assert site_crawler.root_domain == 'example.co.uk'
    assert site_crawler.max_tasks == max_tasks

    assert isinstance(site_crawler.loop, type(asyncio.get_event_loop()))
    assert isinstance(site_crawler.queue, asyncio.Queue)
    assert isinstance(site_crawler.crawled_pages, OrderedDict)

    mocked_add_page.assert_called_once_with(site_crawler.root_url)


def test_add_page(mocker):
    """Test `add_page()` method"""
    mocked_add_page = mocker.patch(
        'asyncio.Queue.put_nowait',
    )

    site_crawler = SiteCrawler('http://example.com/')
    site_crawler.crawled_pages.update({
        'http://example.com/crawled_page': None,
    })

    site_crawler.add_page('https://google.com/')
    site_crawler.add_page('http://example.com/crawled_page')
    site_crawler.add_page('http://example.com/subpage')

    mocked_add_page.assert_called_with('http://example.com/subpage')
    assert mocked_add_page.call_count == 2


# TODO: Add coroutines tests
