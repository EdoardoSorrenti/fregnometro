class Config:
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = variables.MAIL_USERNAME
    MAIL_PASSWORD = variables.MAIL_PASSWORD
    SECRET_KEY = variables.SECRET_KEY
    SQLALCHEMY_DATABASE_URI = variables.SQLALCHEMY_DATABASE_URI
