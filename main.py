import requests

# TODO: Change this to use the ASCII art from one of these other sources:
# 1. Use GitHub API to get the art files from the hugomd/parrot.live project directly.
# 2. Add the art files to this repl.

# Either of the above options may make the animation faster.

url = 'http://parrot.live/'
# Service requires "curl" in User-Agent header
headers = {'User-Agent': 'curl'}

r = requests.get(url, headers=headers, stream=True)

# Using chunks of the same size as the frame may make the animation appear smoother.
# Frames are 18 lines of 50 characters, with space padding and newline (918 characters)
# Frames have 17 characters of terminal control sequences 
# Total characters per frame: 935
for chunk in r.iter_content(chunk_size=935):
  print(chunk.decode('ascii'), end='')
