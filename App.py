import tweepy
import time
auth = tweepy.OAuthHandler('UNUAHlyAXnOL6N0PczlF69Dk4','78f82EH9Xte2EmXFMzKS6XdLmzX8gbM32KVWKJwmXMDqduAx2o')
auth.set_access_token('1348646057308082177-K6o0gV8Nz7foPwJ7Hpr7Xu7UuaTEth','PC6sRN7gfI9j5uVSHt5UrXyxWQw2CaXVccV9ZNRk5Xfx4')

api = tweepy.API(auth)

user = api.get_user('SushantRanade3')
f = user.followers_count
api.update_profile(name=f'Sushant {f} Followers')
print(f'Sushant {f} Followers')
time.sleep(60)
