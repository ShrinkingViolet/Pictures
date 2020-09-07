from PIL import Image
import os
import math
def convert(name):
    img = Image.open('origin/' + name).convert('RGB')
    hei, wid = img.size
    diag = math.sqrt(hei * hei + wid * wid)
    max_size = 800
    if diag <= max_size:
        pass
    else:
        rate = max_size / diag
        img.thumbnail((hei * rate, wid * rate))
    img.save('midsize/' + name.split('.')[0] + '_md.jpg')
# main
with open('datebase.qwq', 'r') as f:
    datebase = f.read().split(';')
if datebase[-1] == '':
    datebase.pop()
for i, j, k in os.walk('origin'):
    for l in k:
        if l.split('.')[0] in datebase:
            continue
        try:
            convert(l)
            datebase.append(l.split('.')[0])
            print(l)
        except:
            print('convert failed: ' + l)
with open('datebase.qwq', 'w') as f:
    for i in datebase:
        f.write(i + ';')
with open('index.html', 'w') as f:
    wt = ''
    for i in datebase:
        wt = '''
        <div class="entry" onclick="window.open('origin/''' + i + '''.jpg')">
            <img src="midsize/''' + i + '''_md.jpg">
        </div>
        ''' + wt
    with open('index.html.tmp', 'r') as t:
        f.write(t.read().replace('$$--$$', wt))
