# HazardEvaluation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**observations** | [**List[NestedObservation]**](NestedObservation.md) |  | 
**examination_type** | [**ExaminationType**](ExaminationType.md) |  | [readonly] 
**examination_type_id** | **int** |  | 
**person_id** | **int** |  | 
**physician_id** | **int** |  | [optional] 
**physician** | [**Physician**](Physician.md) |  | [readonly] 
**note** | **str** |  | [optional] 
**interpretation** | [**ExaminationInterpretation**](ExaminationInterpretation.md) |  | [optional] 
**performed_at** | **date** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**actions** | **List[int]** |  | [readonly] 
**hse_specialist** | **str** |  | [readonly] 
**employment_history_id** | **int** |  | 
**employment_history** | **str** |  | [readonly] 

## Example

```python
from hseagent_sdk.models.hazard_evaluation import HazardEvaluation

# TODO update the JSON string below
json = "{}"
# create an instance of HazardEvaluation from a JSON string
hazard_evaluation_instance = HazardEvaluation.from_json(json)
# print the JSON string representation of the object
print(HazardEvaluation.to_json())

# convert the object into a dict
hazard_evaluation_dict = hazard_evaluation_instance.to_dict()
# create an instance of HazardEvaluation from a dict
hazard_evaluation_from_dict = HazardEvaluation.from_dict(hazard_evaluation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


