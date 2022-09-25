# specifies python image
FROM python:3.9

# creates directory inside the container
RUN apt-get update
WORKDIR /user/src/app

# copy requirements.txt and run pip install in order to install the packages into container at the directory defined above
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt --user
COPY . .

# enter entry point parameters executing the container
ENTRYPOINT ["python", "./app.py"]

# exposing the port to match the port in the runserver.py file
EXPOSE 5000