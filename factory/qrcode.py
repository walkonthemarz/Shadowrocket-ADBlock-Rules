import urllib.parse

with open('../README.template.md', 'r') as file:
    content = file.read()

qr_service_endpoint = 'https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='
content = content.replace('{{qr_service_endpoint}}', qr_service_endpoint)

github_raw_content_endpoint = 'https://raw.githubusercontent.com/walkonthemarz/Shadowrocket-ADBlock-Rules/master/'
content = content.replace('{{github_raw_content_endpoint}}', github_raw_content_endpoint)

url_encoded_github_raw_content_endpoint = urllib.parse.quote(github_raw_content_endpoint, safe='')
content = content.replace('{{url_encoded_github_raw_content_endpoint}}', url_encoded_github_raw_content_endpoint)

with open('../README.md', 'w') as file:
    file.write(content)
