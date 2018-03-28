FROM centos:latest

RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y python-pip --enablerepo=epel
RUN pip install pip --upgrade

COPY requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt
COPY app.py /root/app.py

CMD python /root/app.py
