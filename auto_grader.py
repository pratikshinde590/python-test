import sys
import json
import pytest
import os

tests = []

class MyPlugin:
    def pytest_itemcollected(self, item):
        print(item.nodeid)
        tests.append(item.nodeid)

def extract_dependencies_from_settings_json(settings_path):
    # Extract dependencies from the settings.json file
    # As there is no explicit information about dependencies in the provided settings.json,
    # you may consider prompting users to include a requirements.txt file in each assignment directory.
    # Modify this function based on your actual requirements.
    return []

if __name__ == "__main__":
    # Run pytest with a custom plugin (MyPlugin) to collect test information
    return_code = pytest.main([], plugins=[MyPlugin()])

    # Create a list of test assignments based on the collected test information
    assignments = []
    for test_id, test_name in enumerate(tests, start=1):
        problem_name = f"program{test_id}.py"
        test_checker_name = f"test{test_id}.py"

        # Assuming that the template repository is cloned into a directory named 'template_repo'
        template_repo_path = 'template_repo'
        problem_path = os.path.join(template_repo_path, problem_name)
        test_checker_path = os.path.join(template_repo_path, test_checker_name)

        # Extract dependencies from the settings.json file
        settings_json_path = os.path.join(template_repo_path, '.vscode', 'settings.json')
        dependencies = extract_dependencies_from_settings_json(settings_json_path)

        assignment = {
            "name": f"Assignment {test_id}",
            "setup": f"pip install {' '.join(dependencies)}",
            "run": f"pytest -x {problem_path} -k {test_checker_name}",
            "input": "",
            "output": "",
            "comparison": "included",
            "timeout": 10,
            "points": 1
        }
        assignments.append(assignment)

    assignments = {"tests": assignments}

    # Serialize the assignment information to JSON
    json_string = json.dumps(assignments)

    # Write the JSON to autograding.json
    with open('autograding.json', 'w') as outfile:
        outfile.write(json_string)

    # Exit with the return code from pytest
    sys.exit(return_code)
