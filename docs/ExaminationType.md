# ExaminationType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**parent** | **str** |  | [readonly] 
**description** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.examination_type import ExaminationType

# TODO update the JSON string below
json = "{}"
# create an instance of ExaminationType from a JSON string
examination_type_instance = ExaminationType.from_json(json)
# print the JSON string representation of the object
print(ExaminationType.to_json())

# convert the object into a dict
examination_type_dict = examination_type_instance.to_dict()
# create an instance of ExaminationType from a dict
examination_type_from_dict = ExaminationType.from_dict(examination_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


