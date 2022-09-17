from flask import Flask, current_app

from flask_restx import Api


from werkzeug.middleware.proxy_fix import ProxyFix


from controller.NFT_Controller import api_nft as nftapi


app = Flask(__name__)
app.app_context().push()
app.wsgi_app = ProxyFix(app.wsgi_app)

authorizations = {
    'Basic Auth': {
        'type': 'basic',
        'in': 'header',
        'name': 'Authorization'
    }
}



api = Api(app,
        version='1.0',
        title='NFT API',
        description='A simple NFT API to deploy a thirdweb NFT Collection contract and interact with it.',
        authorizations=authorizations)



api.add_namespace(nftapi, path='/nft')



if __name__ == '__main__':
    app.run(debug=True)
