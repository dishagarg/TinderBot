import fb_auth_token
import tinder_api as api
import config
import re
import json

fb_access_token = fb_auth_token.get_fb_access_token(config.fb_username, config.fb_password)
fb_user_id = fb_auth_token.get_fb_id(fb_access_token)

# Your real config file should simply be named "config.py"
# Just insert your fb_username and fb_password in string format
# and the fb_auth_token.py module will do the rest!
print fb_access_token
print fb_user_id

tinder_auth_token = api.get_auth_token(fb_access_token, fb_user_id)
print tinder_auth_token
# print api.authverif(fb_access_token, fb_user_id)
# print api.get_self()


def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

person_id=''

def likeAPerson():
    for key, value in api.get_recommendations().items():
        if(key == "results"):
            for person in value:
                rating = 0
                for key, value in person.items():
                    if(key == "_id"):
                        person_id = value
                        print person_id
                    if(key == "photos" and len(value) > 1):
                        print "photos OK!"
                        rating += 1
                    if((key=="bio") and value!=""):
                        rating += 1
                        if(any(word in value for word in config.desired_job)):
                            print value.encode('utf-8', 'replace')
                            rating += 1
                    if((key=="teasers") and len(value) > 1):
                        rating += 1
                    if((key=="jobs") and len(value) > 1):
                        rating += 1
                if rating>=3:
                    print api.like(person_id)
        

likeAPerson()

#matches = api.get_updates()['matches']
#
#with open('data.txt', 'w') as outfile:
#    json.dump(matches, outfile)

#ms = api.send_msg(config.match_id, config.msg)
#print ms
