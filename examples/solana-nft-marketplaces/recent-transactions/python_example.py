from theblockchainapi import TheBlockchainAPIResource
import json

# Get an API key pair for free here: https://dashboard.blockchainapi.com/
MY_API_KEY_ID = None
MY_API_SECRET_KEY = None

BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)


def example():
    try:
        assert MY_API_KEY_ID is not None
        assert MY_API_SECRET_KEY is not None
    except AssertionError:
        raise Exception("Fill in your key ID pair!")

    # This pulls all the NFT transactions for the last 30 minutes.
    result = BLOCKCHAIN_API_RESOURCE.get_recent_nft_transactions()
    print(json.dumps(result, indent=4))


if __name__ == '__main__':
    example()