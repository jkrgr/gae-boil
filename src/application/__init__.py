import os
import sys
import webapp2
from urls import urls


sys.path.insert(1, os.path.join(os.path.abspath('..'), 'lib'))
app = webapp2.WSGIApplication(urls, debug=True)
