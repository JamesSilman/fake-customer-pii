import faker

from faker import Faker
fake = Faker()

f = open("customer_database.csv", "w")
f.write("name, phone, job, ssn, address_building_number, address_street, address_street_name, address_street_suffix, address_city, address_postcode, address_country, cc_number, cc_expires, cc_security_code, cc_provider, bank_country\n")

number_of_database_entries = 100

i = 0
while i < number_of_database_entries:
	f.write(

		fake.name() + "," + 
		fake.phone_number() + "," + 
		fake.job().replace(",", "") + "," +
		fake.ssn() + "," +

		fake.building_number() + "," +
		fake.street_address() + "," +
		fake.street_name() + "," +
		fake.street_suffix() + "," +
		fake.city() + "," +
		fake.postcode() + "," +
		fake.country() + "," +

		fake.credit_card_number() + "," +
		fake.credit_card_expire() + "," +
		fake.credit_card_security_code() + "," +
		fake.credit_card_provider() + "," +
		fake.bank_country()
		
		+ "\n")
	i += 1

f.close()
