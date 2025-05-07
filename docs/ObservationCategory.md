# ObservationCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from hseagent_sdk.models.observation_category import ObservationCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationCategory from a JSON string
observation_category_instance = ObservationCategory.from_json(json)
# print the JSON string representation of the object
print(ObservationCategory.to_json())

# convert the object into a dict
observation_category_dict = observation_category_instance.to_dict()
# create an instance of ObservationCategory from a dict
observation_category_from_dict = ObservationCategory.from_dict(observation_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


