# Python-ATM
ATM Software is an academic project developed in Python scripting language which resembles the existing ATM (Automatic Teller Machine) software.

### 1. How to Run the website
If Python and Django is already installed on your machine skip to step 2

### 2. Install Python and Django
If _Python_ and/or _Django_ is not installed, follow this [link][Python and Django install link].  
This link will show you how to install _Python_ and/or _Django_ on **Mac**, **Windows**, and **Linux** machines.

### 3. Running the Site
After downloading the repository and unzipping, open **terminal** (**command prompt** for Windows) and navigate to the **_../django/pythonatm/_** directory. Once there, run the following command to start the server.
#### Linux/Mac  
```
$ python3 manage.py runserver
```
#### Windows
```
C:\> python3 manage.py runserver
```
If the server runs without error, this message will appear:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 03, 2019 - 00:30:28
Django version 2.2.6, using settings 'pythonatm.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

The above message contains the link (**http://127.0.0.1:8000**) to the homepage of the website.

### 4. Useful links
Below are hyperlinks to different parts of the website that will only work if it is currently running.

[Accounts][accounts page link]&nbsp;&nbsp;&nbsp;-&nbsp;&nbsp;&nbsp;Page that has all the active accounts for every user. \*(Will be removed when project is done)\*

[Admin][admin login page]&nbsp;&nbsp;&nbsp;-&nbsp;&nbsp;&nbsp;Log in page for the Admin(s).

[Personal User Accounts][user accounts page]&nbsp;&nbsp;&nbsp;-&nbsp;&nbsp;&nbsp;Page that will only show the logged-in users account(s). This page is currently only accessible by this link.







[Python and Django install link]: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment
[accounts page link]: http://127.0.0.1:8000/catalog/accounts/
[admin login page]: http://127.0.0.1.8000/admin
[user accounts page]: http://127.0.0.1.8000/catalog/myaccounts
