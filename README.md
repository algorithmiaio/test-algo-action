# test-algo github action
A github action designed to test an algorithm on www.algorithmia.com, with a given input/expected output.


# Action Input

```
inputs:
  regular_api_key:
    description: 'your typical Algorithmia API key'
    required: true
  api_address:
    description: 'The API address for the Algorithmia Cluster you wish to connect to'
    required: false
    default: 'https://api.algorithmia.com'
  algorithm_name:
    description: 'The name of the Algorithm you want to test'
    required: true
  cases:
    description: 'A list of Json Case objects that describe the desired test cases'
    required: True
```

```
  regular_api_key - (required) - An Algorithmia api key that has execute access for the algorithm you wish to test, read more about that [here](https://algorithmia.com/developers/platform/customizing-api-keys)
  api_address - (optional) - The Algorithmia API cluster address you wish to connect to, if using a private cluster; please provide the correct path to your environment.
  algorithm_name - (required) - The algorithmia algorithm name for project you're testing. This algorithm name must refer to the github repository you attach this action to in order to work properly.
  cases - (required) - a stringified json list containing test cases to try your algorithm with, if any of the test cases fails - this action will return with an exception indicating which case failed.
```


# Case Schema
Your test cases should follow the following json schema
```
[
 { 
    "case_name": String,
    "input": Any,
    "expected_output": Any
  },
  ...
]
```

`input` and `expected_output` will be expected to be the raw input/output that the algorithm you're testing should expect.

# Example
```
name: Algorithmia test-algo

on:
  commit

jobs:
  test-algo:

    runs-on: ubuntu-latest
    - name: Algorithmia test-algo
      uses: algorithmiaio/test-algo-action@v0.1.0-rc4
      id: build-wait-step
      with:
        regular_api_key: {{ secrets.ALGORITHMIA_API_KEY }}
        api_address: {{ secrets.ALGORITHMIA_API_ADDRESS }}
        algorithm_name: your_username/your_algorithm
        cases: '[{"case_name":"hello test", "input":"test", "expected_output":"hello test"}]
```