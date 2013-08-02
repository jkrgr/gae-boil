import os
import webapp2
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('%s/templates' % os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])


class HelloHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class HelloTemplateHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {'hello': 'world'}
        template = JINJA_ENVIRONMENT.get_template('content.html')
        self.response.write(template.render(template_values))

