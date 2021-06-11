"""
Implement PEP 660, plus the existing setuptools PEP 517 hooks.
"""

from setuptools.build_meta import *


def build_wheel_for_editable(wheel_directory, scheme=None, config_settings=None):
    raise NotImplementedError()


def get_requires_for_build_wheel_for_editable(config_settings=None):
    raise NotImplementedError()