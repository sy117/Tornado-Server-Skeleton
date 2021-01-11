# set base image (host OS)
FROM python:3.7-slim

# set the working directory in the container
WORKDIR /code

# copy the content of the local src directory to the working directory
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# expose port
EXPOSE 8080

# command to run on container start

# for dev environment
CMD [ "python", "main.py" ]

# for prod environment
# CMD [ "python", "main.py", "--prod=True" ]
