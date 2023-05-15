from moralis import evm_api
from download_img import dwnld_img
import json

api_key = "iPdVjMpFEwfVyqwmRpliJkE6CMRH4CMc7Kn5OhzuRn8DyXLm2r6xcXHXrze4nnzw"

params = {
  "chain": "eth",
  "format": "decimal",
  "address": "0x4BB08998a697d0db666783Ba5B56E85B33ba262f",
  "token_id": "2"
}

result = evm_api.nft.get_nft_metadata(
  api_key=api_key,
  params=params,
)

# url_collection = result["token_uri"]

metadata = json.loads(result["metadata"])

url_image = metadata["image"]

protocol = url_image[:4]

url = ''

if protocol == 'ipfs':

  url_image_short = url_image[7:]

  # from download_img import dwnld_img
  
  url = url + f"https://ipfs.io/ipfs/{url_image_short}"

else:

  url = url + url_image

filename = "downloaded_image.png"

dwnld_img(url, filename