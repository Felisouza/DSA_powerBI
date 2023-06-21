import base64

with open(r"C:\Users\feh_s\OneDrive\Documentos\powerbiDSA\cap_08\tema\Fundos power BI.png", "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

print(encoded_image)

