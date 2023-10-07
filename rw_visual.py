import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random walk
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(25, 14))
    ax.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap="plasma", s=1, edgecolors="none")
    # ax.plot(rw.x_values, rw.y_values, linewidth=1, c="purple")
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.savefig("random_walk.png", bbox_inches="tight")
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
