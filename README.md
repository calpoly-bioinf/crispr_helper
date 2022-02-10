# TheAltRockers

The *Pipeline* code for this project can be found in the pipeline folder.
In order to run the pipeline, you must run the Crispor code on a Virtual Machine.

The *alt-rockers* folder contains the barebones foundation for a web application interface. This has not been implemented yet.
The Web application uses a flask backend and react frontend.

The *algorithmAnalysis* folder contains the jupyter notebook used to run the algorithm analysis on our chosen off target sequence algorithms.

## Building Dockerfile

docker build --tag crispr-website .

## Starting

./start_website.sh

## Stopping

./stop_website.sh