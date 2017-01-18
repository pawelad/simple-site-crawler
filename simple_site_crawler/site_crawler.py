import aiohttp
import asyncio
from collections import OrderedDict
from urllib.parse import urlsplit


from simple_site_crawler.webpage import Webpage


class SiteCrawler:
    """
    Site crawler that uses `asyncio` and `aiohttp` libraries to
    asynchronously crawl the website and create its sitemap
    """
    def __init__(self, url, max_tasks=100):
        """
        Initializes class instance with website URL

        :param url: website URL
        :type url: str
        :param max_tasks: maximum number of asynchronous tasks
        :type max_tasks: int
        """
        url_split = urlsplit(url)
        self.root_url = '{0.scheme}://{0.netloc}/'.format(url_split)
        self.root_domain = '{0.netloc}'.format(url_split)
        self.max_tasks = max_tasks

        self.loop = asyncio.get_event_loop()
        self.queue = asyncio.Queue()

        self.crawled_pages = OrderedDict()

        self.add_page(self.root_url)

    def add_page(self, url):
        """
        Add webpage to the queue if it wasn't crawled before and belongs to
        the root domain

        :param url: webpage url
        :type url: str
        """
        domain = urlsplit(url).netloc

        if url not in self.crawled_pages.keys() and domain == self.root_domain:
            self.queue.put_nowait(url)

    async def crawl_webpage(self, session, url):
        """
        Crawl a webpage

        :param session: aiohttp session instance
        :type session: ClientSession
        :param url: webpage url
        :type url: str
        """
        with aiohttp.Timeout(10):
            async with session.get(url) as response:
                content = await response.text()

        webpage = Webpage(
            url=url,
            content=content,
        )
        self.crawled_pages[url] = webpage

        # Add found links to the queue
        for link in webpage.links:
            self.add_page(link)

    async def worker(self, session):
        """
        Single worker that takes next free URL from the queue and crawls it

        :param session: aiohttp session instance
        :type session: ClientSession
        """
        try:
            while True:
                url = await self.queue.get()
                await self.crawl_webpage(session, url)
                self.queue.task_done()
        except asyncio.CancelledError:
            pass

    async def crawl_website(self):
        """
        Crawl website asynchronously until all found links are crawled
        """
        async with aiohttp.ClientSession() as session:
            workers = [
                asyncio.Task(self.worker(session))
                for _ in range(self.max_tasks)
            ]

            await self.queue.join()

            # Cancel worker after everything is done
            for w in workers:
                w.cancel()
