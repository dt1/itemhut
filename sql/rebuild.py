import sys
import os
sys.path.append("/itemhut/pydb/")
import dbconn
import glob

def rebuild(fname):
    f = open(fname, 'r')
    sqlFile = f.read()
    f.close()
    
    # try:
    dbconn.cur.execute(sqlFile)

    dbconn.conn.commit()            
    # except:
    #     print("error", fname)


# rebuild('/itemhut/sql/ebay/categories/tables.sql')
# rebuild('/itemhut/sql/ebay/category_features/tables.sql')

# rebuild('/itemhut/sql/ebay/category_features/functions.sql')
# rebuild('/itemhut/sql/ebay/categories/functions.sql')


# rebuild('/itemhut/sql/ebay/categories/triggers.sql')
# rebuild('/itemhut/sql/ebay/category_features/triggers.sql')

# rebuild('/itemhut/sql/ebay/categories/insertions.sql')

# # rebuild('/itemhut/sql/ebay/orders/tables.sql')
# # rebuild('/itemhut/sql/ebay/orders/functions.sql')
# # rebuild('/itemhut/sql/ebay/orders/triggers.sql')

# rebuild('/itemhut/sql/global/products/products.sql')


# rebuild('/itemhut/sql/amazon/drop-schemas.sql')
# rebuild('/itemhut/sql/amazon/create-schemas.sql')
# rebuild('/itemhut/sql/amazon/constraint-tables/tables/nufiles/auto.sql')

for fname in glob.iglob('/itemhut/sql/amazon/constraint-tables/tables/*.sql'):
    rebuild(fname)
    
dbconn.cur.close()

print('success')




# ('error', '/itemhut/sql/amazon/constraint-tables/tables/food-service-jansan.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/video.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/office.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/coins.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/toys.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/shoes.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/sports.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/clothing.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/consumer-electronics.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/wireless.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/computers.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/pet-supplies.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/mechanical-fasteners.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/lab-supplies.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/food-beverages.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/home.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/music.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/home-improvement.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/power-transmission.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/auto.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/industrial.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/swvg.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/musical-instruments.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/beauty.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/cameras.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/raw-materials.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/amazon_auto.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/health.sql')
# ('error', '/itemhut/sql/amazon/constraint-tables/tables/jewelry.sql')
