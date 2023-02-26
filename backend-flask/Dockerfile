# experiment with multi stage pipeline
FROM python:3.10-slim-buster AS dependencies
WORKDIR /backend-flask
COPY . .
RUN pip3 install -r requirements.txt


FROM dependencies
WORKDIR /backend-flask
COPY --from=dependencies /usr/local /usr/local
COPY --from=dependencies . .
ENV FLASK_ENV=development
EXPOSE ${PORT}
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
