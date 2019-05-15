from rauth import OAuth2Service
import json

nation_slug = "pointblankdev"
oauth_id = "69c795c86f160f200db75597ca9b9a3e82ef8980769056802d7826d682289fa7"
oauth_secret = "29690408c988744532cc94245b5081cfb55955c23ebfea17ad7d09e357d86f7c"
redirect_uri = "https://pointblankdev.nationbuilder.com/oauth_callback"
code ="c921f8957408faf2bc262d2d54dd902e312e8e1d88680e19cc3fc37329602de0"

access_token_url = "http://" + nation_slug + ".nationbuilder.com/oauth/token"
authorize_url = nation_slug + ".nationbuilder.com/oauth/authorize"
service = OAuth2Service(
            client_id = oauth_id,
            client_secret = oauth_secret,
            name = "First_app",
            authorize_url = authorize_url,
            access_token_url = access_token_url,
            base_url = nation_slug + ".nationbuilder.com")

token = service.get_access_token(
    decoder=json.loads,
    data = {
        "code": code,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"}
)

session = service.get_session(token)

response = session.get(
    "https://"+nation_slug+".nationbuilder.com/api/v1/people", 
    params={'format': 'json'}, 
    headers={'content-type': 'application/json'}
)

#actual work

# create a person
create_person = {
  "person": {
    "last_name": "Snow",
    "first_name": "Jane",
    "email": "jane@danorf.ca",
    "sex": "F",
    "signup_type": 0,
    "employer": "Free Folk Inc",
    "party": "C",
    "registered_address": {
      "state": "BC",
      "country_code": "CA"
    }
  }
}
response = session.post(
    "https://" + nation_slug + ".nationbuilder.com/api/v1/people",
    params={'format': 'json', 'person': create_person},
    headers={'content-type': 'application/json'}
)