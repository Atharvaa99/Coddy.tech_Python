def get_capital(country_capitals,country_name):
     return country_capitals[country_name]

dic = {"Norway": "Oslo", "Sweden":"Stockholm"}
con = "Norway"
print(get_capital(dic,con))