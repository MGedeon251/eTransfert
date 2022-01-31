#fonction de hachage des elements données en entrée

import hashlib
hash_object = hashlib.sha256(b'4c9d3add053ab75fd4137746cb641201051acef76bebacaf1de092a04df1c9a5ca6b9062695445cc419e55b7b9d6bae0')
hex_dig = hash_object.hexdigest()
print(hex_dig)