from setuptools import setup, find_packages


def readme():
    with open("README.md", 'r') as f:
        return f.read()


setup(
    name="webclip",
    description="Demo project for Docker for Developers talk. Clipboard as a service.",
    version="0.0.1",
    long_description=readme(),
    author="Brian Balsamo",
    author_email="brian@brianbalsamo.com",
    packages=find_packages(
        exclude=[
        ]
    ),
    include_package_data=True,
    url='https://github.com/bnbalsamo/webclip',
    install_requires=[
        'redis'
    ],
    entry_points={
        'console_scripts': [
            'webclip = webclip:main'
        ]
    },
    tests_require=[
        'pytest'
    ],
    test_suite='tests'
)
