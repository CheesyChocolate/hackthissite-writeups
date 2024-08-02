# Level 6

## Question

Network Security Sam has encrypted his password. The encryption system is
publicly available and can be accessed with this form:

You have recovered his encrypted password. It is:

4bciif7m

Decrypt the password and enter it below to advance to the next level.

## Explanation

In this challenge, we are given the encrypted password and the tool that
encrypt a string.

The encryption system can be guessed by trying some strings and comparing the
encrypted result with its original string.

## Solution

1. Enter the string `12345678` in the encryption tool and get the encrypted
   result. It is `13579;=?`.

2. Enter the string `abcdefgh` in the encryption tool and get the encrypted
   result. It is `acegikmo`.

3. We can see that the encryption tool is shifting the first characterd by 0,
   the second characters by 1, the third characters by 2, and so on.

4. Decrypt the password `4bciif7m` by shifting the characters in the reverse
   order. You can do this by hand or write a script to do it.

5. The `solve.py` script can be used to decrypt the password.

## Answer

```
4aafea1f
```
