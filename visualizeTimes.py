import matplotlib.pyplot as plt

def logTime(time1, time2, file):
    with open(file, "a") as f:
        f.write(str(time1 - time2))
        f.write("\n")


def makePlot(times):
    intTimes = []
    ymin = float(0)
    ymax = float(0)
    for x in times:
        try:
            tmp = float(x)
            if (tmp > ymax): 
                ymax = tmp
            if (tmp < ymin): 
                ymin = tmp
            intTimes.append(tmp)
        except ValueError as e:
            pass
    plt.ylabel('Time between frame in seconds')
    ax = plt.gca()
    ax.set_ylim([ymin, ymax])
    plt.plot(intTimes)
    plt.show()

def processTime(file):
    times = []

    try:
        with open(file, "r") as f:
            times = f.read().split("\n")
    except FileNotFoundError as e:
        pass
    
    return times

makePlot(processTime("times.txt"))
