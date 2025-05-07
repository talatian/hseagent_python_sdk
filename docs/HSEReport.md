# HSEReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**person** | **int** |  | 
**physician_id** | **int** |  | [optional] 
**physician** | [**Physician**](Physician.md) |  | [readonly] 
**examinations** | [**List[Examination]**](Examination.md) |  | [readonly] 
**reason** | **str** |  | [optional] 
**final_opinion** | [**FinalOpinionEnum**](FinalOpinionEnum.md) |  | [optional] 
**recommendations** | **str** |  | [optional] 
**status** | [**HSEReportStatusEnum**](HSEReportStatusEnum.md) |  | [readonly] 
**report_file** | **str** |  | [readonly] 
**examination_ids** | **List[int]** |  | 
**status_fa** | **str** |  | [readonly] 
**actions** | **List[int]** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from hseagent_sdk.models.hse_report import HSEReport

# TODO update the JSON string below
json = "{}"
# create an instance of HSEReport from a JSON string
hse_report_instance = HSEReport.from_json(json)
# print the JSON string representation of the object
print(HSEReport.to_json())

# convert the object into a dict
hse_report_dict = hse_report_instance.to_dict()
# create an instance of HSEReport from a dict
hse_report_from_dict = HSEReport.from_dict(hse_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


