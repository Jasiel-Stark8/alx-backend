import requests
import csv

url = 'https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240103%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240103T121321Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d3d79bd7eb76bf94218b2fe903c84046bc31846cebd3d93c41b9bda3f0d9a2da'

response = requests.get(url)

if response.status_code == 200:
    with open('Popular_Baby_Names.csv', 'w', newline='', encoding='utf-8') as f:
        file = f.write(response.text)
