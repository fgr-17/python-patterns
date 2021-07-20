#!/usr/local/bin/python3
import sys
import log_decorator as ld

log1 = ld.FileLogger(sys.stdout)
log2 = ld.LogFilter('Error', log1)

log1.log('Noisy: this logger always produces output')

log2.log('Ignored: this will be filtered out')
log2.log('Error: this is important and gets printed')

log3 = ld.LogFilter('severe', log2)

log3.log('Error: this is bad, but not that bad')
log3.log('Error: this is pretty severe')