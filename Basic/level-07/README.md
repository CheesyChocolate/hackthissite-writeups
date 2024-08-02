# Level 7

## Question

This time Network Security sam has saved the unencrypted level7 password in an
obscurely named file saved in this very directory.

In other unrelated news, Sam has set up a script that returns the output from
the UNIX cal command. Here is the script:

Enter the year you wish to view and hit 'view'.

## Explanation

The goal is to understand the power of input injection and importance of input
validation. The input field passes whatever is entered to the UNIX command line
without any validation and adds a `cal` command before the input. This allows
us to inject a command to be executed on the server.

The injection commonly done by ending the current command with `;` and then
adding the command to be executed. In this case, we can use `; ls` to list the
files in the current directory.

Then when found the name of the file, we can use the method we learned in the
level 3 to see the content of the file.

## Solution

1. Enter the year `; ls` and hit 'view'.

2. Find the file that can potentially contain the password. Here it is
   `k1kh31b1n55h.php`.

3. Go to URL `https://www.hackthissite.org/missions/basic/7/k1kh31b1n55h.php`
   to see the content of the file.


## Answer

```
b5f5a242
```
