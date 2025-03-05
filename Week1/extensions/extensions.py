filename = input("Type file: ")

new_file = filename.strip().lower()
if ".gif" in new_file:
    print("image/gif")
elif ".png" in new_file:
    print("image/png")
elif ".jpg" in new_file:
    print("image/jpeg")
elif ".pdf" in new_file:
    print("application/pdf")
elif ".jpeg" in new_file:
    print("image/jpeg")
elif ".zip" in new_file:
    print("application/zip")
elif ".txt" in new_file:
    print("text/plain")
else:
    print("application/octet-stream")

