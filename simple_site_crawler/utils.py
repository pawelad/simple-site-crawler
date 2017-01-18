import xml.etree.cElementTree as ET
from xml.dom import minidom


def generate_sitemap_xml(urls, filename='sitemap.xml'):
    """
    Generate 'sitemap.xml' file based on passed urls

    :param urls: list of URLs
    :type urls: list of str
    :param filename: output file name
    :type filename: str
    """
    urlset = ET.Element(
        'urlset',
        xmlns='http://www.sitemaps.org/schemas/sitemap/0.9',
    )

    for webpage_url in urls:
        url = ET.SubElement(urlset, 'url')
        ET.SubElement(url, 'loc').text = webpage_url

    pretty_xml = minidom.parseString(
        ET.tostring(urlset),
    ).toprettyxml(
        encoding='UTF-8',
    )

    with open(filename, 'wb') as f:
        f.write(pretty_xml)


def render_children(children, prefix='│   ├── ', last_item_prefix='│   └── '):
    """
    Simple helper for rendering element children

    :param children: children container
    :type children: iterable object
    :param prefix: string that will prefix the child element
    :type prefix: str
    :param last_item_prefix: string that will prefix the last child elemment
    :return: rendered children string
    :rtype: str
    """
    s = ''

    for item in children[:-1]:
        s += '{}{}\n'.format(prefix, item)

    s += '{}{}'.format(last_item_prefix, children[-1])

    return s
