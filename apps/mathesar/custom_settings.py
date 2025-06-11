# config/settings/custom_settings.py

# Import all settings from Mathesar's default production settings
# This is crucial to avoid breaking their existing configuration.
# Ensure this path is correct relative to Django's module search path.
# Assuming config.settings.production is accessible.
import os
from config.settings.production import *  # type: ignore

# Add 'storages' and 'oidc_auth' to your INSTALLED_APPS
# Check if INSTALLED_APPS is a tuple/list and append.
INSTALLED_APPS = list(INSTALLED_APPS) + ["storages", "oidc_provider"]  # type: ignore

# --- S3 Settings (as before) ---
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME")
AWS_DEFAULT_ACL = os.environ.get("AWS_DEFAULT_ACL", None)
AWS_QUERYSTRING_AUTH = os.environ.get("AWS_QUERYSTRING_AUTH", "False").lower() in (
    "true",
    "1",
    "t",
)
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# --- OIDC Settings ---
# Replace these with your OIDC provider's details.  Use environment variables for sensitive data.
OIDC_RP_CLIENT_ID = os.environ.get("OIDC_RP_CLIENT_ID")
OIDC_RP_CLIENT_SECRET = os.environ.get("OIDC_RP_CLIENT_SECRET")
OIDC_RP_ISSUER_OP = os.environ.get(
    "OIDC_RP_ISSUER_OP"
)  # The base URL of your OIDC provider
OIDC_RP_REDIRECT_URI = os.environ.get(
    "OIDC_RP_REDIRECT_URI"
)  # Adjust to your Mathesar's callback URL
OIDC_RP_SCOPES = os.environ.get(
    "OIDC_RP_SCOPES", "openid email profile"
)  # Adjust scopes as needed
OIDC_RP_VERIFY_SSL = os.environ.get("OIDC_RP_VERIFY_SSL", "True").lower() in (
    "true",
    "1",
    "t",
)


# Add OIDC authentication backend (and potentially remove others)
try:
    AUTHENTICATION_BACKENDS = list(AUTHENTICATION_BACKENDS) + [  # type: ignore
        "oidc_auth.authentication.OIDCAuthenticationBackend"
    ]
except NameError:
    AUTHENTICATION_BACKENDS = [
        "oidc_auth.authentication.OIDCAuthenticationBackend",
    ]

# Redirect all users to the login page
LOGIN_URL = "/oidc/login/"
LOGIN_REDIRECT_URL = "/"  # Where to redirect after successful login
