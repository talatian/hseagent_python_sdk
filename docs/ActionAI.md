# ActionAI


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
**status** | [**ActionAIStatusEnum**](ActionAIStatusEnum.md) |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**target_observation** | **str** |  | [readonly] 
**target_examination** | **str** |  | [readonly] 

## Example

```python
from openapi_client.models.action_ai import ActionAI

# TODO update the JSON string below
json = "{}"
# create an instance of ActionAI from a JSON string
action_ai_instance = ActionAI.from_json(json)
# print the JSON string representation of the object
print(ActionAI.to_json())

# convert the object into a dict
action_ai_dict = action_ai_instance.to_dict()
# create an instance of ActionAI from a dict
action_ai_from_dict = ActionAI.from_dict(action_ai_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


