# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiOduDegThrType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    PERCENTAGE = "PERCENTAGE"
    NUMBER_ERRORED_BLOCKS = "NUMBER_ERRORED_BLOCKS"

    def __init__(self):  # noqa: E501
        """TapiOduDegThrType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOduDegThrType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.odu.DegThrType of this TapiOduDegThrType.  # noqa: E501
        :rtype: TapiOduDegThrType
        """
        return util.deserialize_model(dikt, cls)
