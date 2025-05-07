# Examination


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

## Example

```python
from hseagent_sdk.models.examination import Examination

# TODO update the JSON string below
json = "{}"
# create an instance of Examination from a JSON string
examination_instance = Examination.from_json(json)
# print the JSON string representation of the object
print(Examination.to_json())

# convert the object into a dict
examination_dict = examination_instance.to_dict()
# create an instance of Examination from a dict
examination_from_dict = Examination.from_dict(examination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


