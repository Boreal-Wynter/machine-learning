#!/bin/bash

docker build -q -t machine-learning-image .

docker run machine-learning-image

python create_file_diagram.py