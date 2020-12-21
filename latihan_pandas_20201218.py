# Tanggal 18 Desember 2020

import numpy as np
import pandas as pd

# Membaca data excel
data_df = pd.read_csv('exams.csv')

# Menunjukkan jumlah baris data
len_df = len(data_df)
print(len_df)

# Menunjukkan baris dan kolom data
dim_df = data_df.shape
print(dim_df)

# Menunjukkan data teratas 
df_atas = data_df.head()
# Menunjukkan data terbawah
df_bawah = data_df.tail()

# Untuk melihat tipe data
tipe_data = data_df.info()

# statistika data
stat_data = data_df.describe()
print(stat_data)

# Exploring data set
data_gender = data_df["gender"].value_counts()
print(data_gender)
data_race = data_df["race/ethnicity"].value_counts()
print(data_race)
data_parented = data_df["parental level of education"].value_counts()
print(data_parented)
data_lunch = data_df["lunch"].value_counts()
print(data_lunch)
data_test = data_df["test preparation course"].value_counts()
print(data_test)
data_math = data_df["math score"].value_counts()
print(data_math)
data_read = data_df["reading score"].value_counts()
print(data_read)
data_write = data_df["writing score"].value_counts()
print(data_write)

#melihat score max dari siswa female dan male
max_female_math = data_df.loc[data_df["gender"]=="female", "math score"].max()
# cara lain
#max_female_math = data_df[data_df["gender"]=="female"]["math score"].max()
print(max_female_math)
max_female_reading = data_df.loc[data_df["gender"]=="female", "reading score"].max()
print(max_female_reading)
max_female_writing = data_df.loc[data_df["gender"]=="female", "writing score"].max()
print(max_female_writing)
max_male_math = data_df.loc[data_df["gender"]=="male", "math score"].max()
print(max_male_math)
max_male_reading = data_df.loc[data_df["gender"]=="male", "reading score"].max()
print(max_male_reading)
max_male_writing = data_df.loc[data_df["gender"]=="male", "writing score"].max()
print(max_male_reading)

#buat index diganti dengan gender
data_dfnew = data_df.set_index('gender')

# Menunjukkan sisa kolom
sisa_kolom = data_dfnew.axes[1]

#ambil data row pertama
data_dfnew.iloc[0]
data_dfnew.loc["female"]


# Soal nomor 2
# Nilai Matematika
min_female_math = data_df[data_df["gender"]=="female"] ["math score"].min()
male_lessthan_female_math = data_df[(data_df["gender"] == "male") & (data_df["math score"]< min_female_math)]
male_parented_math = male_lessthan_female_math["parental level of education"].value_counts()
male_race_math = male_lessthan_female_math["race/ethnicity"].value_counts()


# Nilai Reading
min_female_read = data_df[data_df["gender"]=="female"] ["reading score"].min()
male_lessthan_female_read = data_df[(data_df["gender"] == "male") & (data_df["reading score"]< min_female_read)]
male_parented_read = male_lessthan_female_read["parental level of education"].value_counts()
male_race_read = male_lessthan_female_read["race/ethnicity"].value_counts()

# Nilai Writing
min_female_write= data_df[data_df["gender"]=="female"] ["writing score"].min()
male_lessthan_female_write= data_df[(data_df["gender"] == "male") & (data_df["writing score"]< min_female_write)]
male_parented_write = male_lessthan_female_write["parental level of education"].value_counts()
male_race_write = male_lessthan_female_write["race/ethnicity"].value_counts()


# Soal nomor 1
data_female = data_df[data_df["gender"]=="female"] 
data_female_math = data_female[(data_female["math score"] <60) & (data_female["math score"] > 50)]
data_female_math = data_female_math[data_female['parental level of education'].str.endswith("degree")]
