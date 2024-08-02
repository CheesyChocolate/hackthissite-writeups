# Level 4

## Question

This time Sam hardcoded the password into the script. However, the password is
long and complex, and Sam is often forgetful. So he wrote a script that would
email his password to him automatically in case he forgot. Here is the script:

## Explanation

```html
<form action="/missions/basic/4/level4.php" method="post">
    <input type="hidden" name="to" value="sam@hackthissite.org">
    <input type="submit" value="Send password to Sam">
</form>
```

Looking at the source code, we can see that the password is being sent to Sam's
email address. We can intercept the request and change the email address to our
own. We can then submit the form and receive the password.

## Solution

1. Open the source code of the page.

2. Change the email address to your own. (remember the email should be an email
   that is registered in the site)

3. click on the the `Send password to Sam` button.

4. Check your email for the password.


## Answer

```
4cab98e8
```
