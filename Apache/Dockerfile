FROM ubuntu:latest
RUN apt-get update && apt-get install -y apache2 && apt-get install -y git
RUN apt clean 
RUN git clone https://github.com/drozkie/webtest.git /tmp/gr/webtest
RUN cp /tmp/gr/webtest/pipeline.html /var/www/html/
RUN rm -rf /tmp/gr/webtest
EXPOSE 8081
CMD ["apache2ctl", "-D", "FOREGROUND"]