#Gives info on a particular repository

import requests

repo_name = input("Enter Repository Name : ")

url= "https://api.github.com/search/repositories?q="+repo_name
req = requests.get(url)
data = req.json()
#print(data)

#remaining

if data['total_count']==1 :
    print('Description : ', data['items'][0]['description'])
    print('Language : ',data['items'][0]['language'])
    print('Owner : ',data['items'][0]['owner']['login'])
    print('Stargazers : ', data['items'][0]['stargazers_count'])
    print('No of Forks : ',data['items'][0]['forks_count'])
    print('Description : ',data['items'][0]['description'])
    print('Created On ',str(data['items'][0]['created_at'])[:-10])
    print('Last Update : ',str(data['items'][0]['updated_at'])[:-10])
    print('Watcher count : ',data['items'][0]['watchers_count'])
    print('Open-issues : ',data['items'][0]['open_issues_count'])
elif data['total_count']>1:
    print('There are more than 1 repositories with '+ str(repo_name).upper())
    username=input('Please enter username so that we can narrow down the results : \n')

    #like why  ? results by repo_name can be >> results by username/repo_name
    url = "https://api.github.com/users/" + username + "/repos"
    req = requests.get(url)
    data = req.json()
    found = 0
    for i in range(len(list(data))):
        if data[i]['name']==repo_name:
            found = i
            break

    if found>0 :
        print('Owner : ', data[found]['owner']['login'])
        print('Stargazers : ', data[found]['stargazers_count'])
        print('Description : ', data[found]['description'])
        print('Language : ', data[found]['language'])
        print('No of Forks : ', data[found]['forks_count'])
        print('Description : ', data[found]['description'])
        print('Created On ', str(data[found]['created_at'])[:-10])
        print('Last Update : ', str(data[found]['updated_at'])[:-10])
        print('Watcher count : ', data[found]['watchers_count'])
        print('Open-issues : ', data[found]['open_issues_count'])

    else:
        print('please check the repository name and username entered ( searching done by query is case-sensitive )\n for now \n')
        print('No repository named ' + repo_name + ' found by '+ username)
else:
    print('Repository Does Not Exist , please check the repository name entered ( searching done by query is case-sensitive )')