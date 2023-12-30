from instagrapi import Client

username = input('username: ')
password = input('password: ')

client = Client()
client.login(username,password)

hashtag = "programming"
medias = client.hashtag_medias_top(hashtag, 20)

arr = [4,5,1,2]

for i, media in enumerate(medias):
  client.media_like(media.id)
  print(f"Liked post {i+1} of hashtag {hashtag}")
  #each 3rd person
  if i % 3 == 0:
    client.media_comments('41244', 7)
    print(f"Commented this post")