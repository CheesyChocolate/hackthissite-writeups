# Extension blocking

## Question

You have this function, provide the value which must be POST-ed as filename to
obtain the desired results:

Get the source code of hackthissite.org/index.php

here is the function:

```php
<?php
        $lvl_text = file_get_contents($_POST['filename'].'.php');
?>
```

## Explanation

This challenge is fairly simple provided you have an understanding of
application structures. It requires us to slightly modify the provided script
in order to access the index.php page at the root of the web application. In
order to do that we need to perform a directory traversal up two directories to
grab the `index.html` page.

### The Function

As you can see from the PHP code above, we have some fairly basic PHP code
that is attempting to get the contents of the filename specified by the value
`filename`. Furthermore, it specifies the type of extension for the filename
which in this case is `.php`. Underneath the code, we have a submission box
where we need to submit the solution to the challenge.

## Solution

Given these points, all we need to do to solve this mission is to tell the
script to navigate up two directories. We are currently in the `extbasic`
directory looking at the file named 2 `/missions/extbasic/2`. So by traversing
up two directories we should be in the root directory. Once there, we need to
specify the `index.php`, however the file extension `.php` has already been
appended for us, so we only need to specify the word index. The correct
solution should be `../../index`. Paste that into the check form, and you
should complete the mission and be able to proceed on to the next one.

## Answer

```
../../index
```

## credits

- [Haxez](https://medium.com/geekculture/hack-this-site-extended-basic-mission-2-1bc91a788c58)
