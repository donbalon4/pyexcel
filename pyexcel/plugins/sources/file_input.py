"""
    pyexcel.plugins.sources.file_input
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Representation of input file sources

    :copyright: (c) 2015-2017 by Onni Software Ltd.
    :license: New BSD License
"""
import os

from pyexcel.internal import PARSER
import pyexcel.constants as constants
from . import params
from .file_sources import InputSource


# pylint: disable=W0223
class ReadExcelFromFile(InputSource):
    """Pick up 'file_name' field and do single sheet based read and write
    """
    fields = [params.FILE_NAME]
    targets = (constants.SHEET, constants.BOOK)
    actions = (constants.READ_ACTION,)

    def __init__(self, file_name=None, **keywords):
        self.__file_name = file_name

        file_type = self.__file_name.split('.')[-1]
        self.__parser = PARSER.get_a_plugin(file_type)
        InputSource.__init__(self, **keywords)

    def get_source_info(self):
        path, file_name = os.path.split(self.__file_name)
        return file_name, path

    def get_data(self):
        """
        Return a dictionary with only one key and one value
        """
        sheets = self.__parser.parse_file(self.__file_name, **self._keywords)
        return sheets
