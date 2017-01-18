import io
import os
import re

from setuptools import setup, find_packages


# Convert description from markdown to reStructuredText
try:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst', 'markdown')
except (OSError, ImportError):
    description = ''


# Get package version number
# Source: https://packaging.python.org/single_source_version/
def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='simple-site-crawler',
    url='https://github.com/pawelad/simple-site-crawler',
    download_url='https://github.com/pawelad/simple-site-crawler/releases'
                 '/latest',
    bugtrack_url='https://github.com/pawelad/simple-site-crawler/issues',
    version=find_version('simple_site_crawler', '__init__.py'),
    license='MIT License',
    author='Paweł Adamczak',
    author_email='pawel.ad@gmail.com',
    maintainer='Paweł Adamczak',
    maintainer_email='pawel.ad@gmail.com',
    description='Simple website crawler that asynchronously crawls a website '
                'and all subpages that it can find, along with static content '
                'that they rely on.',
    long_description=description,
    packages=find_packages(),
    include_package_data=True,
    scripts=['bin/simple-site-crawler'],
    install_requires=[
        'aiodns>=1.1.1',
        'aiohttp>=1.2.0',
        'beautifulsoup4>=4.5.3',
        'click>=6.7',
        'cchardet>=1.1.2',
        'html5lib>=1.0b10',
    ],
    extras_require={
        'testing': ['pytest'],
    },
    keywords='website crawler sitemap',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
)
