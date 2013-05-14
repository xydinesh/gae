from google.appengine.ext import db
from google.appengine.api import users
import webapp2
import cgi
import datetime
import urllib
import wsgiref.handlers

def project_key(project_name=None):
	"""Constructs a datastore key for a project entity with project name"""
	return db.Key.from_path("Project", project_name or 'default_project')

class Issue(db.Model):
	"""Models issues created in projects"""

	title = db.StringProperty(required=True)
	priority = db.IntegerProperty(required=True)
	description = db.StringProperty(multiline=True)
	due_date = db.DateProperty()
	created_time = db.DateProperty(auto_now_add=True)
	reporter = db.UserProperty()
	comments = db.StringListProperty()


class BugProject(webapp2.RequestHandler):
  def post(self):
    # We set the same parent key on the 'Greeting' to ensure each greeting is in
    # the same entity group. Queries across the single entity group will be
    # consistent. However, the write rate to a single entity group should
    # be limited to ~1/second.
    project_name = self.request.get('project_name')
    title = self.request.get('title')
    priority = int(self.request.get('priority'))
    issue = Issue(parent=project_key(project_name), title=title, priority=priority)

    if users.get_current_user():
    	issue.reporter = users.get_current_user()

    issue.description = self.request.get('description')
    issue.put()
    self.redirect('/?' + urllib.urlencode({'project_name': project_name}))