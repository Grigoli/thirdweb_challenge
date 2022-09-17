from eth_account import Account
from thirdweb import ThirdwebSDK
from thirdweb.types.nft import NFTMetadataInput
from thirdweb.types.settings.metadata import NFTCollectionContractMetadata
from config import PRIVATE_KEY


class NFT_Service:

    def __init__(self):
        # Instantiate a new signer to pass into the SDK
        self.signer = Account.from_key(PRIVATE_KEY)

        # Create a new instance of the SDK to use
        self.sdk = ThirdwebSDK("rinkeby", self.signer)

    def createCollection(self, data):

        collectionAddress = self.sdk.deployer.deploy_nft_collection(
            NFTCollectionContractMetadata.from_json(data)
        )

        return {"NFT Collection Address": collectionAddress}

    def getMetadatasOfNFTs(self, nft_collection_address):

        metadatas = []

        contract = self.sdk.get_nft_collection(nft_collection_address)

        nfts = contract.get_all()

        for nft in nfts:
            metadatas.append(nft.metadata.__dict__)

        return metadatas

    def mintNFT(self, nft_collection_address, data):
        
        nft_collection = self.sdk.get_nft_collection(nft_collection_address)

        # Now you can use any of the SDK contract functions including write functions
        details = nft_collection.mint(NFTMetadataInput.from_json(data))

        return {
            "Minted NFT Transaction: ": details.receipt.transactionHash.hex()
        }
