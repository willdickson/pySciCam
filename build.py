# build.py
from typing import Any, Dict
from setuptools import Extension
from setuptools.command.build_ext import build_ext

ext_modules = [

    Extension(
        "libbayer", 
        sources=["src/bayer/bayer.c"], 
        export_symbols=["dc1394_bayer_dencoding_8bit", "dc1394_bayer_decoding_16bit"]
        ),
]

def build(setup_kwargs: Dict[str, Any]) -> None:
    print('hello')
    setup_kwargs.update(
        {
            "ext_modules": ext_modules,
            "cmdclass": dict(build_ext=build_ext),
            "zip_safe": False,
        }
    )

