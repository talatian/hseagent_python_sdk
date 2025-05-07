# EmploymentHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**role** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**process** | [**List[Process]**](Process.md) |  | [readonly] 
**process_ids** | **List[int]** |  | [optional] 
**branch_id** | **int** |  | [optional] 
**branch** | [**Branch**](Branch.md) |  | [readonly] 
**title** | **str** |  | [readonly] 
**title_position** | **str** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**organization_address** | **str** |  | [optional] 
**assigned_task** | **str** |  | [optional] 
**employment_date_from** | **date** |  | 
**employment_date_to** | **date** |  | [optional] 
**reason_for_job_change** | **str** |  | [optional] 
**current** | **bool** |  | [optional] 
**current_organization** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**person** | **int** |  | 

## Example

```python
from openapi_client.models.employment_history import EmploymentHistory

# TODO update the JSON string below
json = "{}"
# create an instance of EmploymentHistory from a JSON string
employment_history_instance = EmploymentHistory.from_json(json)
# print the JSON string representation of the object
print(EmploymentHistory.to_json())

# convert the object into a dict
employment_history_dict = employment_history_instance.to_dict()
# create an instance of EmploymentHistory from a dict
employment_history_from_dict = EmploymentHistory.from_dict(employment_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


