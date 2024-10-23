import pandas as pd

def create_test_data():
    # Creating two sample DataFrames
    data1 = {
        'ID': [1, 2, 3, 4],
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40]
    }

    data2 = {
        'ID': [3, 4, 5, 6],
        'Name': ['Charlie', 'David', 'Eve', 'Frank'],
        'Age': [35, 40, 45, 50]
    }

    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    
    return df1, df2

def compare_datasets(df1, df2):
    # Finding differences
    diff1 = df1[~df1.apply(tuple, 1).isin(df2.apply(tuple, 1))]
    diff2 = df2[~df2.apply(tuple, 1).isin(df1.apply(tuple, 1))]

    print("Differences in Dataset 1:")
    print(diff1)
    print("\nDifferences in Dataset 2:")
    print(diff2)

if __name__ == "__main__":
    df1, df2 = create_test_data()
    compare_datasets(df1, df2)


'''
Output :
Differences in Dataset 1:
   ID   Name  Age
0   1  Alice   25
1   2    Bob   30

Differences in Dataset 2:
   ID   Name  Age
2   5    Eve   45
3   6  Frank   50
'''
