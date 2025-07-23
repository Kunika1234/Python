import streamlit as st
import requests
import webbrowser
from urllib.parse import urlencode, parse_qs
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://localhost:8000"
AUTH_URL = "https://www.linkedin.com/oauth/v2/authorization"
TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"
SCOPE = "w_member_social"

access_token = None

class OAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        query_components = parse_qs(self.path.split("?")[1])
        auth_code = query_components["code"][0]
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"You can close this tab now.")

def get_auth_code():
    params = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
    }
    url = f"{AUTH_URL}?{urlencode(params)}"
    webbrowser.open(url)

    server = HTTPServer(("localhost", 8000), OAuthHandler)
    server.handle_request()

def get_access_token(auth_code):
    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    response = requests.post(TOKEN_URL, data=data).json()
    return response["access_token"]

def get_user_urn(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("https://api.linkedin.com/v2/me", headers=headers).json()
    return f"urn:li:person:{response['id']}"

def post_to_linkedin(token, message):
    urn = get_user_urn(token)
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
    }
    post_data = {
        "author": urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": message},
                "shareMediaCategory": "NONE",
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }
    r = requests.post("https://api.linkedin.com/v2/ugcPosts", json=post_data, headers=headers)
    return r.status_code, r.text

st.title("🔗 LinkedIn Auto Poster")

message = st.text_area("Write your LinkedIn Post")
if st.button("Authenticate & Post"):
    with st.spinner("Authenticating..."):
        get_auth_code()
        token = get_access_token(auth_code)
        st.success("✅ Authentication successful!")

    with st.spinner("Posting to LinkedIn..."):
        status, text = post_to_linkedin(token, message)
        if status == 201:
            st.success("✅ Successfully posted to LinkedIn!")
        else:
            st.error(f"❌ Error: {text}")
