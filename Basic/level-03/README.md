# Level 3

## Question

This time Network Security Sam remembered to upload the password file, but
there were deeper problems than that.

## Explanation

Looking at the source code of the page, we see that the password file name is
present in the source code. We can use this information to get the password.

```html
<form action="/missions/basic/3/index.php" method="post">
                     	 <input type="hidden" name="file" value="password.php">
                     	 <input type="password" name="password"><br><br>
                     	 <input type="submit" value="submit"></form>
```

## Solution

1. Open the developer tools in the browser.

2. find the input field either by manually looking at the source code or by
   `pick an element` tool in the developer tools.

3. The password file name is in a `input` tag with `type="hidden"` and
   `name="file"`. The value of the `value` attribute is `password.php`.

4. Visit the URL `https://www.hackthissite.org/missions/basic/3/password.php`
   to get the password.

5. Enter the password in the input field and submit the form.


## Answer

```
f12c1851
```
