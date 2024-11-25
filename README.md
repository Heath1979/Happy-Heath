# Happy Heath

![Happy Heath responsive screenshot](documentation/final_views/)

## Introduction

Happy Heath is a blog website showcasing local businesses and the Site Admins experience of them. This website has been developed as part of the Code Institute’s Full-Stack Developer Bootcamp course as my assessed project - focusing on a Django framework, Database manipulation, and CRUD functionality. This project is for educational purposes only.

View live site here : [Happy Heath](https://happy-heath-3daa657fbb51.herokuapp.com/)  
  
For Admin access with relevant sign-in information: [Happy Heath Admin](https://happy-heath-3daa657fbb51.herokuapp.com/admin/login/?next=/admin/)

<hr>

## Table of Contents

- [Happy Heath](#Happy Heath)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
- [UX - User Experience](#ux---user-experience)
  - [Colour Scheme](#colour-scheme)
  - [Font](#font)
- [Project Planning](#project-planning)
  - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
  - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
    - [MoSCoW Prioritization](#moscow-prioritization)
  - [User Stories](#user-stories)
    - [Visitor User Stories](#visitor-user-stories)
  - [Scope Plane](#scope-plane)
  - [Structural Plane](#structural-plane)
  - [Skeleton \& Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
    - [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
    - [Security](#security)
- [Features](#features)
  - [User View - Registered/Unregistered](#user-view---registeredunregistered)
  - [CRUD Functionality](#crud-functionality)
  - [Feature Showcase](#feature-showcase)
  - [Future Features](#future-features)
- [Technologies \& Languages Used](#technologies--languages-used)
  - [Libraries \& Frameworks](#libraries--frameworks)
  - [Tools \& Programs](#tools--programs)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project Setup](#django-project-setup)
  - [Cloudinary API](#cloudinary-api)
  - [Elephant SQL](#elephant-sql)
  - [Heroku deployment](#heroku-deployment)
  - [Clone project](#clone-project)
  - [Fork Project](#fork-project)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
    - [Additional reading/tutorials/books/blogs](#additional-readingtutorialsbooksblogs)
  - [Acknowledgements](#acknowledgements)

## Overview

Happy Heath is a blog site about experiences with local businesses. Users are invited to:

- Join the Happy Heath community
- Create their own profiles
- Interact with reviews through the comments section

Happy Heath is accessible via all browsers with full responsiveness on different screen sizes. Its aim is to create a space where people can read about local businesses and comment on their own experiences. Many small businesses can often only be found through social media business pages and rely on word of mouth to build up business. The aim of the site is to support these businesses and drive customers to them where possible via positive blog posts. Any posts that have a critique of a business should still provide some positivity and hopefully just be to highlight a fixable negative. Happy Heath aims to provide a starting point for people to discuss and promote local businesses. In future developments I would like to invite local businesses the opportunity to promote themselves and add the functionality for users to search for businesses by type.

# UX - User Experience

### Colour Scheme

I aimed for a colour scheme that evoked feelings of warmth and trust. The colour scheme aims to provide an earthy palette in order to create an inviting and natural aesthetic.

![screenshot of colour scheme](documentation/final_views/color-pallette.png)  

### Font

In terms of Font style I opted to stay with the standard Ariel due to its familiarity with users. It is clean and professional and does not detract from other elements of the webpage.
  
# Project Planning  
 
## Strategy Plane

The project goal was to build a simple website showcasing users experiences with local businesses with the option to have a dynamic conversation about the blog posts using the comments section. My intention is to showcase local businesses and the services they offer. A rating system would be added on the idea of the user being a ‘Happy Heath’ or ‘Grumpy Croasdale’. Where possible external links to the businesses would be added in relation to social media and business websites.

### Site Goals

- Create an environment where people could rate and discuss local businesses.
- Easy UI for quick fulfilment of feature CRUD functionalities.
- UX remain the same whether on mobile, tablet or desktop
- Scalable idea, for addition of future features that would allow for business owners to promote themselves.

## Agile Methodologies - Project Management

 Happy Heath is my first project following Agile planning methods. I used my [Github Projects Board](https://github.com/users/Heath1979/projects/4) to plan and document all of my work.

### MoSCoW Prioritization

I chose to follow the MoSCoW Prioritization method for Happy Heath, identifying and labelling my:

- **Must Haves**: the 'required', critical components of the project. Completing my 'Must Haves' helped me to reach the MVP (Minimum Viable Product) for this project early, allowing me to develop the project further than originally planned. 
- **Should Haves**: the components that are valuable to the project but not absolutely 'vital' at the MVP stage. The 'Must Haves' must receive priority over the 'Should Haves'.
- **Could Haves**: these are the features that are a 'bonus' to the project, it would be nice to have them in this phase, but only if the most important issues have been completed first and time allows.
- **Won't Haves**: the features or components that either no longer fit the project's brief or are of very low priority for this release. 

## User Stories

User stories and features recorded and managed on [GitHub Projects](https://github.com/users/Heath1979/projects/4)

### Visitor User Stories

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a **user**, I would like to **view a paginated list of posts** so that I can **select which post I want to view** | **MUST HAVE** |
| As a **site user**, I would like to **click on a post** so that I can **read the full text** | **MUST HAVE** |
| As a **user**, I would like to **check my profile page** so that I can **see my history and amend my details** | **COULD HAVE** |
| As a **site user/admin**, I would like to **view comments on an individual post** so that I can **see feedback on the post** | **SHOULD HAVE** |
| As a **site user**, I would like to **regisger an account** so that I can **comment on a post** | **MUST HAVE** |    
| As a **user**, I would like to **access a blank review/blog template** so that I can **create my own post** | **WONT HAVE** | 
| As a **user**, I would like to **comment on a post** so that I can **interact with the community** | **SHOULD HAVE** | 
| As a **site user**, I would like to **be able to modify or delete a comment on a post** so that I can **make amendments** | **SHOULD HAVE** | 
| As a **user**, I would like to **be able to access external links** so that I can **learn more about the topics in the posts** | **COULD HAVE** | 
| As a **site admin**, I would like to **create, read, update, and delete posts** so that I can **can manage my blog content** | **MUST HAVE** | 
    


