FROM python:3.8.1-alpine

ADD app.py .

# Set up and activate virtual environment
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

CMD [ "python", "./app.py" ]
