# NestedObservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**observation_type** | [**ObservationType**](ObservationType.md) |  | [readonly] 
**observation_type_id** | **int** |  | 
**value** | **str** |  | 
**note** | **str** |  | [optional] 
**based_on_observation_id** | **int** |  | [optional] 
**based_on_examination_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from hseagent_sdk.models.nested_observation import NestedObservation

# TODO update the JSON string below
json = "{}"
# create an instance of NestedObservation from a JSON string
nested_observation_instance = NestedObservation.from_json(json)
# print the JSON string representation of the object
print(NestedObservation.to_json())

# convert the object into a dict
nested_observation_dict = nested_observation_instance.to_dict()
# create an instance of NestedObservation from a dict
nested_observation_from_dict = NestedObservation.from_dict(nested_observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


