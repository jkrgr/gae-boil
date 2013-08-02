import webapp2
import handlers

urls = [
    webapp2.Route(r'/', handlers.HelloHandler),
    webapp2.Route(r'/hello', handlers.HelloTemplateHandler)
]
