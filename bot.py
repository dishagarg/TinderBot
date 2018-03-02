import fb_auth_token
import tinder_api
import config

fb_access_token = fb_auth_token.get_fb_access_token(config.fb_username, config.fb_password)
fb_user_id = fb_auth_token.get_fb_id(fb_access_token)

# Your real config file should simply be named "config.py"
# Just insert your fb_username and fb_password in string format
# and the fb_auth_token.py module will do the rest!
print fb_access_token
print fb_user_id

tinder_auth_token = tinder_api.get_auth_token(fb_access_token, fb_user_id)
print tinder_auth_token
print tinder_api.authverif(fb_access_token, fb_user_id)
print tinder_api.get_self()
