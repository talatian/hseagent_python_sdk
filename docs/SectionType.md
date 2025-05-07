# SectionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from hseagent_sdk.models.section_type import SectionType

# TODO update the JSON string below
json = "{}"
# create an instance of SectionType from a JSON string
section_type_instance = SectionType.from_json(json)
# print the JSON string representation of the object
print(SectionType.to_json())

# convert the object into a dict
section_type_dict = section_type_instance.to_dict()
# create an instance of SectionType from a dict
section_type_from_dict = SectionType.from_dict(section_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


