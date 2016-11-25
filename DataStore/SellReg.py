from google.appengine.ext import ndb

class Sell_Art(ndb.Model):
	sell_id = ndb.IntegerProperty()
	client_name = ndb.StringProperty()
	art_id = ndb.IntegerProperty()
	collab_id = ndb.IntegerProperty()
	descrption = ndb.StringProperty()
	brand = ndb.StringProperty()
	model = ndb.StringProperty()
	amount = ndb.FloatProperty()
	taxes = ndb.FloatProperty()
	date = ndb.DateTimeProperty(auto_now_add = True)
	
	def set_id(self, id):
		self.sell_id = int(id)
	
	def set_client_name(self, name):
		self.client_name = str(name)
		
	def set_art_id(self, art_id):
		self.art_id = int(art_id)
			
	def set_collaborator(self, collab_id):
		self.collab_id = int(collab_id)
		
	def set_description(self, descrption):
		self.descrption = str(descrption)
		
	def set_brand(self, brand):
		self.brand = str(brand)
		
	def set_model(self, model):
		self.model = str(model)
		
	def set_amount(self, amount):
		self.amount = float(amount)
		
	def set_taxes(self, tax):
		self.taxes = float(tax)
		
	def save_sell(self):
		self.put()
		
	def get_all(self):
		return self.all()
		
	def get_last_selled_art(self):
		return self.all().order(-self.date).get()
		
		
		