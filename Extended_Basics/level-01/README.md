# Over and Over?

## Question

You have to give input to a C program which gives you the length of the string.
How would you crash it?

Here is the function:

```c
void blah(char *str)
 {
         char lol[200];
         strcpy(lol, str);
 }
```

## Explanation

This challenge is aimed to familiarize you with buffer overflow attacks. The
`strcpy` function copies the string pointed to by `str` to the buffer `lol`. If
the length of the string pointed to by `str` is greater than 200, the buffer
`lol` will overflow. This can be exploited to overwrite the return address of
the function and crash the program.

We simply can give a string of length greater than 200 to the program to crash
it.

## Solution

1. either use a programming language to generate a string of length greater
   than 200 and pass it to the program, or write a string of length greater
   than 200 manually (text editors like `vim`, `vscode` and even `ms word` can
   track the length of the string). There's also A `solve.py` script that can
   be used to generate a string of length greater than 200.

## Answer

```
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```
