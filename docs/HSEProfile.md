# HSEProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**national_code** | **str** |  | 
**organization** | **str** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from hseagent_sdk.models.hse_profile import HSEProfile

# TODO update the JSON string below
json = "{}"
# create an instance of HSEProfile from a JSON string
hse_profile_instance = HSEProfile.from_json(json)
# print the JSON string representation of the object
print(HSEProfile.to_json())

# convert the object into a dict
hse_profile_dict = hse_profile_instance.to_dict()
# create an instance of HSEProfile from a dict
hse_profile_from_dict = HSEProfile.from_dict(hse_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


