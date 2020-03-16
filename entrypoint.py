#!/usr/bin/python

import Algorithmia
import sys
import json
import os

if __name__ == "__main__":
    api_key = os.getenv("INPUT_API_KEY")
    api_address = os.getenv("INPUT_API_ADDRESS")
    algo_name = os.getenv("INPUT_ALGORITHM_NAME")
    algo_hash = os.getenv("INPUT_ALGORITHM_HASH")
    case_data = os.getenv("INPUT_CASES")

    client = Algorithmia.client(api_key=api_key, api_address=api_address)
    cases = json.loads(case_data)

    failures = []
    for case in cases:
        input = case['input']
        expected = case['expected_output']
        name = case['case_name']
        output = client.algo("{}/{}".format(algo_name, algo_hash)).pipe(input)
        print("case: {}".format(name))
        if output == expected:
            print("pass")
        else:
            failure = {"output": output, "expected_output": expected, "case_name": name}
            failures.append(failure)
            print("fail")
    if len(failures) > 0:
        fail_msg = "At least one test case failed:\n"
        for failure in failures:
            fail_msg += "case_name: {}\nexpected_output: {}\nreal_output: {}\n".format(failure['case_name'], failure['expected_output'], failure['output'])
        raise Exception(fail_msg)
    else:
        print("all test cases pass for {}/{}".format(algo_name, algo_hash))


