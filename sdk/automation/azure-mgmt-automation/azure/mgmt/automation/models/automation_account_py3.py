# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .tracked_resource_py3 import TrackedResource


class AutomationAccount(TrackedResource):
    """Definition of the automation account type.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: The Azure Region where the resource lives
    :type location: str
    :param sku: Gets or sets the SKU of account.
    :type sku: ~azure.mgmt.automation.models.Sku
    :param last_modified_by: Gets or sets the last modified by.
    :type last_modified_by: str
    :ivar state: Gets status of account. Possible values include: 'Ok',
     'Unavailable', 'Suspended'
    :vartype state: str or
     ~azure.mgmt.automation.models.AutomationAccountState
    :ivar creation_time: Gets the creation time.
    :vartype creation_time: datetime
    :ivar last_modified_time: Gets the last modified time.
    :vartype last_modified_time: datetime
    :param description: Gets or sets the description.
    :type description: str
    :param etag: Gets or sets the etag of the resource.
    :type etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'state': {'readonly': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'sku': {'key': 'properties.sku', 'type': 'Sku'},
        'last_modified_by': {'key': 'properties.lastModifiedBy', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, tags=None, location: str=None, sku=None, last_modified_by: str=None, description: str=None, etag: str=None, **kwargs) -> None:
        super(AutomationAccount, self).__init__(tags=tags, location=location, **kwargs)
        self.sku = sku
        self.last_modified_by = last_modified_by
        self.state = None
        self.creation_time = None
        self.last_modified_time = None
        self.description = description
        self.etag = etag
