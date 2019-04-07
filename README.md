# Railway_News_System

This project is done for SIH-2019 under Central Ministry where Central Ministry have two problems and their problem statements are
    (a) The work of choosing newspapers for every advertisement to be released is done manually.The rate/circulation of newspaper is checked manually from DAVP website ,whichis laborious and also is prone to error is noting down advertisement rate.
    (b) It is not feasible to monitor the release of news concerning Ministry of Railway-whether positive or negative due to lack of resources/staff. Using digital technology,a system to be devised to inform/give notification in real time or within 12 Hrs.
    
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running
### Install Python

### Linux Users
It is very likely that you already have Python installed out of the box. To check if you have it installed (and which version it is), open a console and type the following command:

```
$ python3 --version
Python 3.6.1
```
### Windows Users
First check whether your computer is running a 32-bit version or a 64-bit version of Windows, on the "System type" line of the System Info page. To reach this page, try one of these methods:

    1)Press the Windows key and Pause/Break key at the same time
    2)Open your Control Panel from the Windows menu, then navigate to System & Security, then System
    3)Press the Windows button, then navigate to Settings > System > About

You can download Python for Windows from the website https://www.python.org/downloads/windows/. Click on the "Latest Python 3 Release - Python x.x.x" link. If your computer is running a 64-bit version of Windows, download the Windows x86-64 executable installer. Otherwise, download the Windows x86 executable installer. After downloading the installer, you should run it (double-click on it) and follow the instructions there.

One thing to watch out for: During the installation, you will notice a window marked "Setup". Make sure you tick the "Add Python 3.6 to PATH" or 'Add Python to your environment variables" checkbox and click on "Install Now".
And repeat
When the installation completes, you may see a dialog box with a link you can follow to learn more about Python or about the version you installed. Close or cancel that dialog -- you'll be learning more in this tutorial!

Note: if you are using an older version of Windows (7, Vista, or any older version) and the Python 3.6.x installer fails with an error, you can try either:

    1)install all Windows Updates and try to install Python again; or
    2)install an older version of Python, e.g., 3.4.6.

If you install an older version of Python, the installation screen may look a bit different than shown above. Make sure you scroll down to see "Add python.exe to Path", then click the button on the left and pick "Will be installed on local hard drive":

### Virtual environment
All you need to do is find a directory in which you want to create the virtualenv; your home directory, for example. On Windows, it might look like C:\Users\Name\ (where Name is the name of your login).

We will make a virtualenv called myvenv. The general command will be in the format:
```
$ python3 -m venv myvenv

```
### Working with virtualenv
The command above will create a directory called myvenv (or whatever name you chose) that contains our virtual environment (basically a bunch of directory and files).

### Working with virtualenv: Windows
Start your virtual environment by running:
```
C:\Users\Name\SIH_TEAM_GULLY_DEVS_R19_MINISTRY OF RAILWAYS_BB4> myvenv\Scripts\activate
```
### Working with virtualenv: Linux and OS X
Start your virtual environment by running:
```
$ source myvenv/bin/activate
```
### Installing Django
Now that you have your virtualenv started, you can install Django.

Before we do that, we should make sure we have the latest version of pip, the software that we use to install Django:
```
(myvenv) ~$ python -m pip install --upgrade pip
```
Now, run pip install -r requirements.txt to install Django.
```
(myvenv) ~$ pip install -r requirements.txt
```
### Migrate Database
```
(myvenv) ~$ python manage.py migrate
```
### Migrations
```
(myvenv) ~$ python manage.py makemigrations
```
### Starting the web server
You need to be in the directory that contains the manage.py file (the djangogirls directory). In the console, we can start the web server by running python manage.py runserver:
```
(myvenv) ~/SIH_TEAM_GULLY_DEVS_R19_MINISTRY OF RAILWAYS_BB4$ python manage.py runserver
```
## Running the tests

Explain how to run the automated tests for this system

[Login Page](https://user-images.githubusercontent.com/29943381/55633462-0cc16a00-57da-11e9-92da-7e17f5f5c692.png)

[](https://user-images.githubusercontent.com/29943381/55633838-d506f200-57da-11e9-918c-111d968fc8d0.png)

![](https://user-images.githubusercontent.com/29943381/55634315-dedd2500-57db-11e9-9b3f-fb0b69f08aa4.png)

![](https://user-images.githubusercontent.com/29943381/55634446-2bc0fb80-57dc-11e9-8448-8070537c41bd.png)

![](https://user-images.githubusercontent.com/29943381/55634597-7478b480-57dc-11e9-994c-e3459bb35b75.png)

![](https://user-images.githubusercontent.com/29943381/55634841-ed780c00-57dc-11e9-901c-07545ff2518b.png)

![](https://user-images.githubusercontent.com/29943381/55635028-5d869200-57dd-11e9-9d27-b4da888fbd4c.png)


## Built With

* [Python](https://www.python.org/) - Programming Language Used
* [Django](https://www.djangoproject.com/) - The Web framework used
* [Dandelion](https://dandelion.eu/) -  Semantic Text Analytics 

## Acknowledgments

* Smart India Hackathon 
* MHRD
* AICTE
