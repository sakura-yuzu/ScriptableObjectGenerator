template = 'template.asset'
with open(template) as f:
    s = f.read()

datapath = 'data.csv'
with open(datapath) as f:
  l = f.readlines()

for row in l:
	sp = row.split(',')
	obj = s % tuple(sp)
	with open(f'dest/{sp[0]}.asset', mode='w') as f:
		f.write(obj)