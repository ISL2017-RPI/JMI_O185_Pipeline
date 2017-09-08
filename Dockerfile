FROM keyi/python2-mcr2017a-rpi-isl

COPY JMI_O185/ ./JMI_O185
COPY setup.py ./
COPY O185_JMI_wrapper.py ./
COPY trainData.csv ./
COPY trainTargets.csv ./
