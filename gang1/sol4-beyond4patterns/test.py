#!/usr/local/bin/python3
import sol4_only_logger as ol
import sys

f = ol.TextFilter('Error')
h = ol.FileHandler(sys.stdout)
logger = ol.Logger([f], [h])

logger.log('Ignored: this will not be logged')
logger.log('Error: this is important')