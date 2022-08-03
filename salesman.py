import random, numpy, math, copy, matplotlib.pyplot as plt
cities = [random.sample(range(100), 2) for x in range(10)];
tour = random.sample(range(10),10);
def dist (route):
    d = 0.0
    leng = len(route)
    for k in range(0,10):
        i = route[k]
        j = route[(k+1)%leng]
        d+= math.sqrt((cities[i][0]-cities[j][0])**2 + 
            (cities[i][1]-cities[j][1])**2)
    return(d)
print (tour)
for attempt in range(1000):
    [i,j] = sorted(random.sample(range(10),2));
    newTour =  tour[:i] + tour[j:j+1] +  tour[i+1:j] + tour[i:i+1] + tour[j+1:];
    olddist = dist(tour)
    newdist = dist(newTour)
    if newdist < olddist:
        tour = newTour
    if not attempt % 100==1:
        continue
    plt.plot([cities[tour[i % 10]][0] for i in range(11)], [cities[tour[i % 10]][1] for i in range(11)], 'xb-');
    plt.show()
print (("%.1f is length of winning tour " % newdist), tour)