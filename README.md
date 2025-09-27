# CSE2102-Lab4-Basic-HTTP-with-Python-Flask


To run this system you want to type the command below into the Github's built-in terminal:

python my_server.py

The command above would start the server which its main functionality is to find the given interger factors.
In another terminal, you want to run this command:

curl https://fluffy-space-barnacle-jj4x59w65rg4h5x9w-5000.app.github.dev/

The expected output would be "you called", this would ensure you've runned the server properly.
To use its main functionality you want to add after .dev/
factors/x
where x can be any integer.

If the user runs this command:

curl https://fluffy-space-barnacle-jj4x59w65rg4h5x9w-5000.app.github.dev/factors/12

The expected output will be [1, 2, 2, 3] as these are the factors of 12

If the user types in 7 instead of 12, the expected output will be [7]

To run test_factors.py run this command:

pytest test_factors.py
