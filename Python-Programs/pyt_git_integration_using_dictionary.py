#Imported module called requests to integrate with Github
import requests
#Retrieved Github Pull requests details of kubernetes Repo using Github API URL
api_response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
#Converted the received json response to dictionary using requests module method called .json()
complete_details = api_response.json()
#Iterated through the entire dictionary items using for loop to fetch names who made pull requests
for item in range(len(complete_details)):
    print(complete_details[item]["user"]["login"])
    