from bs4 import BeautifulSoup


class Webpage:
    """
    Class representation of a webpage and all its assets
    """
    def __init__(self, url, content):
        """
        Initializes class instance with website page URL and gets all its
        assets

        :param url: webpage URL
        :type url: str
        :param content: webpage content
        :type content: str
        """
        self.url = url
        self.content = content

        self.soup = BeautifulSoup(self.content, 'html5lib')

        self.links = self.get_website_links()
        self.images = self.get_website_images()
        self.css = self.get_website_css()
        self.javascript = self.get_website_javascript()

    def get_website_links(self):
        """Helper method for getting all links from HTML source"""
        return [
            a.get('href')
            for a in self.soup.select('a')
            if a.get('href')
        ]

    def get_website_images(self):
        """Helper class for getting all images from HTML source"""
        return [
            a.get('src')
            for a in self.soup.select('img')
            if a.get('src')
        ]

    def get_website_css(self):
        """Helper class for getting all CSS files from HTML source"""
        return [
            a.get('href')
            for a in self.soup.select('link[rel=stylesheet]')
            if a.get('href')
        ]

    def get_website_javascript(self):
        """Helper class for getting all JavaScript files from HTML source"""
        return [
            a.get('src')
            for a in self.soup.find_all('script')
            if a.get('src')
        ]
