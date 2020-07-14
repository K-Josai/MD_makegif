import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure(figsize=(10, 10))


def update(i, x, y, LCEL):
    if i != 0:
        plt.cla()                      # 現在描写されているグラフを消去

    plt.xlim(0, LCEL)
    plt.ylim(0, LCEL)
    plt.scatter(x[i], y[i], c='blue', marker='o')
    plt.title('i=' + str(i))


def main():
    df2 = pd.read_csv("tekitou.txt", delim_whitespace=True,
                      header=None, skiprows=lambda x: x not in [1])
    NATOM, NRHO, NCYCLE, NPRINT = df2.values[0]
    NATOM = int(NATOM)
    NCYCLE = int(NCYCLE)
    NPRINT = int(NPRINT)
    LCEL = np.sqrt(float(NATOM/NRHO))  # Box Size
    df = pd.read_csv(
        "tekitou.txt", delim_whitespace=True, header=None, skiprows=2)
    data_kari = df.values
    x = data_kari[0::2]
    y = data_kari[1::2]
    ani = animation.FuncAnimation(
        fig, update, fargs=(x, y, LCEL), interval=5, frames=(NCYCLE//NPRINT))
    ani.save("MD_test.gif", writer="imagemagick")


def test():
    df2 = pd.read_csv("tekitou.txt", delim_whitespace=True,
                      header=None, skiprows=lambda x: x not in [1])
    data2 = df2.values
    x = data2[0][1]
    print(x)


if __name__ == "__main__":

    main()
