import hashlib

# text = "Hello World !"
# hash_object = hashlib.sha256(text.encode())
# hash_digest = hash_object.hexdigest()
# print(hash_digest)

def hashfile(filepath):
    h=hashlib.new("sha256")
    with open(filepath,"rb") as file:
        while True:
            chunk=file.read(1024)
            if chunk==b"":
                break
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    print(hashfile("check.txt"))