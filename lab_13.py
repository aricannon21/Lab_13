#git is important for version control and it is th industry's standard
#git is usd before commands, git init
class delivery_personnel:
	def __init__(self, name, years_of_service, company, is_drone, zip_codes_covered):
		self.name = name
		self.years_of_service = years_of_service
		self.company = company
		self.is_drone = is_drone
		self.zip_codes_covered = zip_codes_covered

#getter methods
	def get_years_of_service(self):
		return(self.years_of_service)

	def get_company(self):
		return(self.get_company)


	def get_zip_codes_covered(self):
		return(self.zip_codes_covered)

#setter methods
	def set_years_of_service(self, d):
		self.years_of_service = d 

	def set_company(self, d):
		self.company = d 

	def set_zip_codes_covered(self, d):
		self.zip_codes_covered = d 

#recursive delivery
	def recursive_delivery(self, input_list):
		output_list = [i for i in input_list if self.zip_codes_covered]
		print(output_list)

def main():
	person_1 = delivery_personnel(name = 'Clhoe', years_of_service = 6, company = "UPS", is_drone = False, zip_codes_covered = "90271")
	input_list_1 = ['06525', '90274', '90271', '06527']
	person_1.recursive_delivery(input_list_1)

if __name__ == '__main__':
	main()
