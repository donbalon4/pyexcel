"""
    pyexcel.plugins.parsers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A list of built-in parsers

    :copyright: (c) 2015-2017 by Onni Software Ltd.
    :license: New BSD License
"""
from pyexcel_io.plugins import readers
from pyexcel_io.constants import DB_SQL, DB_DJANGO

from pyexcel.internal.common import PyexcelPluginList


__pyexcel_plugins__ = PyexcelPluginList(__name__).add_a_parser(
    submodule='excel',
    file_types=readers.get_all_formats()
).add_a_parser(
    submodule='sqlalchemy',
    file_types=[DB_SQL]
).add_a_parser(
    submodule='django',
    file_types=[DB_DJANGO]
)
