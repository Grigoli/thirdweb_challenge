from flask_restx import Api, Resource, Namespace, fields
from auth import auth

from service.NFT_Service import NFT_Service

api_nft = Namespace('NFT', description='NFT Operations')

nft_metadata = api_nft.model('nft_metadata', {
    'name': fields.String(required=True, description='The name of the NFT'),
    'description': fields.String(required=False, description='The optional description of the NFT'),
    'image': fields.String(required=False, description='The optional image of the NFT'),
    'external_url': fields.String(required=False, description='The optional external URL of the NFT'),
    'animation_url': fields.String(required=False, description='The optional animation URL of the NFT'),
    'background_color': fields.String(required=False, description='The name of the NFT'),
    'properties': fields.Raw(required=False, description='The optional properties of the NFT'),
    'attributes': fields.Raw(required=False, description='The optional attributes of the NFT'),
})

nft_collection_contract_metadata = api_nft.model('nft_collection_contract_metadata', {
    'name': fields.String(required=True, description='The name of the NFT Collection'),
    'primary_sale_recipient': fields.String(required=True, description='The name of the primary sale recipient'),
    'description': fields.String(required=False, description='The optional description of the NFT Collection'),
    'image': fields.String(required=False, description='The optional image of the NFT Collection'),
    'external_url': fields.String(required=False, description='The optional external URL of the NFT Collection'),
    'seller_fee_basis_points': fields.Integer(required=False, description=' Define how much % you want from secondary market sales 1000 = 10%'),
    'symbol': fields.String(required=False, description='The name of the NFT'),
    'platform_fee_basis_points': fields.Integer(required=False, description='Advanced configuration - platform fees'),
    'platform_fee_recipient': fields.String(required=False, description='Advanced configuration - Recipient Address'),
    'trusted_forwarders': fields.List(fields.String(required=False, description='Custom gasless trusted forwarder addresses'))

})

@api_nft.route("/collection")
class NFT_Collection_Controller(Resource):
    @api_nft.doc('Authenticated users can deploy new NFT Collection contracts')
    @api_nft.doc(security='Basic Auth')
    @api_nft.expect(nft_collection_contract_metadata)
    @auth.login_required
    def post(self):
        '''Create NFT Collection'''
        data = api_nft.payload
        return NFT_Service().createCollection(data), 201


@api_nft.route("/collection/<nft_collection_address>")
class NFT_Collection_Controller_Get(Resource):
    @api_nft.doc('Get the metadata of all tokens in the contract')
    def get(self, nft_collection_address):
        '''Get the metadata of all tokens in the contract'''
        return NFT_Service().getMetadatasOfNFTs(nft_collection_address)


@api_nft.route("/mint/<nft_collection_address>")
class NFT_Controller(Resource):
    @api_nft.doc('Authenticated users can mint NFTs with metadata on a deployed NFT Collection contract')
    @api_nft.doc(security='Basic Auth')
    @api_nft.expect(nft_metadata)
    @auth.login_required
    def post(self, nft_collection_address):
        '''Mint NFT on a deployed NFT Collection contract'''
        data = api_nft.payload
        return NFT_Service().mintNFT(nft_collection_address, data)
