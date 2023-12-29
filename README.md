# Instructions:
1. Clone the repository into your local system
2. Download the extension "Run on Save" and enable it.
3. Restart your VS Code.

# Questions:

1. Python Program - Sum of Even Numbers
   - Write a Python function that takes a list of integers as input and returns the sum of all even numbers in the list. (program1.py)

2. C# Program - Factorial Calculator
   - Write a C# program that calculates the factorial of a given positive integer. (program2.cs)

3. JavaScript Program - Palindrome Checker
   - Write a JavaScript function that checks if a given string is a palindrome (reads the same backward as forward). (program3.js)


## Test Script

The test script (`test_program1.py`), (`TestProgram2.cs`), (`test_program3.js`) is designed to check the correctness of your programs. It imports the functions from the respective program files and performs tests using predefined input values.

## Follow these steps to run the test script:

1. For Each program, there are 20 marks.
2. Do not make changes to these files (`test_program1.py`), (`TestProgram2.cs`), (`test_program3.js`).
3. Execute the test script by running the command:

    ```bash
    python test_program1.py
    mstest /testcontainer:TestProgram2.dll
    mocha test_program3.js
    ```

5. Review the test results for each program. If all tests pass, the programs are working correctly.
6. Commit and push your code to the repository so that your test will be submitted.


