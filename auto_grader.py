import sys
import json
import pytest

tests = []


class MyPlugin:
    def pytest_itemcollected(self, item):
        print(item.nodeid)
        tests.append(item.nodeid)


if __name__ == "__main__":
    return_code = pytest.main([], plugins=[MyPlugin()])

    assignments = list(map(lambda x: {
        "name": x.split('/')[2],
        "setup": "sudo -H pip3 install pytest",
        "run": "pytest -x " + x,
        "input": "",
        "output": "",
        "comparison": "included",
        "timeout": 10,
        "points": 1
    }, tests))
    assignments = {"tests": assignments}
    # print(assignments)
    json_string = json.dumps(assignments)
    with open('autograding.json', 'w') as outfile:
        outfile.write(json_string)
    sys.exit(return_code)