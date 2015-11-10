import webapp2

from webapp2_extras import jinja2
from webapp2_extras import routes

class MainPage(webapp2.RequestHandler):

  @webapp2.cached_property
  def jinja2(self):
    # Returns a Jinja2 renderer cached in the app registry.
    return jinja2.get_jinja2(app=self.app)

  def get(self):
    rv = self.jinja2.render_template('new/index.html')
    self.response.write(rv)

app = webapp2.WSGIApplication([('/weds-meghashree', MainPage),
                               routes.RedirectRoute('/<:\w*>',
                                                    redirect_to='/weds-meghashree')],
                              debug=True)
