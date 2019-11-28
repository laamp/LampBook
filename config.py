import os


class Config(object):
    SECRET_KEY = os.environ.get["SECRET_KEY"] or "you-will-never-guess"


# left off at explaining the secret key config variable
