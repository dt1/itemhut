import sys
sys.path.append("/omark/pydb/")
import dbconn


def rebuild(fname):
    f = open(fname, 'r')
    sqlFile = f.read()
    f.close()

    try:
        dbconn.cur.execute(sqlFile)
        dbconn.conn.commit()            
    except:
        print("error", fname)


rebuild('/omark/sql/ebay/categories/tables.sql')
rebuild('/omark/sql/ebay/category_features/tables.sql')

rebuild('/omark/sql/ebay/category_features/functions.sql')
rebuild('/omark/sql/ebay/categories/functions.sql')


rebuild('/omark/sql/ebay/categories/triggers.sql')
rebuild('/omark/sql/ebay/category_features/triggers.sql')

rebuild('/omark/sql/ebay/categories/insertions.sql')

# rebuild('/omark/sql/ebay/orders/tables.sql')
# rebuild('/omark/sql/ebay/orders/functions.sql')
# rebuild('/omark/sql/ebay/orders/triggers.sql')

rebuild('/omark/sql/global/products/products.sql')

dbconn.cur.close()

print('success')
