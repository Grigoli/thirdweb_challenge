# thirdweb_challenge
The challenge for Thirdweb

## Description
This app is built in Python Flask. Using Thirdweb sdk to deploy a thirdweb NFT Collection contract and interact with it. For demo purposes this project uses rinkeby network. Below I have included instructions to create and configure wallet to the Rinkeby test network.


## Installation
To install dependencies, navigate to your `src` directory on your command line and issue the following commands:

```shell
pip3 install -r requirements.txt
# If the above command doesn't work, try one of the commands below:
# py -m pip install -r requirements.txt
# python3 -m pip install -r requirements.txt
# python -m pip install -r requirements.txt
```

## Wallet Configuration
Set up a MetaMask wallet account. https://metamask.zendesk.com/hc/en-us/articles/360015489531-Getting-started-with-MetaMask
Configure your MetaMask wallet to the Rinkeby test network. 
Connect your wallet to request free funding on the Rinkeby network. https://faucets.chain.link/


## Running your Flask Server

Before running app config.py needs to be updated with a private key of your wallet. 

### On Mac / Linux
```shell
# venv
python3 -m venv venv
. venv/bin/activate

export FLASK_APP=src/app.py
export FLASK_ENV=development
flask run
```

### On Windows
```shell
set FLASK_APP=src/app.py
set FLASK_ENV=development
flask run
# alternative commands to try if "flask run" doesn't work:
# py -m flask run
# python3 -m flask run
# python -m flask run
```

<img width="1461" alt="image" src="https://user-images.githubusercontent.com/34671779/190838884-09535f92-edde-4a7f-abc0-a1bbb6bef04b.png">


## Demo


### Create NFT Collection
```
POST /nft/collection

this method takes following payload 
```
<img width="690" alt="image" src="https://user-images.githubusercontent.com/34671779/190838995-eadd5c1e-c78b-4f27-8b44-ab8fe4c7d820.png">

```
and returns NFT Collection Address
```



### Get the metadata of all tokens in the contract
```
GET /nft/collection/{nft_collection_address}

this method takes NFT Collection Address
and returns a list of metadatas of NFTs
```


### Mint NFT on a deployed NFT Collection contract
```
POST /nft/mint/{nft_collection_address}

this method takes NFT Collection Address parameter and following payload 
```
<img width="455" alt="image" src="https://user-images.githubusercontent.com/34671779/190839126-78f98068-7072-47ef-91ca-b552048e8c2c.png">

```
and returns Minted NFT Transaction Hash
```




