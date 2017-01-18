# simple-site-crawler
[![Build status](https://img.shields.io/travis/pawelad/simple-site-crawler.svg)][travis]
[![Test coverage](https://img.shields.io/coveralls/pawelad/simple-site-crawler.svg)][coveralls]
[![PyPI version](https://img.shields.io/pypi/v/simple-site-crawler.svg)][pypi]
[![Python versions](https://img.shields.io/pypi/pyversions/simple-site-crawler.svg)][pypi]
[![License](https://img.shields.io/github/license/pawelad/simple-site-crawler.svg)][license]

Simple website crawler that asynchronously crawls a website and all subpages
that it can find, along with static content that they rely on. You can either
use it as a library, inside your Python project or check out the provided CLI
that can currently show you the crawled data (links, images, CSS and Javascript
files) for each found site amd create a `sitemap.xml` file.

Created primarily to play with `asyncio`, `aiohttp` and the new `async/await`
syntax, so:

- it requires Python 3.5 or higher
- new features are not planned at the moment; feel free to suggest them though,
as I'm happy to implement them if someone will actually use them ; -)

Full disclosure - halfway through the project I found [this][crawler] article
(and code) which does pretty much exactly what I wanted and is co-written by
the BDFL himself. Oh well. I still finished the project and didn't copy anything
explicitly but it did influence some of my choices. After all, if it's good
enough for the creator of the language I'm using, it's probably good enough for
me.

## Installation
From PyPI:

```
$ pip3 install simple-site-crawler
```

With git clone:

```
$ git clone https://github.com/pawelad/simple-site-crawler
$ pip3 install -r simple-site-crawler/requirements.txt
$ cd simple-site-crawler/bin
```

## Usage

```
$ simple-site-crawler --help                      
Usage: simple-site-crawler [OPTIONS] URL

  Simple website crawler that generates its sitemap and can either print it
  (and its static content) or export it to standard XML format.

  See https://github.com/pawelad/simple-site-crawler for more info.

Options:
  -t, --max-tasks INTEGER  Maximum allowed number of async tasks.
  -e, --export-to-xml      Export sitemap to XML file.
  -s, --suppress           Suppress printing output to stdout.
  --help                   Show this message and exit.
```

## API
There's no proper documentation as of now, but the code is commented and
*should* be pretty straightforward to use.

That said - feel free to ask me either via [email](mailto:pawel.ad@gmail.com)
or [GitHub issues][github add issue] if anything is unclear.

## Tests
Package was tested with the help of `py.test` and `tox` on Python 3.5 and 3.6
(see `tox.ini`).

Code coverage is available at [Coveralls][coveralls].

To run tests yourself you need to run `tox` inside the repository:

```shell
$ pip install -r requirements/dev.txt
$ tox
```

## Contributions
Package source code is available at [GitHub][github].

Feel free to use, ask, fork, star, report bugs, fix them, suggest enhancements,
add functionality and point out any mistakes. Thanks!

## Authors
Developed and maintained by [Paweł Adamczak][pawelad].

Released under [MIT License][license].


[coveralls]: https://coveralls.io/github/pawelad/simple-site-crawler
[crawler]: http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html
[github]: https://github.com/pawelad/simple-site-crawler
[github add issue]: https://github.com/pawelad/simple-site-crawler/issues/new
[license]: https://github.com/pawelad/simple-site-crawler/blob/master/LICENSE
[pawelad]: https://github.com/pawelad
[pypi]: https://pypi.python.org/pypi/simple-site-crawler
[travis]: https://travis-ci.org/pawelad/simple-site-crawler
