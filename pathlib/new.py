from pathlib import Path

root_path = Path('/etc')
# Просто "делим" путь на его компоненты
full_path = root_path / 'nginx' / 'nginx.conf'

print(full_path) # /etc/nginx/nginx.conf
