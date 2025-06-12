from setuptools import setup

setup(
    name="sumadora",
    version="0.1.0",
    description="Una app Flask simple que suma dos números",
    packages=["."],
    install_requires=[
        "flask",
        "gunicorn"
    ],
)
