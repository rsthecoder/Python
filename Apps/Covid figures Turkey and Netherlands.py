#first install corona module -> pip install covid
#https://pypi.org/project/covid/

print("Python package to get information regarding the novel corona virus provided by Johns Hopkins university and worldometers.info\n")

from covid import Covid

#covid = Covid() #default
covid = Covid(source="worldometers")

# countries = covid.list_countries() -> print(countries)


tur = covid.get_status_by_country_name("Turkey")
net = covid.get_status_by_country_name("Netherlands")

#data for Turkey
tur_total = tur["confirmed"]
tur_new = tur["new_cases"]
tur_deaths = tur["new_deaths"]
tur_tests = tur["total_tests"]

#data for Netherlands
net_total = net["confirmed"]
net_new = net["new_cases"]
net_deaths = net["new_deaths"]
net_tests = net["total_tests"]

data_all_tur = """
Corona figures for Turkey
Total cases     : {:,}
New cases today : {:,}
New deaths      : {} 
Total tests     : {:,}

""".format(tur_total, tur_new,tur_deaths,tur_tests)

data_all_net = """
Corona figures for Netherlands
Total cases     : {:,}
New cases today : {:,}
New deaths      : {} 
Total tests     : {:,}

""".format(net_total, net_new,net_deaths,net_tests)



print(data_all_tur)
print(data_all_net)

input("Enter any key to quit")

