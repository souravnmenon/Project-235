import requests

for i in range(1,5001,1):
  url = "http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id={i}"
  o = requests.get(url)
  if o.status_code==200:
    print("Success",i)
  else:
    print("Fail",i)
