FROM python

# Install the python library flask and requests
RUN pip3 install flask
RUN pip3 install requests

# Creating volume
VOLUME app

# Creating a WORKDIR app to unify all the elements
WORKDIR /app

EXPOSE 81

ENTRYPOINT ["python"]
CMD ["consumer.py"]