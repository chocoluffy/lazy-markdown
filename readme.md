## Usage

run `python scripts.py source.md target.md` so that the script can detect the markdown format of image usage, and replace it with something else, for example:

given some structure like `![pool](http://ww1.sinaimg.cn/large/006tNc79gw1f9k6ilaabuj30hg0eo76b.jpg)`, the script will output its centered image md instance like: `<img src="http://ww1.sinaimg.cn/large/006tNc79gw1f9k6ilaabuj30hg0eo76b.jpg" style="display: block; margin: 0 auto;">`
