# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from nadiki_registrar.models.base_model_ import Model
from nadiki_registrar import util


class RackUpdate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, facility_id=None, total_available_power=5, total_available_cooling_capacity=5, number_of_pdus=2, power_redundancy=2, product_passport=None, description=None):  # noqa: E501
        """RackUpdate - a model defined in OpenAPI

        :param facility_id: The facility_id of this RackUpdate.  # noqa: E501
        :type facility_id: str
        :param total_available_power: The total_available_power of this RackUpdate.  # noqa: E501
        :type total_available_power: float
        :param total_available_cooling_capacity: The total_available_cooling_capacity of this RackUpdate.  # noqa: E501
        :type total_available_cooling_capacity: float
        :param number_of_pdus: The number_of_pdus of this RackUpdate.  # noqa: E501
        :type number_of_pdus: int
        :param power_redundancy: The power_redundancy of this RackUpdate.  # noqa: E501
        :type power_redundancy: int
        :param product_passport: The product_passport of this RackUpdate.  # noqa: E501
        :type product_passport: object
        :param description: The description of this RackUpdate.  # noqa: E501
        :type description: str
        """
        self.openapi_types = {
            'facility_id': str,
            'total_available_power': float,
            'total_available_cooling_capacity': float,
            'number_of_pdus': int,
            'power_redundancy': int,
            'product_passport': object,
            'description': str
        }

        self.attribute_map = {
            'facility_id': 'facility_id',
            'total_available_power': 'total_available_power',
            'total_available_cooling_capacity': 'total_available_cooling_capacity',
            'number_of_pdus': 'number_of_pdus',
            'power_redundancy': 'power_redundancy',
            'product_passport': 'product_passport',
            'description': 'description'
        }

        self._facility_id = facility_id
        self._total_available_power = total_available_power
        self._total_available_cooling_capacity = total_available_cooling_capacity
        self._number_of_pdus = number_of_pdus
        self._power_redundancy = power_redundancy
        self._product_passport = product_passport
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'RackUpdate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RackUpdate of this RackUpdate.  # noqa: E501
        :rtype: RackUpdate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def facility_id(self):
        """Gets the facility_id of this RackUpdate.

        ID of the facility where the rack is located  # noqa: E501

        :return: The facility_id of this RackUpdate.
        :rtype: str
        """
        return self._facility_id

    @facility_id.setter
    def facility_id(self, facility_id):
        """Sets the facility_id of this RackUpdate.

        ID of the facility where the rack is located  # noqa: E501

        :param facility_id: The facility_id of this RackUpdate.
        :type facility_id: str
        """
        if facility_id is None:
            raise ValueError("Invalid value for `facility_id`, must not be `None`")  # noqa: E501

        self._facility_id = facility_id

    @property
    def total_available_power(self):
        """Gets the total_available_power of this RackUpdate.

        Total available power in kW  # noqa: E501

        :return: The total_available_power of this RackUpdate.
        :rtype: float
        """
        return self._total_available_power

    @total_available_power.setter
    def total_available_power(self, total_available_power):
        """Sets the total_available_power of this RackUpdate.

        Total available power in kW  # noqa: E501

        :param total_available_power: The total_available_power of this RackUpdate.
        :type total_available_power: float
        """

        self._total_available_power = total_available_power

    @property
    def total_available_cooling_capacity(self):
        """Gets the total_available_cooling_capacity of this RackUpdate.

        Total available cooling capacity in kW  # noqa: E501

        :return: The total_available_cooling_capacity of this RackUpdate.
        :rtype: float
        """
        return self._total_available_cooling_capacity

    @total_available_cooling_capacity.setter
    def total_available_cooling_capacity(self, total_available_cooling_capacity):
        """Sets the total_available_cooling_capacity of this RackUpdate.

        Total available cooling capacity in kW  # noqa: E501

        :param total_available_cooling_capacity: The total_available_cooling_capacity of this RackUpdate.
        :type total_available_cooling_capacity: float
        """

        self._total_available_cooling_capacity = total_available_cooling_capacity

    @property
    def number_of_pdus(self):
        """Gets the number_of_pdus of this RackUpdate.

        Number of PDUs in the rack  # noqa: E501

        :return: The number_of_pdus of this RackUpdate.
        :rtype: int
        """
        return self._number_of_pdus

    @number_of_pdus.setter
    def number_of_pdus(self, number_of_pdus):
        """Sets the number_of_pdus of this RackUpdate.

        Number of PDUs in the rack  # noqa: E501

        :param number_of_pdus: The number_of_pdus of this RackUpdate.
        :type number_of_pdus: int
        """
        if number_of_pdus is not None and number_of_pdus < 1:  # noqa: E501
            raise ValueError("Invalid value for `number_of_pdus`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_of_pdus = number_of_pdus

    @property
    def power_redundancy(self):
        """Gets the power_redundancy of this RackUpdate.

        Number of power feeds used for redundancy  # noqa: E501

        :return: The power_redundancy of this RackUpdate.
        :rtype: int
        """
        return self._power_redundancy

    @power_redundancy.setter
    def power_redundancy(self, power_redundancy):
        """Sets the power_redundancy of this RackUpdate.

        Number of power feeds used for redundancy  # noqa: E501

        :param power_redundancy: The power_redundancy of this RackUpdate.
        :type power_redundancy: int
        """
        if power_redundancy is not None and power_redundancy < 1:  # noqa: E501
            raise ValueError("Invalid value for `power_redundancy`, must be a value greater than or equal to `1`")  # noqa: E501

        self._power_redundancy = power_redundancy

    @property
    def product_passport(self):
        """Gets the product_passport of this RackUpdate.

        LCA product passport data  # noqa: E501

        :return: The product_passport of this RackUpdate.
        :rtype: object
        """
        return self._product_passport

    @product_passport.setter
    def product_passport(self, product_passport):
        """Sets the product_passport of this RackUpdate.

        LCA product passport data  # noqa: E501

        :param product_passport: The product_passport of this RackUpdate.
        :type product_passport: object
        """

        self._product_passport = product_passport

    @property
    def description(self):
        """Gets the description of this RackUpdate.

        Textual description ob the facility for informational purposes  # noqa: E501

        :return: The description of this RackUpdate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RackUpdate.

        Textual description ob the facility for informational purposes  # noqa: E501

        :param description: The description of this RackUpdate.
        :type description: str
        """

        self._description = description
