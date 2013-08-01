import os
import webapp2
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('%s/templates' % os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class TemplateHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {'hello': 'world'}
        template = JINJA_ENVIRONMENT.get_template('content.html')
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([('/', MainHandler),
                               ('/hello', TemplateHandler)],
                              debug=True)
