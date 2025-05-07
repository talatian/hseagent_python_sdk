# PatchedEmploymentHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**role** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**process** | [**List[Process]**](Process.md) |  | [optional] [readonly] 
**process_ids** | **List[int]** |  | [optional] 
**branch_id** | **int** |  | [optional] 
**branch** | [**Branch**](Branch.md) |  | [optional] [readonly] 
**title** | **str** |  | [optional] [readonly] 
**title_position** | **str** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**organization_address** | **str** |  | [optional] 
**assigned_task** | **str** |  | [optional] 
**employment_date_from** | **date** |  | [optional] 
**employment_date_to** | **date** |  | [optional] 
**reason_for_job_change** | **str** |  | [optional] 
**current** | **bool** |  | [optional] 
**current_organization** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**person** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.patched_employment_history import PatchedEmploymentHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedEmploymentHistory from a JSON string
patched_employment_history_instance = PatchedEmploymentHistory.from_json(json)
# print the JSON string representation of the object
print(PatchedEmploymentHistory.to_json())

# convert the object into a dict
patched_employment_history_dict = patched_employment_history_instance.to_dict()
# create an instance of PatchedEmploymentHistory from a dict
patched_employment_history_from_dict = PatchedEmploymentHistory.from_dict(patched_employment_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


