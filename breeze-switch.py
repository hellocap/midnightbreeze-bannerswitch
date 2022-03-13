import tweepy
import random
import tempfile
import requests

# Using Tweepy's OAuthHandler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# list of MB ids - input here the # corresponding to your midnight breeze
MB_list = [6377,4216,2732,2342,1757,1744,1224,1098]

# format of pinata link to your MB : https://midnightbreeze.mypinata.cloud/ipfs/QmVcZrjzmT7CMa2nkgLN5nXVaydxtwPoyUdofNDLwzFTS8/(number).png
filename = str(MB_list[random.randint(0, len(MB_list)-1)]) + '.png'

url =  f"https://midnightbreeze.mypinata.cloud/ipfs/QmVcZrjzmT7CMa2nkgLN5nXVaydxtwPoyUdofNDLwzFTS8/{filename}"

file = requests.get(url)
temp = tempfile.NamedTemporaryFile(suffix=".png")
try:
    temp.write(file.content)         
    api.update_profile_banner(filename=temp.name)
finally:
    temp.close()