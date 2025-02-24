# Dusk Core
This library is meant to be the central location for all the libraries used to build and interact with the Confluence structure. 

## Services
This is where all the basic logic that is used for all microservices is written. 

### Routes
These the are the default routes that all APIs need in order to function. They handle situations such as managing key rotation.

### Middleware
Middleware is the section in which middleware for all apps is written. It is meant to be used in conjunction with FastAPI, Dusk's API framework of choice.

## Security
This section handles cryptography and other important security features imbedded in APIs running within a microservice architecture.