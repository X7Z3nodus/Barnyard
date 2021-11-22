import subprocess

print('ping www.python.org')
r = subprocess.call(('ping', 'www.python.org'))
print('Exit code:', r)