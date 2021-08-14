FROM centos:latest
WORKDIR /ws
RUN yum install python3 -y
RUN pip3 install flask 
RUN pip3 install keras 
RUN yum install gcc-c++ -y

RUN yum install python3-devel -y
RUN pip3 install --upgrade pip
RUN pip3 install tensorflow --no-cache-dir  tensorflow
RUN pip3 install --upgrade tensorflow  
RUN pip3 install pillow
COPY ["covid.h5","diabetes_model.h5","/ws/"]
RUN mkdir /ws/templates
ADD templates /ws/templates
RUN mkdir /ws/Images
COPY app.py /ws/
EXPOSE 5000
CMD python3 /ws/app.py


