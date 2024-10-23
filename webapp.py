from maincode import create_app
application = create_app()
application.secret_key = 'Ef090694'

application.run(host='0.0.0.0', debug='True')
