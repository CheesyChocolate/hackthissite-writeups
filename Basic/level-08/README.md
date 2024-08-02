# Level 8

## Question

Sam remains confident that an obscured password file is still the best idea,
but he screwed up with the calendar program. Sam has saved the unencrypted
password file in `/var/www/hackthissite.org/html/missions/basic/8/`

However, Sam's young daughter Stephanie has just learned to program in PHP.
She's talented for her age, but she knows nothing about security. She recently
learned about saving files, and she wrote a script to demonstrate her ability.

Enter your name:

## Explanation

Same as challenge 7, the goal is to understand the input injection
vulnerability. The difference here is that in previous challenge, we exploited
the UNIX bash shell, but here we will exploit the PHP script.

Here we can make use of type of attack called `payload` to exploit the
vulnerability. The payload is a piece of code that is injected into the
application to exploit the vulnerability.

## Solution

1. first let's test the PHP program by entering a text in the input field.

2. Click on `here` in new page to see the result of program.

3. Looking at the URL, we can see the current URL ends with `.shtml`. This
   means the server is running Apache server and the server is configured to
   parse the PHP code in `.shtml` files. The `.shtml` files are server side
   includes (SSI) files that are used to include the content of one file into
   another file.

4. This suggests that the program is vulnerable to a Server Side Include
   Injection (SSI) attack.

5. We can use the `payload` to exploit the vulnerability. The payload is

```html
<!--#exec cmd="ls /var/www/hackthissite.org/html/missions/basic/8/" -->
```

- `<!--` and `-->` is the start of HTML comment.
- `#exec` is the SSI command to execute the command.
- `cmd` is the parameter to the `#exec` command.
- `ls /var/www/hackthissite.org/html/missions/basic/8/` is the command to list
  the files in the directory.

6. Enter the payload in the input field and click on `here` to see the result.

7. Well, you see an easteregg. The solution is still correct, but not what what
   the owner of the site was expecting.

8. let's modify the payload to what that owner was probably expecting.

```html
<!--#exec cmd="ls ../" -->
```

- `ls ../` is the command to list the files in the parent directory.

9. Enter the payload in the input field and click on `here` to see the result.

10. We can see `au12ha39vc.php` file in the list. This is the password file
    that we are looking for.

11. We use the method we learned in challenge 3 to read the content of the file
    by entering the following URL in the browser.

```html
https://www.hackthissite.org/missions/basic/8/au12ha39vc.php
```

## Answer

```
571194b9
```
