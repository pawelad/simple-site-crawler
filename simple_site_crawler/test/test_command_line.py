import pytest
from click.testing import CliRunner

from simple_site_crawler.command_line import cli


# Fixtures
@pytest.fixture(scope='function')
def runner():
    """Get CliRunner"""
    return CliRunner()


# Tests
# TODO: Mock `SiteCrawler` and don't actually crawl test website
@pytest.mark.parametrize('cli_args', [
    ('http://example.com',),
    ('-t', '5', 'http://example.com'),
    ('--max-tasks', '50', 'http://example.com'),
])
def test_running_the_script(runner, cli_args):
    """Test running the script on 'http://example.com' website"""
    result = runner.invoke(
        cli, args=list(cli_args),
    )

    assert result.exit_code == 0
    assert result.output
    assert result.output.startswith('http://example.com')
    assert 'http://www.iana.org/domains/example' in result.output
    assert result.output.count('\n') == 5


@pytest.mark.parametrize('cli_args', [
    ('-e', 'http://example.com'),
    ('--export-to-xml', 'http://example.com'),
])
def test_exporting_to_xml(runner, mocker, cli_args):
    """Test exporting sitemap to XML file"""
    mocked_generate_sitemap_xml = mocker.patch(
        'simple_site_crawler.command_line.generate_sitemap_xml'
    )

    result = runner.invoke(
        cli, args=list(cli_args),
    )

    assert mocked_generate_sitemap_xml.call_count == 1

    assert result.exit_code == 0
    assert result.output
    assert result.output.count('\n') == 7


def test_suppress_option(runner):
    """Test running the with 'suppress' option"""
    result = runner.invoke(
        cli, args=['-s', 'http://example.com'],
    )

    assert result.exit_code == 0
    assert result.output
    assert result.output.startswith('All done!')
    assert result.output.count('\n') == 1
