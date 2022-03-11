FROM python:2.7

COPY crisporWebsite .

ADD crisporWebsite/crispor.py /

RUN apt-get update

RUN apt -y install r-base

RUN pip2.7 install biopython==1.76 numpy==1.14.0 scikit-learn==0.16.1 pandas twobitreader matplotlib pytabix scipy

RUN Rscript -e 'install.packages(c("e1071"),  repos="http://cran.rstudio.com/")'

CMD [ "python2.7", "./crispor.py" ]

#FROM ubuntu
#ENTRYPOINT exec top -b