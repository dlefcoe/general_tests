

'''

example of recursive

'''
import os
import sys
import random
import matplotlib.pyplot as plt


sys.setrecursionlimit(10_000)

def main():
    ''' the main module '''

    random_path([100], 0.1, 1)
    return



def random_path(path:list, drift, diffuse):
    ''' a random path generated recursively '''

    r = random.uniform(-1, 1)
    
    path.append(path[-1] + drift + diffuse * r)
    # print(path[-1])

    # condition to finish recursion
    if len(path) > 1000:
        print('path finished at', path[-1])
        plot_data(path)
        return

    # take the next step in the random path    
    random_path(path, drift, diffuse)

    return

def plot_data(data):
    ''' plot some data '''

    plt.plot(data, color='magenta', marker='o',mfc='pink' )
    plt.xticks(range(0,len(data)+1, 1))
    plt.ylabel('path') #set the label for y axis
    plt.xlabel('steps') #set the label for x-axis
    plt.title("a random walk") #set the title of the graph
    # plt.show()

    # save the plot
    folder_path = os.path.dirname(__file__)
    file_name = 'random_walk.png'
    full_path = os.path.join(folder_path, file_name)
    plt.savefig(full_path)
    print('the plot is saved here:' , full_path)

    return



if __name__ == '__main__':
    main()
