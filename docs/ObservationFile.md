# ObservationFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**file** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from openapi_client.models.observation_file import ObservationFile

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationFile from a JSON string
observation_file_instance = ObservationFile.from_json(json)
# print the JSON string representation of the object
print(ObservationFile.to_json())

# convert the object into a dict
observation_file_dict = observation_file_instance.to_dict()
# create an instance of ObservationFile from a dict
observation_file_from_dict = ObservationFile.from_dict(observation_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


