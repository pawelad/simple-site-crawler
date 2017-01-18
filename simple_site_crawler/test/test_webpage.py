import os
from uuid import uuid4

import pytest
from bs4 import BeautifulSoup

from simple_site_crawler.webpage import Webpage


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


# Fixtures
@pytest.fixture(scope='module')
def html_content():
    """Return example HTML content"""
    file_path = os.path.join(BASE_DIR, 'files', 'example.html')
    with open(file_path) as f:
        content = f.read()

    return content


# Tests
def test_initialization(html_content):
    """Test class initialization"""
    url = str(uuid4())
    content = html_content

    webpage = Webpage(
        url=url,
        content=content,
    )

    assert webpage.url == url
    assert webpage.content == content

    assert webpage.soup == BeautifulSoup(content, 'html5lib')

    assert webpage.links == webpage.get_website_links()
    assert webpage.images == webpage.get_website_images()
    assert webpage.css == webpage.get_website_css()
    assert webpage.javascript == webpage.get_website_javascript()


def test_get_website_links(html_content):
    """Test `get_website_links()` method"""
    webpage = Webpage(
        url=str(uuid4()),
        content=html_content,
    )

    links = webpage.get_website_links()
    expected_links = [
        'https://google.com/', 'https://www.python.org/',
    ]

    assert set(links) == set(expected_links)


def test_get_website_images(html_content):
    """Test `get_website_images()` method"""
    webpage = Webpage(
        url=str(uuid4()),
        content=html_content,
    )

    images = webpage.get_website_images()
    expected_images = [
        'https://www.google.com/logo.png',
        'https://www.python.org/logo.png'
    ]

    assert set(images) == set(expected_images)


def test_get_website_css(html_content):
    """Test `get_website_css()` method"""
    webpage = Webpage(
        url=str(uuid4()),
        content=html_content,
    )

    css = webpage.get_website_css()
    expected_css = [
        'https://fonts.googleapis.com/css?family=Roboto',
        'https://code.getmdl.io/1.3.0/material.indigo-pink.min.css'
    ]

    assert set(css) == set(expected_css)


def test_get_website_javascript(html_content):
    """Test `get_website_javascript()` method"""
    webpage = Webpage(
        url=str(uuid4()),
        content=html_content,
    )

    js = webpage.get_website_javascript()
    expected_js = [
        'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
        'https://code.getmdl.io/1.3.0/material.min.js'
    ]

    assert set(js) == set(expected_js)
