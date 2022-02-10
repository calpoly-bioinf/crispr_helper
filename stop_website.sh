#!/bin/bash

for container_id in `docker ps | grep crispr-website | awk '{print $1}'`
do
    docker stop $container_id
done;