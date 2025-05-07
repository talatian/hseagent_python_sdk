# Action


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**action_type** | [**ObservationType**](ObservationType.md) |  | [readonly] 
**person** | **int** |  | [optional] 
**based_on_examination** | [**Examination**](Examination.md) |  | [readonly] 
**based_on_report** | [**HSEReport**](HSEReport.md) |  | [readonly] 
**data** | **object** |  | [optional] 
**result** | **str** |  | [readonly] 
**based_on_examination_id** | **int** |  | [optional] 
**based_on_report_id** | **int** |  | [optional] 
**status** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from hseagent_sdk.models.action import Action

# TODO update the JSON string below
json = "{}"
# create an instance of Action from a JSON string
action_instance = Action.from_json(json)
# print the JSON string representation of the object
print(Action.to_json())

# convert the object into a dict
action_dict = action_instance.to_dict()
# create an instance of Action from a dict
action_from_dict = Action.from_dict(action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


