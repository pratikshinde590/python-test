# Instructions:
1. Clone the repository into your local system
2. Download the extension "Run on Save" and enable it.
3. Restart your VS Code.

# Questions:

1. We distribute some number of candies, to a row of n = num_people people in the following way:
We then give 1 candy to the first person, 2 candies to the second person, and so on until we give n candies to the last person.
Then, we go back to the start of the row, giving n + 1 candies to the first person, n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.
This process repeats (with us giving one more candy each time, and moving to the start of the row after we reach the end) until we run out of candies.  The last person will receive all of our remaining candies (not necessarily one more than the previous gift).
Return an array (of length num_people and sum candies) that represents the final distribution of candies.
 
Example 1:


Input: candies = 7, num_people = 4Output: [1,2,3,1]Explanation:On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
Example 2:


Input: candies = 10, num_people = 3Output: [5,2,3]Explanation: On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
 
Constraints:
1 <= candies <= 10^9
1 <= num_people <= 1000





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


