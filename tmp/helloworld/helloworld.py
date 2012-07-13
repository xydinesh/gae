import webapp2
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        
        if user :
            self.response.headers['Content-Type'] = 'text/html'
            self.response.out.write("<h3>Hello, " + user.nickname()+"</h3>")
        else:
            self.redirect(users.create_login_url(self.request.uri))

    
app = webapp2.WSGIApplication([('/', MainPage)])

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()  
