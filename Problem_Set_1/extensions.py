fileName = input("File name: ").lower().strip()

if fileName.endswith(".gif"):
    print("image/gif")
elif fileName.endswith(".jpg"):
    print("image/jpeg")
elif fileName.endswith(".jpeg"):
    print("image/jpeg")
elif fileName.endswith(".png"):
    print("image/png")
elif fileName.endswith(".pdf"):
    print("application/pdf")
elif fileName.endswith(".txt"):
    print("text/plain")
elif fileName.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
