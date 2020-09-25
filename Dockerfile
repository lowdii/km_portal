#Grab the latest alpine image
FROM python:3.7
ENV PYTHONBUFFERED 1

# Install python and pip
#RUN apk add --no-cache --update python3 py3-pip bash
ADD ./requirements.txt /tmp/requirements.txt




# Add our code
ADD . /opt/kmportal
WORKDIR /opt/kmportal

# Install dependencies
RUN pip3 install -r /tmp/requirements.txt

#RUN pip3 install six
#RUN pip3 install --upgrade six

# Expose is NOT supported by Heroku
# EXPOSE 5000 		
#RUN python manage.py migrate

RUN python manage.py collectstatic

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			

CMD python manage.py runserver 0.0.0.0:$PORT
