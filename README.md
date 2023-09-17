### User Management System

#### Summary:
This is a sample User Mgmt Application. It has the features to register new users, log in the existing users, and it shows the all users list in the system. This app uses Postgresql as DB.

#### Overview of architecture:
![user_mgmt](https://github.com/dinesh-g0/usermanagement/assets/60867274/bfc4358f-5eec-4a21-aad1-2823be68dd4c)

#### Breakdown of phases of project:

##### Tier-UI
UI is developed using Bootstrap5 and HTML.
##### Login page
<img width="1272" alt="login_page" src="https://github.com/dinesh-g0/usermanagement/assets/60867274/73e4fb5c-ac23-4e56-90d3-048e9f2c2ded">


##### Signup page
<img width="1272" alt="signup_page" src="https://github.com/dinesh-g0/usermanagement/assets/60867274/e2a9da34-f877-44e5-b8bf-cc750c67e08e">


##### Users dashboard page
<img width="1263" alt="users_dashboard" src="https://github.com/dinesh-g0/usermanagement/assets/60867274/5525fe6d-72f1-4536-ba3d-6fe537ab14c8">

#### Tier-Backend
1. In this MVP, this is the first feature of the application, authentication and partitioning the users into groups and giving them granular permissions.
2. The backend uses django framework for starting the server and to interact with the remote Postgresql DB, and for form rendering to show the three UI pages.
#### Tier-Database
Postgresql that is remotely hosted on Heroku
