import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener

print('Hello world');

#Consumer keys and access tokens, used for OAuth
consumer_key = 'DZZZlqwtgP8YfsRbICqHA5BUd'
consumer_secret = 'KEF2ANyqZsUjrMJpk9zbAx0rluRVf5bHJEgDDpwIAC6NQl2aKK'
access_token = '1010956451999670272-Ay607OrRAmRwIhgXITvkpweqtsgEKZ'
access_token_secret = 'J8Ep8i3FwnMj1X5CypOzfTXFCqrFqo1hlxfIPtJb7eKtF'

#OAuth process using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

#Creation of the actual interface
api = tweepy.API(auth)

#Sample method used to update a status
#api.update_status('Hello ,Its Nancy Pitta')

#Creating a user object
user = api.me()
print('Name: '+user.name)
print('Location: '+user.location)
print('Friends: '+str(user.friends_count))

class StdOutListener(StreamListener):
    '''Handles data received from the stream.'''

    def on_status(self,status):
        #Prints the text of the tweet
        print('Tweet text: '+status.text)

        #There are many options in the status object
        #hashtags access now
        for hashtag in status.entries['hashtags']:
            print(hashtag['text'])
        return true

        def on_error(self,status_code):
            print('Error is '+str(status_code))
            return true

        def on_timeout(self):
            print('TImeout')
            return true

if __name__ == '_main__':
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream = Stream(auth,listener)
    stream.filter(follow=[38744894],track=['#pythoncentral'])
