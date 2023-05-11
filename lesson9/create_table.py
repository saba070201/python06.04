import pandas as pd
def create_data_frame(data1,data2,dates):
    s1=pd.Series(data1,name='source1_val')
    s2=pd.Series(data2,name='source2_val')
    s3=pd.Series(dates,name='dates')
    df=pd.DataFrame({s1.name:data1,s2.name:data2,s3.name:dates})
    return df