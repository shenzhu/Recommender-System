from math import sqrt

critics = {'Lisa Rose':{'Lady in the Water':2.5,
                        'Snakes on a Plane':3.5,
                        'Just My Luck':3.0,
                        'Superman Returns':3.5,
                        'You, Me and Dupree':2.5,
                        'The Nighr Listener':3.0},
           'Gene Seymour':{'Lady in the Water':3.0,
                           'Snakes on a Plane':3.5,
                           'Just My Luck':1.5,
                           'Superman Returns':5.0,
                           'The Night Listener':3.0,
                           'You, Me and Dupree':3.6},
           'Michael Phillips':{'Lady in the Water':2.5,
                               'Snakes on a Plane':3.0,
                               'Superman Returns':3.5,
                               'The Night Listener':4.0},
           'Claudia Puig':{'Snakes on a Plane':3.5,
                           'Just My Luck':3.0,
                           'The Night Listener':4.5,
                           'Superman Returns':4.0,
                           'You, Me and Durpee':3.0},

           'Mick LaSalle':{'Lady in the Water':3.0,
                           'Snakes on a Plane':4.0,
                           'Just My Luck':2.0,
                           'Superman Returns':3.0,
                           'The Night Listener':3.0,
                           'You, Me and Dupree':2.0},
           'Jack Matthews':{'Lady in the Water':3.0,
                            'Snakes on a Plane':4.0,
                            'The Night Listener':3.0,
                            'Superman Returns':5.0,
                            'You, Me and Durpee':3.5,},
           'Toby':{'Snakes on a Plane':4.5,
                   'You, Me and Dupree':1.0,
                   'Superman Returns':4.0}
           }

#Euclidean Distance
def sim_distance(prefs, person1, person2):
    #get the list of shared_items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    #if they have nothing in common, return 0
    if len(si) == 0:
        return 0

    #compute the Euclidean distance
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]]
                         )

    return 1 / (1 + sqrt(sum_of_squares))

#Pearson Collretion Score
def sim_pearson(prefs, p1, p2):
    #get the shared item list
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    #get the numbers of their shared items:
    n = len(si)

    #if they have nothing in common, return 1
    if n == 0:
        return 1

    #sum all the prefs
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    #sum squared rating
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    #calculate Pearson Correlation Score
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0

    r = num / den

    return r

#get the top matchers of a particular person from the dictionary
def topMatches(prefs, person, n=5, similarity = sim_distance):
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]

    scores.sort()
    scores.reverse()

    return scores[0:n]

#recommend to someone based on utilizing the weigthed average of others
def getRecommendations(prefs, person, similarity = sim_distance):
    totals = {}
    simSums = {}

    for other in prefs:
        #do not compare with self
        if other == person: continue
        sim = similarity(prefs, person, other)

        #ignore situations when the evalution is smaller or equal to 0
        if sim <= 0: continue
        for item in prefs[other]:

            #only evaluate the item that haven't been seen
            if item not in prefs[person] or prefs[person][item] == 0:

                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim

                #sum of sim
                simSums.setdefault(item, 0)
                simSums[item] += sim

    rankings = [(total / simSums[item], item) for item, total in totals.items()]

    rankings.sort()
    rankings.reverse()

    return rankings
                

        

    
