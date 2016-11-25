import webapp2
from Handlers import SellRegistration #as sell
from google.appengine.ext.webapp import template

class Data_Manager(webapp2.RequestHandler):
	def get(self):
		self.response.write(template.render("Templates/index.html", {}))

	def post(self):
		#last_sell = SellRegistration.get_last_sell()
		#new_sell = last_sell.sell_id() + 1
		selling = SellRegistration.register_sell(self.request.get('client_name'), self.request.get('art_id'), self.request.get('user_id'), self.request.get('art_description'), self.request.get('art_brand'), self.request.get('art_model'), self.request.get('art_price'), self.request.get('art_tax'))
		self.redirect("/main_page")
		#self.response.write('hello')