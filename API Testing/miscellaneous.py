import requests

url = 'https://rahulshettyacademy.com/'
cookie = {'visit-month' :'October'}
r = requests.get(url,allow_redirects=False, cookies=cookie, timeout=1)   #- Added Redirection as false and timeout =1 for getting proper respose
print(r.history)                ##- For checking redirection history
print(r.status_code)

## -- Checking wheter cookies accepted by server or not

url2 = "https://httpbin.org/cookies"
##-- For Calling cookies from Session manager, creating session manager below

se = requests.session()
se.cookies.update(cookie)

res = se.get(url2, cookies={'visit-year':'2022'})
print(res.status_code)
print(res.text)


## -- Sending Attachments
img_url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
img_file = {'file': open('C:\\Users\\VINOD\\Downloads\\profile_pic.png', 'rb')}
img_resp = requests.post(img_url,files=img_file)
print(img_resp.status_code)
print(img_resp.text)

# url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
# files = {'file': open('C:\\Users\\Owner\\Documents\\ra.png', 'rb')}
# r = requests.post(url, files=files)
# print(r.status_code)
# print(r.text)
