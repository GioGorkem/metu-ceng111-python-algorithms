url = "http://www.google.com/search?q=ceng111&id=9317263&ie=UTF-8"
par = "id"

start_point = url.find(par + "=")

end_point = url.find("&", start_point)
if end_point != -1:
    opt = url[start_point + len(par)+1:end_point]
else:
    opt = url[start_point + len(par)+1:]
print(opt)
