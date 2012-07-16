import cgi

import webapp2
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp2.RequestHandler):
    def get(self):
       self.response.out.write("""
                               <html>
                                <body>
                                    <form action="/sign" method="post">
                                         <div><textarea name="content" rows="3" cols="60"></textarea></div>
                                         <div><input type="submit" value="Sign"></div>
                                </body>
                               </html>""")
       

class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.out.write('<html><body>You wrote: <pre>')
        self.response.out.write(cgi.escape(self.request.get('content')))
        self.response.out.write('</pre></body></html>')

    
app = webapp2.WSGIApplication([('/', MainPage),
                                ('/sign', Guestbook)])

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()  
