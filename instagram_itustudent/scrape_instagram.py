from igramscraper.instagram import Instagram
from time import sleep
from pprint import pprint as pp
import json

instagram = Instagram()

# authentication supported
instagram.with_credentials('louisscraper', 'x')
instagram.login()

# Getting an account by id
account = instagram.get_account('itustudent')

digest = {}

medias = instagram.get_medias("itustudent", 300)

for m in medias:
    comment_texts = []

    if m.comments_count > 0:
        comments = instagram.get_media_comments_by_id(m.identifier)['comments']
        comment_texts = [x.text for x in comments]

    digest[m.identifier] = {
        "id": m.identifier,
        "time": m.created_time,
        "comment_count": m.comments_count,
        "caption": m.caption,
        "comments": comment_texts
    }

with open('results.json', 'w') as f:
    json.dump(digest, f)

# pp(digest)


# with open('results.data', 'w') as f:
#     for media in medias:
#         f.write(
#             f"{media,}"
#         )

# print(dir(medias[0]))

# print(medias[1])

# print(medias[1].identifier)
# print(medias[1].created_time)
# print(medias[1].comments_count)
# print(medias[1].caption)

# comments = instagram.get_media_comments_by_id(medias[1].identifier)

# for com in comments['comments']:
#     print(com.text)


# Available fields
# print('Account info:')
# print('Id: ', account.identifier)
# print('Username: ', account.username)
# print('Full name: ', account.full_name)
# print('Biography: ', account.biography)
# print('Profile pic url: ', account.get_profile_picture_url())
# print('External Url: ', account.external_url)
# print('Number of published posts: ', account.media_count)
# print('Number of followers: ', account.followed_by_count)
# print('Number of follows: ', account.follows_count)
# print('Is private: ', account.is_private)
# print('Is verified: ', account.is_verified)

# or simply for printing use
# print(account)