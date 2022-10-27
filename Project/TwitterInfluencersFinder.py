import tweepy
import time
import random

#f.write("This will be in the text")
#f.close()

with open("names1.txt", 'r') as read_obj:
    t1k = read_obj.readlines()
    a = ''
    for i in t1k:
        a += i
    t1k = a
with open("names2.txt", 'r') as read_obj:
    t3k = read_obj.readlines()
    a = ''
    for i in t3k:
        a += i
    t3k = a
with open("names3.txt", 'r') as read_obj:
    t5k = read_obj.readlines()
    a = ''
    for i in t5k:
        a += i
    t5k = a




consumer_key = 'WUA3Hcmt1W0qiU9oeD8R48Gzw'
consumer_secret = '9S8kspaIDvpYVgV1P5cKcpl5tKvUcbyB8sWq0AwNjOTUmeqn9r'

access_token = '1411985008412270593-P3hlgkagLD7sCbfe2unKkFjTLrqqxq'
access_token_secret = 'tFcYSNzTFrLL2h6geiInTflywRPgQxsVayEIxkWHN3ru6'

callback_url = 'oob'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret,callback_url)
#auth.set_access_token(access_token, access_token_secret)

#api = tweepy.API(auth,wait_on_rate_limit=True)
api = tweepy.API(auth)


def wait(time):
    for i in range(time):
        print (i)
        time.sleep(1)


####user = api.get_user("PZelekha")
####recipient_id = user.id_str
####text = "Testing"
####direct_message = api.send_direct_message(recipient_id, text)

#result = twitter.friendships.show(source_screen_name = source,

print("done!")


#user = api.get_user(StartingUser)

def CheckIfNotIn(File,Pharse):
    if Pharse in File:
        return False
    else:
        return True

def ChooseStarter():
    with open("names2.txt", 'r') as read_obj:
        t3k = read_obj.readlines()
        a = t3k
        a = a[-1]
        a = a[:-1]
        print("New starter:  " + a)
    return a

def Wait(Time):
    for i in range(Time):
        print(i)
        time.sleep(1)

def WriteStuff(File,Name):
    Obj = open(File,"a")
    Obj.write(user.screen_name+'\n')
    Obj.close()
#try:

StartingUser = ChooseStarter()
def Main (StartingUser):
    global t1k
    global t3k
    global t5k
    try:
        while True:
            counter = 0
            for user in tweepy.Cursor(api.friends, screen_name=StartingUser).items():
                if counter < 5:
                    print(user.screen_name)
                    if 1500 < user.followers_count < 3000:
                        if CheckIfNotIn(t1k,user.screen_name):
                            t1k += user.screen_name+'\n'
                            counter += 1
                    elif 3000 < user.followers_count < 5000:
                        if CheckIfNotIn(t3k,user.screen_name):
                            t3k += user.screen_name+'\n'
                            counter += 1
                    elif 5000 < user.followers_count < 10000:
                        if CheckIfNotIn(t3k,user.screen_name):
                            t5k += user.screen_name+'\n'
                            counter += 1
                    else:
                        print("------------------^Pass^------------------")
                else:
                    f = open("names1.txt", 'w+')
                    f.write(t1k)
                    f.close()
                    f = open("names2.txt", 'w+')
                    f.write(t3k)
                    f.close()
                    f = open("names3.txt", 'w+')
                    f.write(t5k)
                    f.close()
                    counter = 0
    except:
        Wait(60)
        Main(ChooseStarter())


Main(StartingUser)

#for user in tweepy.Cursor(api.followers, screen_name=StartingUser).items():
#    print('follower: ' + user.screen_name)