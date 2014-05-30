# -*- coding: utf-8 -*-
# Copyright (c) 2012-2014, Anima Istanbul
#
# This module is part of anima-tools and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
"""This module contains exceptions
"""


class PublishError(RuntimeError):
    """Raised when the published version is not matching the quality
    """
    pass