from DataStore import SellReg# as SellReg

def register_sell(client_name, art_id, collab_id, description, brand, model, amount, tax):
	#last_sell = SellReg.Sell_Art.get_last_selled_art()
	#last_sell = SellReg.Sell_Art.get_all()
	#for sells in last_sell:
	#	sells = sells + 1
	
	sell = SellReg.Sell_Art()
	sell.set_id(1)
	sell.set_client_name(client_name)
	sell.set_art_id(art_id)
	sell.set_collaborator(collab_id)
	sell.set_description(description)
	sell.set_brand(brand)
	sell.set_model(model)
	sell.set_amount(amount)
	sell.set_taxes(tax)
	sell.save_sell()
	#return True

def get_all_sell_art():
	return SellReg.Sell_Art.get_all()
	
def get_allEnable_Phones():
	phones = Telefonos.UserPhone.all().filter('phone_enable =', True)
	return phones