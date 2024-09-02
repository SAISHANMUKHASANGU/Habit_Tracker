import requests
from datetime import datetime

USERNAME="shanmukha0607"
TOKEN="shanmukha23456sangu"
GRAPH_ID="graph2"

pixela_endpoint="https://pixe.la/v1/users"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}

# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    "id":GRAPH_ID,
    "name":"Coding Graph",
    "unit":"Hours",
    "type":"int",
    "color":"ajisai"
}

header={
    "X-USER-TOKEN":TOKEN
}

# response=requests.post(url=graph_endpoint,json=graph_config,headers=header)
# print(response.text)

pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today=datetime.now()

pixel_params={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many hours did you code today: ")
}
response=requests.post(url=pixel_endpoint,json=pixel_params,headers=header)
print(response.text)

pixel_update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
update_parametrs={
    "quantity":"15"
}
# response=requests.put(url=pixel_update_endpoint,json=update_parametrs,headers=header)
# print(response.text)

delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

# response=requests.delete(url=delete_endpoint,headers=header)
# print(response.text)