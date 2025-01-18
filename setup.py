from setuptools import setup

setup(
    name="webp_converter",
    version="1.0",
    py_modules=["webpconverter"],
    entry_points={
        "console_scripts": [
            "webp-converter=webpconverter:main",
        ],
    },
)
