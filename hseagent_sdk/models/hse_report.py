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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from hseagent_sdk.models.examination import Examination
from hseagent_sdk.models.final_opinion_enum import FinalOpinionEnum
from hseagent_sdk.models.hse_report_status_enum import HSEReportStatusEnum
from hseagent_sdk.models.physician import Physician
from typing import Optional, Set
from typing_extensions import Self

class HSEReport(BaseModel):
    """
    HSEReport
    """ # noqa: E501
    id: StrictInt
    person: StrictInt
    physician_id: Optional[StrictInt] = None
    physician: Physician
    examinations: List[Examination]
    reason: Optional[StrictStr] = None
    final_opinion: Optional[FinalOpinionEnum] = None
    recommendations: Optional[StrictStr] = None
    status: HSEReportStatusEnum
    report_file: StrictStr
    examination_ids: List[StrictInt]
    status_fa: StrictStr
    actions: List[StrictInt]
    created_at: datetime
    updated_at: datetime
    __properties: ClassVar[List[str]] = ["id", "person", "physician_id", "physician", "examinations", "reason", "final_opinion", "recommendations", "status", "report_file", "examination_ids", "status_fa", "actions", "created_at", "updated_at"]

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
        """Create an instance of HSEReport from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "physician",
            "examinations",
            "status",
            "report_file",
            "status_fa",
            "actions",
            "created_at",
            "updated_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of physician
        if self.physician:
            _dict['physician'] = self.physician.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in examinations (list)
        _items = []
        if self.examinations:
            for _item_examinations in self.examinations:
                if _item_examinations:
                    _items.append(_item_examinations.to_dict())
            _dict['examinations'] = _items
        # set to None if reason (nullable) is None
        # and model_fields_set contains the field
        if self.reason is None and "reason" in self.model_fields_set:
            _dict['reason'] = None

        # set to None if recommendations (nullable) is None
        # and model_fields_set contains the field
        if self.recommendations is None and "recommendations" in self.model_fields_set:
            _dict['recommendations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HSEReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "person": obj.get("person"),
            "physician_id": obj.get("physician_id"),
            "physician": Physician.from_dict(obj["physician"]) if obj.get("physician") is not None else None,
            "examinations": [Examination.from_dict(_item) for _item in obj["examinations"]] if obj.get("examinations") is not None else None,
            "reason": obj.get("reason"),
            "final_opinion": obj.get("final_opinion"),
            "recommendations": obj.get("recommendations"),
            "status": obj.get("status"),
            "report_file": obj.get("report_file"),
            "examination_ids": obj.get("examination_ids"),
            "status_fa": obj.get("status_fa"),
            "actions": obj.get("actions"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


