FROM python:3.8-alpine
COPY ./requirements.txt /src/requirements.txt
WORKDIR /src
RUN pip install -r requirements.txt
RUN pip install debugpy
COPY /src /src
CMD [ "npm", "start"]
ENTRYPOINT ["python"]
CMD ["app.py"]
