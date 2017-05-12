FROM python
WORKDIR /wx-server
ADD . /wx-server
RUN pip install -r requirements.txt
EXPOSE 80
ENV NAME World
CMD ["python", "./wx-server/app.py"]