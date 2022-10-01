# Analysis Choosing App service as Web App versus VM service:
First of all let us list the main differences between App service and VM service.

- App Service: it is an http based service, allows the user to host web apps, rest apis, mobile backends,etc.
- VM service: it is a service which provide infrastructure as a service IaaS by given user to create and use virtual machines in the cloud and be responsible for setting up all required dependencies such as OS, updating OS, installing antivirus etc.

### Deployment choice:
I preferred using App service over VM service because I do not need custom VM and OS version to run my application since I need to focus on the main business logic of a CMS backend app. And it will require more time and effort setting up a VM to spin my application such as the need of installing python, git, flask on the VM and manage the network access by exposing apis on specific port which is an extra layer of complexity added on this simple project

### App changes that would change your decision.
Of course there are many factors could affect my decision about choosing App service, one of them if we want to gain higher performance and get control for the underlying infrastructure like installing custom images and software a VM service would be the choice here.