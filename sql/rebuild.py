import sys
import os
sys.path.append("/omark/pydb/")
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


# rebuild('/omark/sql/ebay/categories/tables.sql')
# rebuild('/omark/sql/ebay/category_features/tables.sql')

# rebuild('/omark/sql/ebay/category_features/functions.sql')
# rebuild('/omark/sql/ebay/categories/functions.sql')


# rebuild('/omark/sql/ebay/categories/triggers.sql')
# rebuild('/omark/sql/ebay/category_features/triggers.sql')

# rebuild('/omark/sql/ebay/categories/insertions.sql')

# # rebuild('/omark/sql/ebay/orders/tables.sql')
# # rebuild('/omark/sql/ebay/orders/functions.sql')
# # rebuild('/omark/sql/ebay/orders/triggers.sql')

# rebuild('/omark/sql/global/products/products.sql')


# rebuild('/omark/sql/amazon/drop-schemas.sql')
# rebuild('/omark/sql/amazon/create-schemas.sql')
# rebuild('/omark/sql/amazon/constraint-tables/tables/nufiles/auto.sql')

for fname in glob.iglob('/omark/sql/amazon/constraint-tables/tables/*.sql'):
    rebuild(fname)
    
dbconn.cur.close()

print('success')




# ('error', '/omark/sql/amazon/constraint-tables/tables/food-service-jansan.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/video.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/office.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/coins.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/toys.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/shoes.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/sports.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/clothing.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/consumer-electronics.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/wireless.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/computers.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/pet-supplies.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/mechanical-fasteners.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/lab-supplies.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/food-beverages.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/home.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/music.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/home-improvement.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/power-transmission.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/auto.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/industrial.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/swvg.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/musical-instruments.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/beauty.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/cameras.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/raw-materials.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/amazon_auto.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/health.sql')
# ('error', '/omark/sql/amazon/constraint-tables/tables/jewelry.sql')
