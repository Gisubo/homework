FROM texlive/texlive:latest

RUN apt-get update && apt-get install -y python3 python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install . --break-system-packages
CMD ["python3", "test.py"]
