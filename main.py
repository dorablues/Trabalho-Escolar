#   main.py

#   import
from interface import *
from connection import Database
#   vaiable
reg=('Julia',25,'Rua B',225)
#   code
db=Database('dataBase.db'); db.new('CAD'); db.status()
db.insert('CAD',reg)

db.consulte('CAD',1)
db.consulte.read()