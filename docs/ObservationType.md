# ObservationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**sections** | [**List[Section]**](Section.md) |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**var_schema** | **object** |  | [optional] 
**value_type** | [**ObservationTypeValueType**](ObservationTypeValueType.md) |  | [optional] 
**category** | [**ObservationCategory**](ObservationCategory.md) |  | [readonly] 
**unit** | **str** |  | [optional] 
**hint** | **str** |  | [optional] 
**examination_types** | [**List[ExaminationType]**](ExaminationType.md) |  | [readonly] 

## Example

```python
from hseagent_sdk.models.observation_type import ObservationType

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationType from a JSON string
observation_type_instance = ObservationType.from_json(json)
# print the JSON string representation of the object
print(ObservationType.to_json())

# convert the object into a dict
observation_type_dict = observation_type_instance.to_dict()
# create an instance of ObservationType from a dict
observation_type_from_dict = ObservationType.from_dict(observation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


