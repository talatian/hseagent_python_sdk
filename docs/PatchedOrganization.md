# PatchedOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**occupational_clinics** | **List[int]** |  | [optional] 
**hse_specialists** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.patched_organization import PatchedOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedOrganization from a JSON string
patched_organization_instance = PatchedOrganization.from_json(json)
# print the JSON string representation of the object
print(PatchedOrganization.to_json())

# convert the object into a dict
patched_organization_dict = patched_organization_instance.to_dict()
# create an instance of PatchedOrganization from a dict
patched_organization_from_dict = PatchedOrganization.from_dict(patched_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


