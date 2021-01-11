# Tornado-Server-Skeleton
This repository contains Codebase of a Backend Server created using Tornado framework. This is just a skeleton on top of which actual server can be created.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
Pip
Python
Tornado
Docker
Docker-Compose
```

### Installing

Follow these steps to installing  dependencies and running this project on your local
by setting development environment:

- Clone project on local machine

```
 git clone https://github.com/sy117/Tornado-Server-Skeleton.git
```


Run application inside container using docker

```
 sudo docker-compose up

```


## Deployment

Before deployment create image for production by following these steps:-

 - Move to dummy_server directory
  ```
  cd dummy_server/
  ```
 - Change Entrypoint in Dockefile for production environment
    - Comment this line
    ```
    CMD [ "python", "main.py" ]
    ```
    - Uncomment this line
    ```
    CMD [ "python", "main.py", "--prod=True" ]
    ```
Steps to Create image manually:
 - Go to dummy_server directory
    ```
    cd dummy_server/
    ```
 - Create image using below command
    ```
    sudo docker build -t <ImageName>:<ImageTag> .
    ```
 - Push this Image to any Container Registry(DockerHub, GCR)
 
## Built With

* [Torndo](https://www.tornadoweb.org/en/stable/) - The web framework used
* [Docker](https://www.docker.com/) - Docker
