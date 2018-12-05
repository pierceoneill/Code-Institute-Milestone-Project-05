![Build Status](https://travis-ci.org/pierceoneill/Code-Institute-Milestone-Project-05.svg?branch=master)](https://travis-ci.org/pierceoneill/Code-Institute-Milestone-Project-05)
# Code Institute - Stream 3 Project 
### By Pierce O'Neill

## Deployment
- https://ci-milestone-05-minderfiner.herokuapp.com/

## About this project

I am currently a student at the Code Institute doing a Full Stack Diploma in Software Development. This is the third of three projects which I must complete in order to be awarded the globally recognised Diploma from Edinburgh Napier University. This project will cover the Full Stack i.e all sections of the course both frontend and backend web development.

Having consulted with my mentor Chris Zielinski, I decided to build a babysitter app where parents or guardians could search and book a babysitter or childcare for their children. The babysitters apply to be registered on the site. 

## The needs this project fulfils

- This is a business website. It is built for a client running babysitter / childcare agency The website is needed for e-commerce so that potential parents / guardians can browse and search before eventually booking a childminder for their children that suits their location ,needs and requirements.

## UX

The UX is made with simplicity in mind, it's meant to be easy to navigate and simple information with icons to process.

### The Client Dashboard

- The Dashboard is the main area for the clients to edit their information and and information on their children. Simple buttons that provide the user with a modal for editing their own personal information and also 
adding children to their profiles.

- The Client must register firstly to be able to post their information. The register and login forms can be accessed by clicking on the relevant button on the navbar.

### The Babysitters List

- The Babysitters list displays the basic information for each of the babysitters who are available with a small profile picture along with their name and a short description. Their price per hour is also displayed.

-  There is a search table at the top which leads to the search results page once selected.

### The Babysitters Profile

-  The babysitter profile page displays details information on each babysitter from personal details, qualifications, work experience and childcare references.

- The babysitter booking process can be started from here by selecting the quantity of hours required which adds to the cart.
- 
### The Blog
This is a simple Django blog with some saple posts regarding childcare and childcare information. The users can post comments which have to be approved or deleted byt he ADMIN and only the admin can post a new story to the blog.


### About

- The About Page gives a brief rundown of how the site works for both babysitters and the potential clients. There is a testimonial slider at the top and also some sample payment rates at the bottom with a link to the babysitters main page to encourage a booking.

### Contact

- The contact page contains a google map container highlighting the location of the business. There is also an email contact form which is working using emailjs. For those who have a special requirement outside of the standard bookings or any enquiry, they can use this form.


## Technologies used:

### Cloud9   
- cloud based IDE to create the project
#####  Heroku 
- to deploy the project
#### AWS - Amazon Web Services
- AWS S3 - to store static and media files and to serve the website
- AWS IAM - manages user access and encryption keys

####  Travis CI 
- Used to build and test the project
#### HTML
 - hypertext markup language
#### CSS 
- cascading style sheets 
#### Javascript 
- client side scripting language
#### Python 
- Programming Language
#### GitHub 
-for version control and backup of code
#### Bootstrap 
- A framework for developing responsive, mobile first websites.
#### Django 
- python web framework
#### Libraries and packages 

- django forms bootstrap library for styling of forms
- pillow needed for using images
- ckeditor for rich text editing in creating and editing posts
- dj-database-url to allow connection to database url
- psycopg2 to allow connection to postgress database
- django storages and botoS3- both needed to use django with S3
- gunicorn - to connect to heroku


#### Stripe 
- needed for online payment transactions for purchasing products
#### EmailJs 
- needed for the contact forms
#### Gmail 
- needed for emails

## Testing

- I have outlined my testing in a seperate file  [testing.md - click here to view it](https://github.com/sarahbarron/Stream-3-Project/blob/master/testing.md)

## Deployment

- Set up an [heroku app](https://dashboard.heroku.com/apps)
- Added on the Heroku Postgress Database
- Installed the package dj-database-url to allow connection to a database url
- Installed the package psycopg2 for connecting to postgress databases
- Setup the default database in settings.py to the postgres database
- Migrated the project in order to use the new postgres datatbase
- Created a superuser
- Set up a AWS S3 bucket to serve the website
- Set up an AWS IAM - to manage user access and encrytion 
   - Setup a group 
   - Created a policy
   - Attached the group to the policy
   - Created a user
   - Downloaded the users keys .csv file
- Installed django-storages  and botoS3 in order to use dajango with S3
- Setup Django to connect with AWS
- Setup Travis CI to build and test the project
- Setup my config variables in Heroku
- Installed the package gunicorn to connect my project to Heroku. 
- Disabled collectstatic in heroku so heroku wont try to upload the static files.
- Deployed the project on heroku
- Added the heroku address to valid hosts in settings.py
- Changed Debug to false and added 403.html, 404.html and 505.html files to the root templates folder.

## Problems encountered throughout the project

- I committed my env.py which held my private development envrionment variables to GitHub. To solve the problem i deleted the env.py file from all my previous Git Commits and added the the env.py file to .gitignore for all future commits. 

- I has issues connecting education, work experience and references to each babysitter. I got around this i created 3 querysets for each of the sections.
```
def babysitter_profile(request, id):
    """A view that displays the profile page of a registered babysitter"""
    babysitter = get_object_or_404(Babysitter, id=id)
    reference_qs = Reference.objects.filter(babysitter_id=babysitter.id)
    education_qs = Education.objects.filter(babysitter_id=babysitter.id)
    return render(request, "babysitter_profile.html", {
        'babysitter': babysitter,
        'education_qs': education_qs,
        'reference_qs': reference_qs}
    )
```
- I also had an issue with displaying order history on the clients profile page and this is still work in progress.

## References

- [Django Documentation](https://docs.djangoproject.com/en/2.0/) helped me with all backend aspects of my project. 
- [Stripe Documentation](https://stripe.com/docs) - helped me with my stripe payments and testing
- [Stack Overflow](https://stackoverflow.com) helped me with some of the logic dealing with multiple models



## Thank You

I would like to thank the [Code Institute](https://www.codeinstitute.net/) and [Springboard](https://springboardcourses.ie/) for providing me with such a wonderful course and experience.  It has been a rewarding experience and I feel like I have really learned new skills that I can use going forward. I would like to thank my mentor Chris Zielinski and also my fellow students on slack. I would also like to thank the institute for the Halloween Hackathon which was not only fun but a great learning experience.