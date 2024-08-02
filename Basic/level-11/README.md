# Level 11

## Question

Sam decided to make a music site. Unfortunately he does not understand Apache.
This mission is a bit harder than the other basics. I love my music! "Sad Songs
(Say So Much)" is the best !

## Explanation

This challenge is aimed to test the understanding of the Apache web server
directory listing and configuration.

The user is landed on the page
`https://www.hackthissite.org/missions/basic/11/` which shows a message and is
not the usual page with a form to submit the answer. We can change the URL to
check the submit form page. Also since the directory listing is enabled, we can
check for the files in the directory.

You also need to know that the Apache web server has a configuration file
`.htaccess` that can be used to configure the server. One of the configurations
is to hide certain files or directories from the directory listing. But if the
name of the file or directory is known, it can be accessed directly. If you
can access the `.htaccess` file, you can find the hidden files or directory
names, and access them directly.

## Solution

1. Open the URL `https://www.hackthissite.org/missions/basic/11/index.php` to
   get the form to submit the answer. Keep this page open.

2. In a new tab, let's try to find a directory that exists under the current
   directory. Open the URL
   `https://www.hackthissite.org/missions/basic/11/` and try adding `/a`, `/b`,
   `/c`, etc. to the URL to find a directory that exists.

**Note:** There are tools that let you automatically search for all the open
access directories in a website. But for this challenge, we can manually check
the directories.

3. We find that the directory
   `https://www.hackthissite.org/missions/basic/11/e/` exists and has a file.
   Follow the files this you reach the end with the URL
   `https://www.hackthissite.org/missions/basic/11/e/l/t/o/n/`.

4. Now, let's try to find the `.htaccess` file. Open the URL
   `https://www.hackthissite.org/missions/basic/11/e/l/t/o/n/.htaccess` and you
   will find the file.

```apache
IndexIgnore DaAnswer.* .htaccess
<Files .htaccess>
require all granted
</Files>
```

5. We can see the file `DaAnswer` is hidden. Open the URL
   `https://www.hackthissite.org/missions/basic/11/e/l/t/o/n/DaAnswer` to get
   the answer.

6. We will see the sentence `The answer is close! Just look a little harder.`.
   (Note: The sentence may be different for you.)

7. Go to `https://www.hackthissite.org/missions/basic/11/index.php` and submit
   the text `close` to complete the challenge.

## Answer

```
close
```
