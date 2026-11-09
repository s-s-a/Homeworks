import os

root_path = '/etc'
subfolder = 'nginx'
filename = 'nginx.conf'

full_path = os.path.join(root_path, subfolder, filename)
print(full_path) # /etc/nginx/nginx.conf
