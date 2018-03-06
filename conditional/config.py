from os import environ as env
from conditional import __version__

# Flask config
DEBUG = True if env.get("CONDITIONAL_DEBUG", "false").lower() == "true" else False
HOST_NAME = env.get("CONDITIONAL_HOST_NAME", "conditional.csh.rit.edu")
APP_NAME = "conditional"
IP = env.get("CONDITIONAL_IP", "0.0.0.0")
PORT = env.get("CONDITIONAL_PORT", 6969)

# DB Info
SQLALCHEMY_DATABASE_URI = env.get("SQLALCHEMY_DATABASE_URI", "")

# LDAP config
LDAP_RO = True if env.get("CONDITIONAL_LDAP_RO", "true").lower() == "true" else False
LDAP_BIND_DN = env.get("CONDITIONAL_LDAP_BIND_DN", "cn=conditional,ou=Apps,dc=csh,dc=rit,dc=edu")
LDAP_BIND_PW = env.get("CONDITIONAL_LDAP_BIND_PW", "")

# Sentry config
# Do not set the DSN for local development
SENTRY_CONFIG = {
    'dsn': env.get("CONDITIONAL_SENTRY_DSN", ""),
    'release': __version__,
}

# OIDC Config
OIDC_ISSUER = env.get("CONDITIONAL_OIDC_ISSUER", "https://sso.csh.rit.edu/auth/realms/csh")
OIDC_CLIENT_CONFIG = {
    'client_id': env.get("CONDITIONAL_OIDC_CLIENT_ID", "conditional"),
    'client_secret': env.get("CONDITIONAL_OIDC_CLIENT_SECRET", ""),
    'post_logout_redirect_uris': [env.get("CONDITIONAL_OIDC_CLIENT_LOGOUT", "http://0.0.0.0:6969/logout")]
}

# General config
DUES_PER_SEMESTER = env.get("CONDITIONAL_DUES_PER_SEMESTER", 80)
