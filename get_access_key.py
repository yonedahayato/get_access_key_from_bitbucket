from rauth.service import OAuth1Service
import sys

OAUTH_REQUEST = "https://bitbucket.org/api/1.0/oauth/request_token"
OAUTH_AUTH = "https://bitbucket.org/api/1.0/oauth/authenticate"
OAUTH_ACCESS = "https://bitbucket.org/api/1.0/oauth/access_token"

def authorize(CONSUMER_KEY, CONSUMER_SECRET):
    service = OAuth1Service(name='bitbucket', consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                         request_token_url=OAUTH_REQUEST,
                         access_token_url=OAUTH_ACCESS,
                         authorize_url=OAUTH_AUTH)
    rtoken, rtokensecret = service.get_request_token(method='GET')
    auth_url = service.get_authorize_url(rtoken)
    print("Visit this url and copy&paste your PIN.\n{0}".format(auth_url))
    pin = raw_input('Please enter your PIN:')
    r = service.get_access_token('POST', request_token=rtoken, request_token_secret=rtokensecret,
                                 data={'oauth_verifier': pin})
    content = r.content
    return content['oauth_token'], content['oauth_token_secret']

if __name__ == "__main__":
    argvs = sys.argv
    consumer_key = argvs[1]
    consumer_secret = argvs[2]
    authorize(consumer_key, consumer_secret)
