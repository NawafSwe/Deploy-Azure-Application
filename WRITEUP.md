# Analysis Choosing App service as Web App versus VM service:
First of all let us list the main differences between App service and VM service.

- App Service: it is an http based service, allows the user to host web apps, rest apis, mobile backends,etc.
- VM service: it is a service which provide infrastructure as a service IaaS by given user to create and use virtual machines in the cloud and be responsible for setting up all required dependencies such as OS, updating OS, installing antivirus etc.

# Comparison between Azure VM vs Azure App service:
- Cost wise: Azure VM has the plan of pay-as-you-go unlike App service you will pay based on the plan even if you are not fully utilizing it and we need to note that Azure VMs are more expensive to run in comparison to Azure App Service.
- Portability wise: Azure App service have certain choices of the programming languages set such as Python, Nodejs, dot net, Java, and PHP. As you can see you are restricted by theses choices if you are planning to use Azure App service, however an Azure VM service can play the game here where you can set up the VM with language's environment you need here.
- Flexibility wise: Azure VM are more flexible where you have the access to the server and the underlying OS unlike Azure App service.
### Deployment choice:
I preferred using App service over VM service because I do not need custom VM and OS version to run my application since I need to focus on the main business logic of a CMS backend app. And it will require more time and effort setting up a VM to spin my application such as the need of installing python, git, flask on the VM and manage the network access by exposing apis on specific port which is an extra layer of complexity added on this simple project

### App changes that would change your decision.
Of course there are many factors could affect my decision about choosing App service, one of them if we want to gain higher performance and get control for the underlying infrastructure like installing custom images and software a VM service would be the choice here.