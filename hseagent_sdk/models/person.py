# coding: utf-8

"""
    My API

    Description of my API

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from hseagent_sdk.models.gender_enum import GenderEnum
from hseagent_sdk.models.patched_person_education_level import PatchedPersonEducationLevel
from hseagent_sdk.models.patched_person_marital_status import PatchedPersonMaritalStatus
from hseagent_sdk.models.patched_person_military_service import PatchedPersonMilitaryService
from typing import Optional, Set
from typing_extensions import Self

class Person(BaseModel):
    """
    Person
    """ # noqa: E501
    id: StrictInt
    department: StrictStr
    role: StrictStr
    status: StrictStr
    first_name: Annotated[str, Field(strict=True, max_length=50)]
    last_name: Annotated[str, Field(strict=True, max_length=50)]
    father_name: Annotated[str, Field(strict=True, max_length=50)]
    gender: GenderEnum
    national_code: Annotated[str, Field(strict=True, max_length=10)]
    insurance_code: Optional[Annotated[str, Field(strict=True, max_length=10)]] = None
    employee_code: Optional[Annotated[str, Field(strict=True, max_length=10)]] = None
    birthdate: Optional[date] = None
    education_level: Optional[PatchedPersonEducationLevel] = None
    marital_status: Optional[PatchedPersonMaritalStatus] = None
    number_of_children: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = None
    military_service: Optional[PatchedPersonMilitaryService] = None
    exemption_reason: Optional[Annotated[str, Field(strict=True, max_length=200)]] = None
    is_active: Optional[StrictBool] = None
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    organization: StrictInt
    __properties: ClassVar[List[str]] = ["id", "department", "role", "status", "first_name", "last_name", "father_name", "gender", "national_code", "insurance_code", "employee_code", "birthdate", "education_level", "marital_status", "number_of_children", "military_service", "exemption_reason", "is_active", "created_at", "updated_at", "organization"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Person from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "department",
            "role",
            "status",
            "created_at",
            "updated_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of education_level
        if self.education_level:
            _dict['education_level'] = self.education_level.to_dict()
        # override the default output from pydantic by calling `to_dict()` of marital_status
        if self.marital_status:
            _dict['marital_status'] = self.marital_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of military_service
        if self.military_service:
            _dict['military_service'] = self.military_service.to_dict()
        # set to None if insurance_code (nullable) is None
        # and model_fields_set contains the field
        if self.insurance_code is None and "insurance_code" in self.model_fields_set:
            _dict['insurance_code'] = None

        # set to None if employee_code (nullable) is None
        # and model_fields_set contains the field
        if self.employee_code is None and "employee_code" in self.model_fields_set:
            _dict['employee_code'] = None

        # set to None if birthdate (nullable) is None
        # and model_fields_set contains the field
        if self.birthdate is None and "birthdate" in self.model_fields_set:
            _dict['birthdate'] = None

        # set to None if education_level (nullable) is None
        # and model_fields_set contains the field
        if self.education_level is None and "education_level" in self.model_fields_set:
            _dict['education_level'] = None

        # set to None if marital_status (nullable) is None
        # and model_fields_set contains the field
        if self.marital_status is None and "marital_status" in self.model_fields_set:
            _dict['marital_status'] = None

        # set to None if number_of_children (nullable) is None
        # and model_fields_set contains the field
        if self.number_of_children is None and "number_of_children" in self.model_fields_set:
            _dict['number_of_children'] = None

        # set to None if military_service (nullable) is None
        # and model_fields_set contains the field
        if self.military_service is None and "military_service" in self.model_fields_set:
            _dict['military_service'] = None

        # set to None if exemption_reason (nullable) is None
        # and model_fields_set contains the field
        if self.exemption_reason is None and "exemption_reason" in self.model_fields_set:
            _dict['exemption_reason'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Person from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "department": obj.get("department"),
            "role": obj.get("role"),
            "status": obj.get("status"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "father_name": obj.get("father_name"),
            "gender": obj.get("gender"),
            "national_code": obj.get("national_code"),
            "insurance_code": obj.get("insurance_code"),
            "employee_code": obj.get("employee_code"),
            "birthdate": obj.get("birthdate"),
            "education_level": PatchedPersonEducationLevel.from_dict(obj["education_level"]) if obj.get("education_level") is not None else None,
            "marital_status": PatchedPersonMaritalStatus.from_dict(obj["marital_status"]) if obj.get("marital_status") is not None else None,
            "number_of_children": obj.get("number_of_children"),
            "military_service": PatchedPersonMilitaryService.from_dict(obj["military_service"]) if obj.get("military_service") is not None else None,
            "exemption_reason": obj.get("exemption_reason"),
            "is_active": obj.get("is_active"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "organization": obj.get("organization")
        })
        return _obj


