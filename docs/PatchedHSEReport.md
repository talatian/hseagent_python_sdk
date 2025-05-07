# PatchedHSEReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**person** | **int** |  | [optional] 
**physician_id** | **int** |  | [optional] 
**physician** | [**Physician**](Physician.md) |  | [optional] [readonly] 
**examinations** | [**List[Examination]**](Examination.md) |  | [optional] [readonly] 
**reason** | **str** |  | [optional] 
**final_opinion** | [**FinalOpinionEnum**](FinalOpinionEnum.md) |  | [optional] 
**recommendations** | **str** |  | [optional] 
**status** | [**HSEReportStatusEnum**](HSEReportStatusEnum.md) |  | [optional] [readonly] 
**report_file** | **str** |  | [optional] [readonly] 
**examination_ids** | **List[int]** |  | [optional] 
**status_fa** | **str** |  | [optional] [readonly] 
**actions** | **List[int]** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.patched_hse_report import PatchedHSEReport

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedHSEReport from a JSON string
patched_hse_report_instance = PatchedHSEReport.from_json(json)
# print the JSON string representation of the object
print(PatchedHSEReport.to_json())

# convert the object into a dict
patched_hse_report_dict = patched_hse_report_instance.to_dict()
# create an instance of PatchedHSEReport from a dict
patched_hse_report_from_dict = PatchedHSEReport.from_dict(patched_hse_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


