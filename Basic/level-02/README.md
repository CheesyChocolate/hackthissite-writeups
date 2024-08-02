# Level 2

## Question

Network Security Sam set up a password protection script. He made it load the
real password from an unencrypted text file and compare it to the password the
user enters. However, he neglected to upload the password file...

## Explanation

Since the password file does not exist, the script will not be able to load the
password. This cusses the password check script to check the input against an
empty string. This means that the password check will pass only when the input
is an empty string.

## Solution

1. Don't enter anything, just press enter.

## Answer

```

```
