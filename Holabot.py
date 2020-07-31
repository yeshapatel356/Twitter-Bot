import tweepy
import time

print("\n\nHelloWorld! I am  BOT. My name is Hola\n\n")

CONSUMER_KEY = 'XXXXXX'
CONSUMER_SECRET =  'XXXXXX'
ACCESS_KEY = 'XXXXXX'
ACCESS_SECRET = 'XXXXXX'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth) 

def retrieve_last_tweet_id(file_name):
    f_read = open(file_name, 'r')
    last_tweet_id = int(f_read.read().strip())
    f_read.close()
    return last_tweet_id

def store_last_tweet_id(last_tweet_id,file_name):
    f_write = open(file_name,'w')
    f_write.write(str(last_tweet_id))
    f_write.close()
    return

# REPLYING TO TWEETS CONATAIN HEY BY MENTIONING ME
def reply_to_tweets():

    print("retriveing and replying tweets")
    last_tweet_id = retrieve_last_tweet_id('last_tweet_id.txt')

    mentions =  api.mentions_timeline()
    #or 'hi'or "hy" or "hello" or "hola"
    for mention in reversed(mentions):
        print(str(mention.id)+ '--' + mention.text)
        last_tweet_id = mention.id
        store_last_tweet_id(last_tweet_id,'last_tweet_id.txt')
        lowermention = mention.text.lower()
        if('hey' in lowermention):
            print('\n\nHey! I found #hey...\n')
            api.update_status("@"+ mention.user.screen_name + " Hey There!! I am Hola bot." , mention.id)
            print("\ndone replying to",mention.user.screen_name ," Id =", mention.id,'\n')
        elif('hi' in lowermention):
            print('\n\nHey! I found #hey...\n')
            api.update_status("@"+ mention.user.screen_name + " Hi There! I am Hola bot" , mention.id)
            print("\ndone replying to",mention.user.screen_name ," Id =", mention.id,'\n')
        elif('hello' in lowermention):
            print('\n\nHey! I found #hey...\n')
            api.update_status("@"+ mention.user.screen_name + " Hello There! I am Hola bot" , mention.id)
            print("\ndone replying to",mention.user.screen_name ," Id =", mention.id,'\n')
        elif('hy' in lowermention):
            print('\n\nHey! I found #hey...\n')
            api.update_status("@"+ mention.user.screen_name + " Hy There! I am Hola bot" , mention.id)
            print("\ndone replying to",mention.user.screen_name ," Id =", mention.id,'\n')
        elif('hii' in lowermention):
            print('\n\nHey! I found #hey...\n')
            api.update_status("@"+ mention.user.screen_name + " Hii There! I am Hola bot" , mention.id)
            print("\ndone replying to",mention.user.screen_name ," Id =", mention.id,'\n')
        elif('hola' in lowermention):
            print('\n\nHey! I found #hey...\n')
            api.update_status("@"+ mention.user.screen_name + " Hey There! I am Hola bot. Thanks For mentioning me" , mention.id)
            print("\ndone replying to",mention.user.screen_name ," Id =", mention.id,'\n')
        elif('helloworld' in lowermention):
            print('\n\nHey! I found #hey...\n')
            api.update_status("@"+ mention.user.screen_name + " Hey World! I am Hola bot" , mention.id)
            print("\ndone replying to",mention.user.screen_name ," Id =", mention.id,'\n')
        else:
            print("No Greating")
            api.update_status("@"+ mention.user.screen_name + " HELLOWORLD! I am Hola bot" , mention.id)
            print("\ndone replying to",mention.user.screen_name ," Id =", mention.id,'\n')
    


def reply_to_home_tweet():
    print("retriveing and replying tweets")
    last_tweet_id = retrieve_last_tweet_id('last_tweet_id.txt')
    home_tweets = api.home_timeline()
    for home_tweet in home_tweets:
        print(str(home_tweet.id)+ '--' + home_tweet.text)
        last_tweet_id = home_tweet.id
        store_last_tweet_id(last_tweet_id,'last_tweet_id.txt')
        api.update_status("@"+ home_tweet.user.screen_name + " #HELLOWORLD" , home_tweet.id)
        print("\ndone replying to",home_tweet.user.screen_name ," Id =", home_tweet.id,'\n')
        

        
if __name__ == "__main__": 
    #IT WILL AUTOMATICALLY REPLY TO ALL LATEST TWEETS WHO MENTION YOU 
    reply_to_tweets()
    #IT WILL AUTOMATICALLY REPLY TO ALL LATEST TWEETS IN YOUR HOME PAGE
    reply_to_home_tweet()
    time.sleep(15)