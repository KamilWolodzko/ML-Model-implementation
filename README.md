## Solution

### Creating docker
To create the docker image please use 
<br><b > docker build --tag mldev-interview .</b><br>

### Running docker
To run created image use 
<br><b> docker run -i -p 5000:5000 -d mldev-docker </b>

### Running tests
While the docker is running you can test it by below command. 
<br><b>docker exec -it $CONTAINERID python -m pytest tests</b>
