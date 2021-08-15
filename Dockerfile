FROM centos:latest
WORKDIR /ws
RUN yum install python3 -y
RUN pip3 install flask 
RUN pip3 install keras 
RUN yum install gcc-c++ -y

RUN yum install python3-devel -y
RUN pip3 install --upgrade pip
RUN pip3 install tensorflow --no-cache-dir 
RUN pip3 install --upgrade tensorflow  
RUN pip3 install pillow
COPY ["covid-19.h5","diabetes_model.h5","/ws/"]
RUN mkdir /ws/templates
ADD templates /ws/templates
RUN mkdir /ws/Images
COPY app.py /ws/
EXPOSE 5000
RUN export FLASK_APP=/ws/app.py
ENTRYPOINT flask run --host='0.0.0.0' --port=5000

