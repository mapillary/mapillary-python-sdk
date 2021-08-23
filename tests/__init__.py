# Copyright (c) Facebook, Inc. and its affiliates. (http://www.facebook.com)
# -*- coding: utf-8 -*-

"""
tests.__init__

This module loads the test modules under tests/

:copyright: (c) 2021 Facebook
:license: MIT LICENSE
"""

# Configuration
from . import conftest  # noqa: F401

# Utils testing
from . import utils as tests_utils  # noqa: F401

# Helper testing
from . import helper as tests_helper  # noqa: F401
