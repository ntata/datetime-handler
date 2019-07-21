FROM python:3.6.1-onbuild
EXPOSE 5000
CMD ["python", "datetime-handler.py"]
