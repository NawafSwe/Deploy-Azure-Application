import msal
from FlaskWebProject import Config
import uuid
from flask import session

def load_cache():
    cache = msal.SerializableTokenCache()
    if session.get("token_cache"):
        cache.deserialize(session["token_cache"])
    return cache


def save_cache(cache):
    if cache.has_state_changed:
        session["token_cache"] = cache.serialize()


def _build_msal_app(cache=None, authority=None):
    """
    building the clientConfidential app
    """
    return msal.ConfidentialClientApplication(
        client_id=Config.CLIENT_ID,
        client_credential=Config.CLIENT_SECRET,
        token_cache=cache,
        authority=authority,
    )


def build_auth_url(authority=None, scopes=None, state=None):
    return _build_msal_app(
        authority=authority or Config.AUTHORITY
    ).get_authorization_request_url(
        scopes=scopes,
        state=state or str(uuid.uuid4()),
        redirect_uri=f"https://cms-backend.azurewebsites.net" + Config.REDIRECT_PATH,
    )


def acquire_token_by_authorization_code(code, scopes, cache=None, redirect_uri=None):
    return _build_msal_app(
        authority=Config.AUTHORITY,
        cache=cache,
    ).acquire_token_by_authorization_code(
        code=code,
        scopes=scopes,
        redirect_uri=f"https://cms-backend.azurewebsites.net" + Config.REDIRECT_PATH,
    )