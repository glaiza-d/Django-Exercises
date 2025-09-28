# Challenges during setup

1. Activating venv

While attempting to activate venv, I encountered the following error:

    *<path file>* cannot be loaded 
    because running scripts is disabled on this system. For more information, see about_Execution_Policies at 
    https:/go.microsoft.com/fwlink/?LinkID=135170.
    At line:1 char:1
    + .\.venv\Scripts\Activate.ps1
    + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        + CategoryInfo          : SecurityError: (:) [], PSSecurityException
        + FullyQualifiedErrorId : UnauthorizedAccess

To resolve the issue, I entered the following command:

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

After that, I was still not able to proceed with the next steps, only to find out that I forgot to run the command again to activate venv. 

2. Unnecessary files committed to repo

While doing the assignment, I accidentally pushed the venv and db.sqlite3 files to the repo. I was not sure to remove it using git so I manually deleted the files from the GitHub page.

After that, I created the .gitignore file and added the list of files that do not need to be included in the repo.

3. Cannot open default Django page on the browser.

When opening the localhost from the browser, it shows an error 404 page. I followed the instructions on the error page to set DEBUG to False in settings.py. After that, I tried running the server again using the command: py manage.py runserver, and then got an error: CommandError: You must set settings.ALLOWED_HOSTS if DEBUG is False. To fix that, I set the ALLOWED_HOSTS in the settings.py file to ["*"].
