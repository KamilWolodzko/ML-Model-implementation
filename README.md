## Solution for ML Dev interview
<br>The repository contains 2 endpoints:</br>
<br>/predict endpoint - to make a prediction using user json data previous_values.</br>
<br>/metrics endpoint to get predictions performance metric.</br>
<br>Whole solution have been written in python 3.9 and using pytest for the tests.</br>
### How to create docker
To create the docker image please use 
<br><b > docker build --tag mldev-interview-docker .</b><br>

### How to run docker
To run created image use 
<br><b> docker run -i -p 5000:5000 -d mldev-interview-docker </b>

### How to run tests
While the docker is running you can test it by below command. 
<br><b>docker exec -it $CONTAINERID python -m pytest tests</b>
