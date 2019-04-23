from kennethreitz/pipenv

# Python, don't write bytecode!
ENV PYTHONDONTWRITEBYTECODE 1

# Copy the source code over.
COPY . /app
RUN pipenv install --dev --system

RUN apt install bash -y

RUN find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

# Run setup.py test.
CMD pytest
