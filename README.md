# Covid-19 Vaccine Booking

An online web platform for Covid-19 Vaccine Bookings. Developed using Python Django, Django Rest Framework, microservices architecture, and AWS services

<p align="center"> <img align="center" src=https://github.com/dhritix1999/Covid19-Vaccine-Booking/blob/main/screenshots/login.png></p>


## Table of Contents
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Architecture and Deployment](#architecture-and-deployment)


## Features

The Covid-19 Vaccine Booking System is an online web platform that allows patients to book an appointment to receive the Covid-19 vaccine, provided they are eligible. The system is also a comprehensive management portal that allows administrators to manage vaccine centers, their stocks, etc.

<p align="center"> <img align="center" src=https://github.com/dhritix1999/Covid19-Vaccine-Booking/blob/main/screenshots/homepage.png></p>


Here are some key features that the system possesses:

### Make a Booking

Once a patient registers an account with the system, providing their details, they can login and make a booking. Firstly, the system checks whether the patient is eligible to take the Covid-19 vaccine, based on their medical conditions.

<p align="center"> <img align="center" src=https://github.com/dhritix1999/Covid19-Vaccine-Booking/blob/main/screenshots/eligibility.png></p>

If the patient is found to be eligible, the system will generate a list of all vaccine centers with stocks available and will present them to the user, in order of proximity to the patient. The system also prioritizes certain users, based on their industry, and will reserve vaccine centers with depleting stocks for them.

The user can then select a vaccine center, and make a booking.

<p align="center"> <img align="center" src=https://github.com/dhritix1999/Covid19-Vaccine-Booking/blob/main/screenshots/slots.png></p>

A confirmation message is displayed to the user upon successful booking.

### Stock Monitoring

The system is also usable by administrators to ensure proper functioning of the vaccination drive. Specifically, admins are able to manage vaccine centers, by creating new ones, updating their stocks, etc.

<p align="center"> <img align="center" src=https://github.com/dhritix1999/Covid19-Vaccine-Booking/blob/main/screenshots/centers.png></p>

This allows admins to be able to update information about the various vaccination centers easily.

### Priority Management

Similarly, the admins are also able to manage which professions and industries are considered priority for vaccination. This affects the Booking system that patients experience.

<p align="center"> <img align="center" src=https://github.com/dhritix1999/Covid19-Vaccine-Booking/blob/main/screenshots/industry.png></p>

Admins can update the priority status of industries, or create and delete them, using this functionality.

### User Management

The system tracks patients and adminstrators simultaneously. Users are easily able to register accounts with the system, and login accordingly.


## Technologies Used
* [Django](https://www.djangoproject.com/) v3.2.3
* [Django Rest Framework](https://www.django-rest-framework.org/) v3.12.4
* Python 3.8
* HTML 5 / CSS / Javascript / jQuery / Bootstrap
* [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)
* [Amazon RDS](https://aws.amazon.com/rds/)

## Architecture and Deployment

This system was developed using the Microservices architecture. This allows each major functionality to be isolated into its own microservice, and so interfacing with this is performed using uniform REST APIs. Specifically, the following microservices were developed:

* Booking Management
* Profile Management
* Vaccine Center Management

The system was then deployed into the cloud using AWS services. Each microservice was deployed into an Elastic Beanstalk instance, that used Amazon RDS as the database.
