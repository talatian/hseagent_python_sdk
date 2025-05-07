# PatchedHazardEvaluation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**observations** | [**List[NestedObservation]**](NestedObservation.md) |  | [optional] 
**examination_type** | [**ExaminationType**](ExaminationType.md) |  | [optional] [readonly] 
**examination_type_id** | **int** |  | [optional] 
**person_id** | **int** |  | [optional] 
**physician_id** | **int** |  | [optional] 
**physician** | [**Physician**](Physician.md) |  | [optional] [readonly] 
**note** | **str** |  | [optional] 
**interpretation** | [**ExaminationInterpretation**](ExaminationInterpretation.md) |  | [optional] 
**performed_at** | **date** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**actions** | **List[int]** |  | [optional] [readonly] 
**hse_specialist** | **str** |  | [optional] [readonly] 
**employment_history_id** | **int** |  | [optional] 
**employment_history** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.patched_hazard_evaluation import PatchedHazardEvaluation

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedHazardEvaluation from a JSON string
patched_hazard_evaluation_instance = PatchedHazardEvaluation.from_json(json)
# print the JSON string representation of the object
print(PatchedHazardEvaluation.to_json())

# convert the object into a dict
patched_hazard_evaluation_dict = patched_hazard_evaluation_instance.to_dict()
# create an instance of PatchedHazardEvaluation from a dict
patched_hazard_evaluation_from_dict = PatchedHazardEvaluation.from_dict(patched_hazard_evaluation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


