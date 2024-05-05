FROM python:alpine
RUN pip install nltk
WORKDIR /dir
COPY main.py /dir/
COPY random_paragraphs.txt /dir/
CMD python main.p
