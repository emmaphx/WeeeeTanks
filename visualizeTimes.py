import matplotlib.pyplot as plt

def logTime(time1, time2, file):
    with open(file, "a") as f:
        f.write(str(time1 - time2))
        f.write("\n")

def processTime(file):
    times = []
    with open(file, "r") as f:
        times = f.read().split("\n")
    
    return times

def makePlot(times):
    plt.plot(times)
    plt.ylabel('Time between frame in seconds')
    plt.show()



makePlot(processTime("times.txt"))