import asyncio
import click
import time

from simple_site_crawler import SiteCrawler
from simple_site_crawler.utils import generate_sitemap_xml, render_children


@click.command()
@click.option('--max-tasks', '-t', type=int, default=100,
              help="Maximum allowed number of async tasks.")
@click.option('--export-to-xml', '-e', is_flag=True, default=False,
              help="Export sitemap to XML file.")
@click.argument('URL', type=str)
def cli(max_tasks, export_to_xml, url):
    """
    Simple website crawler that generates its sitemap and can either print it
    (and its static content) or export it to standard XML format.

    See https://github.com/pawelad/simple-site-crawler for more info.
    """
    start_time = time.time()
    loop = asyncio.get_event_loop()

    sitemap = SiteCrawler(
        url=url,
        max_tasks=max_tasks,
    )

    loop.run_until_complete(sitemap.crawl_website())
    loop.close()
    end_time = time.time()

    run_time = end_time - start_time

    if export_to_xml:
        # Create a standard 'sitemap.xml' from found URLs
        urls = [page for page in sitemap.crawled_pages.keys()]
        generate_sitemap_xml(urls)

        click.secho(
            "Sitemap saved as 'sitemap.xml'", fg='yellow'
        )
    else:
        # Print sitemap to stdout
        for webpage in sitemap.crawled_pages.values():
            click.secho(webpage.url, fg='yellow')

            # Links
            if webpage.links:
                click.secho('├── Links', fg='blue')
                click.echo(render_children(webpage.links))

            # Images
            if webpage.images:
                click.secho('├── Images', fg='blue')
                click.echo(render_children(webpage.images))

            # CSS files
            if webpage.css:
                click.secho('├── CSS files', fg='blue')
                click.echo(render_children(webpage.css))

            # JavaScript files
            if webpage.javascript:
                click.secho('└── JavaScript files', fg='blue')
                click.echo(render_children(
                    webpage.javascript,
                    prefix='    ├── ',
                    last_item_prefix='    └── ',
                ))

            click.echo()

    click.secho(
        "All done! Found and crawled {0} websites in {1:.4f} seconds.".format(
            len(sitemap.crawled_pages), run_time,
        ), fg='green',
    )


if __name__ == '__main__':
    cli()
