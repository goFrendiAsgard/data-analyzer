import sys
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    filepath = sys.argv[1] if len(sys.argv) > 1 else 'data.csv'
    hue = sys.argv[2] if len(sys.argv) > 2 else None
    sep = sys.argv[3] if len(sys.argv) > 3 else ','
    delimiter = sys.argv[4] if len(sys.argv) > 4 else None
    df = pd.read_csv(filepath, sep=sep, delimiter=delimiter)
    if hue is None:
        hue = df.columns[-1]
    sns.pairplot(df, hue=hue)
    plt.show()
