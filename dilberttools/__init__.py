# Dilbert Tools
# Copyright (c) 2008-2016 Scott Zeid
# https://code.s.zeid.me/dilbert-tools
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA

# __init__.py file
# (No shit, Sherlock.)

from __future__ import print_function

__author__  = "Scott Zeid <support+dilbert-tools@s.zeid.me>"

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


from . import fetch
from . import providers
from . import update
from . import utils


__all__ = [
 "fetch",
 "providers",
 "update",
 "utils",
]
