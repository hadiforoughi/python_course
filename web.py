import requests as re
mydata={"name":"hadi","email":"hadiforooghi1377@gmail.com"}
# r=re.post("http://www.w3schools.com/php/welcome.php",data=mydata)
r=re.get("http://www.w3schools.com/php/welcome.php")
print(r.url)
file=open("./page.html","w+")
file.write(r.text)