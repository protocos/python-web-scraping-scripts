import pickledb

db = pickledb.load('example.db', False)
print db.get('test')
print db.getall()

db.set('key', 'value')
db.set('key2', ['value2', 'value3'])
db.dump()

test = db.get('key2')
print test


db.dump()