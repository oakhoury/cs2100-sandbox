import matplotlib.pyplot as plt


def demo_bar_chart():
    x = [0, 1, 2]
    y1 = [3, 4, 3]
    y2 = [8, 9, 12]
    plt.bar(x, y1, color = "mediumpurple")
    plt.bar(x, y2, bottom = y1, color ="gold")
    # bottom is a way to achieve stacked bar plots
    # Color choices, see: https://matplotlib.org/stable/gallery/color/named_colors.html

    plt.show()



def demo_histogram():
    scores = [52, 58, 61, 40, 81, 65, 67, 68, 68, 70,
            71, 72, 72, 73, 74, 74, 75, 76, 77, 78,
            79, 80, 82, 83, 85, 86, 88, 91, 94, 98]

    fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))

    axes[0].hist(scores, bins = 3, color='darkgray')
    axes[0].set(title="3 bins, Pyplot determines boundaries")

    axes[1].hist(scores, bins=[50, 60, 70, 80, 90, 100], color='royalblue', edgecolor="white")
    axes[1].set(title="5 bins, defined by explicit boundaries")

    axes[2].hist(scores, bins = 15, color='lightgreen')
    axes[2].set(title="15 bins, Pyplot determines boundaries")

    for plot in axes:
        plot.set(xlabel="Exam score", ylabel="Number of students")

    fig.savefig('figures/histograms.png')

    plt.show()

def main():
    # demo_bar_chart()
    demo_histogram()

if __name__ == '__main__':
    main()
