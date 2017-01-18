import os
from tempfile import NamedTemporaryFile

from simple_site_crawler.utils import generate_sitemap_xml, render_children


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


# Tests
def test_generate_sitemap_xml():
    """Test `generate_sitemap_xml()` function"""
    tmp_f = NamedTemporaryFile(delete=False)
    generate_sitemap_xml(
        urls=['http://example.com/'], filename=tmp_f.name,
    )

    # Read generated sitemap.xml content
    with open(tmp_f.name) as f:
        generated_sitemap = f.read()

    # Read expected sitemap.xml content
    file_path = os.path.join(BASE_DIR, 'files', 'sitemap.xml')
    with open(file_path) as f:
        expected_sitemap = f.read()

    assert generated_sitemap == expected_sitemap


def test_render_children():
    """Test `render_children()` function"""
    children = ['child A', 'child B', 'child C']

    expected_outcome = (
        '│   ├── child A\n'
        '│   ├── child B\n'
        '│   └── child C'
    )
    rendered_children = render_children(children)

    assert expected_outcome == rendered_children


def test_render_children_with_custom_prefixes():
    """Test `render_children()` function with custom prefixes"""
    children = ['child A', 'child B', 'child C']

    expected_outcome = (
        '    ├~~child A\n'
        '    ├~~child B\n'
        '    └~~child C'
    )
    rendered_children = render_children(
        children=children,
        prefix='    ├~~',
        last_item_prefix='    └~~',
    )

    assert expected_outcome == rendered_children
