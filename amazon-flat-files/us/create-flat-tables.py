#!/usr/bin/python2

import pandas as pd
import sys

pfile = str(sys.argv[1])
sname = str(sys.argv[2])


x2 = pd.ExcelFile(pfile)
x2 = x2.parse('Valid Values')

aa = []
for i in x2.itertuples():
    aa.append(i)

for j in aa[0]:
    if j != 0:
        print(
'''
create table {0}.valid_{1} (
     {1} varchar
);'''.format(sname, j))

# d = {}
# for j in aa[0][1:]:
#     d[j] = []

# print(d)

# for k in aa:
#     if type(k[1:][0]) != float:
#         print(k[1:])
    
# dir(x2)                         # 
 # 'abs', 'add', 'add_prefix', 'add_suffix', 'align', 'all', 'any', 'append', 'apply', 'applymap', 'as_blocks', 'as_matrix', 'asfreq', 'astype', 'at', 'at_time', 'axes', 'between_time', 'bfill', 'blocks', 'bool', 'boxplot', 'clip', 'clip_lower', 'clip_upper', 'columns', 'combine', 'combineAdd', 'combineMult', 'combine_first', 'compound', 'consolidate', 'convert_objects', 'copy', 'corr', 'corrwith', 'count', 'cov', 'cummax', 'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 'dot', 'drop', 'drop_duplicates', 'dropna', 'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'eval', 'ffill', 'fillna', 'filter', 'first', 'first_valid_index', 'floordiv', 'from_csv', 'from_dict', 'from_items', 'from_records', 'ftypes', 'ge', 'get', 'get_dtype_counts', 'get_ftype_counts', 'get_value', 'get_values', 'groupby', 'gt', 'head', 'hist', 'iat', 'icol', 'idxmax', 'idxmin', 'iget_value', 'iloc', 'index', 'info', 'insert', 'interpolate', 'irow', 'is_copy', 'isin', 'isnull', 'iteritems', 'iterkv', 'iterrows', 'itertuples', 'ix', 'join', 'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'load', 'loc', 'lookup', 'lt', 'mad', 'mask', 'max', 'mean', 'median', 'memory_usage', 'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 'ndim', 'ne', 'notnull', 'pct_change', 'pivot', 'pivot_table', 'plot', 'pop', 'pow', 'prod', 'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 'reindex', 'reindex_axis', 'reindex_like', 'rename', 'rename_axis', 'reorder_levels', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rpow', 'rsub', 'rtruediv', 'save', 'select', 'select_dtypes', 'sem', 'set_axis', 'set_index', 'set_value', 'shape', 'shift', 'size', 'skew', 'slice_shift', 'sort', 'sort_index', 'sortlevel', 'squeeze', 'stack', 'std', 'sub', 'subtract', 'sum', 'swapaxes', 'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dense', 'to_dict', 'to_excel', 'to_gbq', 'to_hdf', 'to_html', 'to_json', 'to_latex', 'to_msgpack', 'to_panel', 'to_period', 'to_pickle', 'to_records', 'to_sparse', 'to_sql', 'to_stata', 'to_string', 'to_timestamp', 'to_wide', 'transpose', 'truediv', 'truncate', 'tshift', 'tz_convert', 'tz_localize', 'unstack', 'update', 'values', 'var', 'where', 'xs']
