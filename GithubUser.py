#Gives user details
import requests
import urllib.request
from PIL import Image
import os

os.path.dirname(os.path.abspath(__file__))

def dp(url,name):
    if not os.path.isfile(os.path.dirname(os.path.abspath(__file__))+name+'.jpg'):  #issues over here dude
        print('Image already exists , Please check username entered .')
    #gets updated if changed
    urllib.request.urlretrieve(url,name+".jpg")

name = input('Enter Username : ')

url = "https://api.github.com/users/"+name

req=requests.get(url)
data = req.json()   # has dict of data with links
#print(data)

#Image
dp(data['avatar_url'],name)    # list key : avatar_url
pic= Image.open(name+".jpg")
pic.show()

#name , email , bio , followers , following , public repos
print('Name : ', data['name'])
if (data['company']!='None'): print("Company : ",data['company'])
print('Location : ', data['location'])
print('Email : ', data['email'])
print('Bio : ',data['bio'])
print('Public Repositories : ',data['public_repos'])
print('Follower count : ', data['followers'])
print('Following count : ',data['following'])

#last active , joined Github
print("Joined Github on : " , str(data['created_at'])[:-10])
print('Last Activity : ', str(data['updated_at'])[:-10])

#Last watched ( stalk :-P )
stu = "https://api.github.com/users/"+ name +"/events"
stureq = requests.get(stu)
stdata = stureq.json()
print("Last Watched/starred : ",stdata[0]['repo']['name'])
print("On : ", str(stdata[0]['created_at'])[:-10])
print("Link to last watched : ", "https://github.com/"+str(stdata[0]['repo']['name']))

print()
choice = input('Do you want list of followers & following of '+ name +'(y/n) ? ')
if choice =='y':
    follows="https://api.github.com/users/"+name+"/followers"
    followreq = requests.get(follows)
    followdata = followreq.json()
    print()
    print("Followers of "+name +"\n")
    for i in range(data['followers']):
        print(followdata[i]['login'])
    followings="https://api.github.com/users/"+name+"/following"
    followingreq=requests.get(followings)
    followingdata = followingreq.json()
    print()
    print(name + " is following : \n")
    for i in range(data['following']):
        print(followingdata[i]['login'])