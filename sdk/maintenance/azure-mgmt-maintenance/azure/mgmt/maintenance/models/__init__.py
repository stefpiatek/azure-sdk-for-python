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

try:
    from ._models_py3 import ApplyUpdate
    from ._models_py3 import ConfigurationAssignment
    from ._models_py3 import ErrorDetails
    from ._models_py3 import MaintenanceConfiguration
    from ._models_py3 import MaintenanceError, MaintenanceErrorException
    from ._models_py3 import Operation
    from ._models_py3 import OperationInfo
    from ._models_py3 import Resource
    from ._models_py3 import Update
except (SyntaxError, ImportError):
    from ._models import ApplyUpdate
    from ._models import ConfigurationAssignment
    from ._models import ErrorDetails
    from ._models import MaintenanceConfiguration
    from ._models import MaintenanceError, MaintenanceErrorException
    from ._models import Operation
    from ._models import OperationInfo
    from ._models import Resource
    from ._models import Update
from ._paged_models import ConfigurationAssignmentPaged
from ._paged_models import MaintenanceConfigurationPaged
from ._paged_models import OperationPaged
from ._paged_models import UpdatePaged
from ._maintenance_management_client_enums import (
    UpdateStatus,
    MaintenanceScope,
    ImpactType,
)

__all__ = [
    'ApplyUpdate',
    'ConfigurationAssignment',
    'ErrorDetails',
    'MaintenanceConfiguration',
    'MaintenanceError', 'MaintenanceErrorException',
    'Operation',
    'OperationInfo',
    'Resource',
    'Update',
    'ConfigurationAssignmentPaged',
    'MaintenanceConfigurationPaged',
    'OperationPaged',
    'UpdatePaged',
    'UpdateStatus',
    'MaintenanceScope',
    'ImpactType',
]
