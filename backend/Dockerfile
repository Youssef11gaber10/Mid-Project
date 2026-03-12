FROM python:3.11 AS build
# this gonna be builder i will collect all dependencies in env and pass it to smaller image
WORKDIR /app
COPY requirements.txt .
#create venv inside /opt/venv and activate it and install requirements
RUN python -m venv /youssef/venv && \
    . /youssef/venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt


# so we collect all dependencies in venv now move it to smaller image
FROM python:3.11-slim

COPY --from=build /youssef/venv /youssef/venv

WORKDIR /app

COPY . .

ENV PATH="$PATH:/youssef/venv/bin" 



EXPOSE 5000

# CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--workers", "3"]
CMD ["/youssef/venv/bin/python", "entrypoint.py"] 
# we change the gunicorn and run it in entry point to make the migrations and run the app with gunicorn
# you can specify port inside code but needed here also to define it when run command gunicorn
