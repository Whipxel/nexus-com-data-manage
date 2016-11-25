import webapp2
from Handlers import Main_Page

app = webapp2.WSGIApplication([
	('/main_page',Main_Page.Data_Manager)

], debug=False)

def main():
	app.run()
	
if __name__ == '__main__':
	main()