# P2Wildcats

# Project Overview
Our idea is a website that teaches you about animals, specifically wildcats and their lifestyle with cool facts. 
- We were inspired by this idea because of our group name given on the first day of the trimester by Mr. Mortensen!
- We have created multiple pages for the project. These pages are accessible through the menu on the top of the site.
- Home page contains links for project plan and journal.
- Catalog page contains information and a button that randomizes pictures of cats.
- About page contains information about everyone in the group.
- Added a login system to keep track of everybody's account and will guide you through the website.

# Applications/Installations Needed and How to Create Code and Publish it
- Install IntelliJ IDEA [Download](https://www.jetbrains.com/idea/)
- Install Python [Download](https://www.python.org/downloads/release/python-390/)
- Install Git [Download](https://git-scm.com/downloads) </li>
- Open up IntelliJ and on the 'Configure' screen install python plug-ins after searching them up
- Go back to the main screen, go to 'Get Version Control' and input the url for the Git repository
- Now you should be able to push and pull code to and from Git

# How To Run 
- Clone this repository into IntelliJ or your IDE of choice by copying the HTTPS link.
- When opend, install packages > project > project structure > SDK's > packages > +
    - Flask, flask-bootstrap, flask-wtf, wtforms, flask-sqlalchemy, werkzeug, flask-login, email validator
- Open the project, and run the "views.py" file, which contains imports.
- A link should appear at the bottom of 'python terminal', click the link to receive access to site.

# Login System
- Login is not needed to navigate through website, but is required to keep track of your progress.
- Create an account with a username and password of your choice and click the box to remember the info. 
- Account info. is stored in database.

# Big Ticket Items 
Login System: This login system is a database that will store your account information and keep track of your learning/progress on the website.
Navigation Bar: This will have a page for the animals to learn about them as well as an about us page and embedded videos.
Wildcat Randomization Database: The catalog page will have a randomizer where you click the button and it displays a random wildcat from our database including some info. 

# Scrum Project Board
https://github.com/andrewc26/P2Wildcats/projects/1

The project Board keeps log of what is in progress, what has been asigned, and what has been completed and ready to push to github or onto rasberry pi. 
It helps keep track of whos job it is for certian tasks in order to make sure all group is working and getting the job done by the deadline.

# Project Plan
https://docs.google.com/document/d/1SOJ9NIcBcs_JgxbmhQpfNp5UvPgIRAXqdzKQGvdFSLw/edit#
The project plan is where our group brainstorms and plans out ideas to improve or add to our project.

# Journals 
Andrew and Travis Journal Link:
https://docs.google.com/document/d/1Rn2xLqRm99J29nrHp6zhihUfQyBIgqrA3u0H1DxFc5c/edit

Anthony and Nick Journal Link:
https://docs.google.com/document/d/1H_rkU8QGBcCwCwj6Ia5sylhfVicfE1cv6_J8-KukuZM/edit

The journals are used to keep track of what is completed or worked on each week as well as our comments/grades for each other.

# 4 Card/Ticket Review Items
Scrum Board:
- Anthony Ticket: Deployment/Uploading Site to Pi - http://70.95.177.55:8080/
- Travis Ticket: About Page & Home Page - Look above in "How To Run" for help to find code
https://github.com/andrewc26/P2Wildcats/blob/main/templates/about.html
- Nick Ticket: Dashboard progress and updating - Look above in "How To Run" for help to find code
https://github.com/andrewc26/P2Wildcats/blob/main/templates/dashboard.html
- Andrew Ticket: Catalog progress and updating - Look above in "How To Run" for help to find code
https://github.com/andrewc26/P2Wildcats/blob/main/templates/catalog.html
- Anthony scrum master score: 19/20
- Travis scrum master score: 19/20
- Nick scrum master score: 17/20
- Andrew scrum master score: 19/20
- SCRUM BOARD:
https://github.com/andrewc26/P2Wildcats/projects/1?fullscreen=true

# Easter Egg 
The easter egg in our project is a secret link that takes you to a hidden page on our website. On that page we have embedded links to different websites where you can take quizzes to see what wildcat you are most like.
- https://github.com/andrewc26/P2Wildcats/blob/main/templates/easternav.html
- https://github.com/andrewc26/P2Wildcats/blob/main/templates/easter.html
- http://127.0.0.1:5000/easter

# Tickets and Easter Egg Completion
https://github.com/andrewc26/P2Wildcats/projects/1
- Nick Ticket: Work on persistent data and fix log in system 
https://github.com/andrewc26/P2Wildcats/blob/main/templates/login.html
- Travis Ticket: Easter egg creation and Easter egg page progress
https://github.com/andrewc26/P2Wildcats/blob/main/templates/easternav.html
https://github.com/andrewc26/P2Wildcats/blob/main/templates/easter.html
- Andrew Ticket: Nav bar for Easter Egg with embedded links to wildcat quizzes and metadata through api
https://github.com/andrewc26/P2Wildcats/blob/main/templates/catalog.html
https://github.com/andrewc26/P2Wildcats/blob/main/templates/easternav.html
https://github.com/andrewc26/P2Wildcats/blob/main/templates/easter.html
- Anthony Ticket: helped fix log in system and layout/style of the Easter egg page 
https://github.com/andrewc26/P2Wildcats/blob/main/templates/login.html
https://github.com/andrewc26/P2Wildcats/blob/main/templates/easter.html
