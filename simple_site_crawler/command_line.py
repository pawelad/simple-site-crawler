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
@click.option('--suppress', '-s', is_flag=True, default=False,
              help="Suppress printing output to stdout.")
@click.argument('URL', type=str)
def cli(max_tasks, export_to_xml, suppress, url):
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
    end_time = time.time()

    run_time = end_time - start_time

    # Create a standard 'sitemap.xml' from found URLs
    if export_to_xml:
        urls = [page for page in sitemap.crawled_pages.keys()]
        generate_sitemap_xml(urls)

        click.secho(
            "Sitemap saved as 'sitemap.xml'", fg='yellow'
        )
        click.echo()

    # Print sitemap to stdout
    if not suppress:
        for webpage in sitemap.crawled_pages.values():
            click.secho(webpage.url, fg='yellow')

            # We do it this way to nicely print children even if some of the
            # groups are empty and we don't know which will be printed last
            groups = [
                ('Links', webpage.links),
                ('Images', webpage.images),
                ('CSS files', webpage.css),
                ('JavaScript files', webpage.javascript),
            ]
            # Get rid of empty values
            groups = [item for item in groups if item[1]]

            for group_name, group_items in groups[:-1]:
                click.secho('├── {}'.format(group_name), fg='blue')
                click.echo(render_children(group_items))

            last_group_name, last_group_items = groups[-1]
            click.secho('└── {}'.format(last_group_name), fg='blue')
            click.echo(render_children(
                last_group_items,
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
