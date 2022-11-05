# FINAL QA UDACITY PROJECT
## This is a complex project and consist of the folowing:

## BUILD
In this seccion the project will aprovision the infraestructure. This
infraestructure will have:
- A VM 
- A Service App

Obviously this will create a series of resources need for this two resources
be functional, for example, a service plan, network, public ip, custom image,
and more.

## Deploy
For this stage we previously locally had to run the infraestructure and set
in Azure Devops an enviroment. we called it TEST. 
Once de environment is setted we will have two jobs: one for the apps in the
enviroment( VM ) and one for the webapp.
we will deploy the webapp fakerestapy wich is in the automation/jmeter/ folder
and will deploy some test in the environemt: a selenium test and a jmeter test.

## post-deploy
in this stage we are going to run regression and validation test post webapp
deployment to test our webapp aplication.

# RUN AUTOMATECLY

After we set the enviroment and infraestructure locally we can run the pipeline
and it will create the infraestructure, and run the 3 stages automatecly