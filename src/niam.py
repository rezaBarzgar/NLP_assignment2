import matplotlib.pyplot as plt


def plotKs(n, ks):
    plt.title(f"{n}-gram figure")
    for values, title in ks:
        plt.plot([i for i in range(len(k1))], values, label=title)
    plt.legend()
    plt.savefig(fname=f"{n}-gram.png", format="png")
    plt.cla()

if __name__ == '__main__':
    with open("src/output.txt", "r") as f:
        lines = f.readlines()
        ary = None
        k1, k5, k10, kall = [],[],[],[]
        current_gram = 1
        for i, l in enumerate(lines):
            if i % 6 == 0:
                if i == len(lines) - 1:
                    plotKs(last_gram, [
                        (k1, "k at 1"),
                        (k5, "k at 5"),
                        (k10, "k at 10"),
                        (kall, "k at all"),
                    ])
                    continue
                ary = l[0]
                if 48 <= ord(l[1]) <= 57:
                    ary += l[1]
                last_gram = current_gram
                current_gram = int(ary)
                if last_gram != current_gram:
                    plotKs(last_gram, [
                        (k1, "k at 1"),
                        (k5, "k at 5"),
                        (k10, "k at 10"),
                        (kall, "k at all"),
                    ])
                    k1, k5, k10, kall = [],[],[],[]
            elif i % 6 == 1: # 1
                k1.append(float(l.split(" ")[-1]))
            elif i % 6 == 2: # 10
                k10.append(float(l.split(" ")[-1]))
            elif i % 6 == 3: # 5
                k5.append(float(l.split(" ")[-1]))
            elif i % 6 == 4: # all
                kall.append(float(l.split(" ")[-1]))
            elif i % 6 == 5: # refresh
                continue
