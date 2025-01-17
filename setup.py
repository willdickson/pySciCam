#/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
    Read images from high speed and scientific cameras in Python
    
    @author Daniel Duke <daniel.duke@monash.edu>
    @copyright (c) 2018-2022 LTRAC
    @license GPL-3.0+
    @version 0.4.4
    @date 11/08/2022
        __   ____________    ___    ______
       / /  /_  ____ __  \  /   |  / ____/
      / /    / /   / /_/ / / /| | / /
     / /___ / /   / _, _/ / ___ |/ /_________
    /_____//_/   /_/ |__\/_/  |_|\__________/
    
    Laboratory for Turbulence Research in Aerospace & Combustion (LTRAC)
    Monash University, Australia
    
    Please see help(pySciCam) for more information.
"""
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

cython_modules = [
    Extension(
        "pySciCam.chronos14_raw",
        ["src/pySciCam/chronos14_raw.pyx"],
    ),
    Extension(
        "pySciCam.b16_raw",
        ["src/pySciCam/b16_raw.pyx"],
    ),
    Extension(
        "pySciCam.photron_mraw",
        ["src/pySciCam/photron_mraw.pyx"],
    )
]

c_libraries = [
    Extension(
        "libbayer",
        sources = ["src/bayer/bayer.c"],
        export_symbols = ["dc1394_bayer_decoding_8bit", "dc1394_bayer_decoding_16bit"]
    )
]

setup(packages=['pySciCam','bayer'],
      package_dir={'': 'src'},
      url='daniel-duke.net',
      ext_modules=cythonize(cython_modules, language_level = "3") + c_libraries,
      include_dirs=[numpy.get_include()]
)
