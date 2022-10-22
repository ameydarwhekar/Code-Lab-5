#Based on Python
FROM python

# Install the python library flask and requests

RUN pip3 install flask
RUN pip3 install requests

RUN pip install psycopg2-binary --user
RUN pip3 install psycopg2

# Creating a volume
VOLUME app

# Creating a WORKDIR app to unify all the elements
WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["api.py"]