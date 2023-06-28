import base64

with open(r"C:\Users\feh_s\DSA_powerBI\DSA_powerBI\cap_10\tema\Fundos power BI.png", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

print(type(encoded_image))

# try:
# #    file_content=base64.b64decode(encoded_image)
#    with open(r"C:\Users\feh_s\DSA_powerBI\DSA_powerBI\cap_10\tema\encoded-20230627141819.txt", "rb") as f:
#         f.write(encoded_image)
# except Exception as e:
#    print(str(f'Deu errado: {e}'))

try:
    text_file = open(r"C:\Users\feh_s\DSA_powerBI\DSA_powerBI\cap_10\tema\encoded-20230627141819.txt", "w")
    n = text_file.write(encoded_image)
    text_file.close()
except Exception as e:
    print(str(e))

# print(encoded_image)

