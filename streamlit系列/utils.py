import pandas as pd
import numpy as np
import pandas.api.types  as pd_types


def get_cat_col_infos(df:pd.DataFrame):
    
    for col in df.columns:
        if pd_types.is_object_dtype(df[col]):
            dup_value = df[col].drop_duplicates()
            yield col,dup_value