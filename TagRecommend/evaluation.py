def getTrainUsers(train):
    """
    help function for recall and precision;
    record all the users in training set;
    return a list users_train;
    users_train: [user, user, user......]
    """
    users_train = []

    for item in train:
        user = item[1]
        if user not in users_train:
            users_train.append(user)

    return users_train


def getTestUsers(test):
    """
    help function for recall and precision;
    record all the users in test set;
    return a list users_test;
    users_test: [user, user, user......]
    """
    users_test = []

    for item in test:
        user = item[1]
        if user not in users_test:
            users_test.append(user)

    return users_test


def getUserItems():
    """
    help function for recall and precison;
    record the items a user tagged in test set;
    return a dict userItems;
    userItems: {user: [item, item, item...],
                user: [item, item, item...],
                ......}
    """
    userItems = {}

    for entry in test:
        user = entry[1]
        item = entry[2]

        if user not in userItems.keys():
            userItems[user] = []
            userItems[user].append(item)
        elif item in userItems[user]:
            pass
        else:
            userItems[user].append(item)

    return userItems


def Recall(train, test ,n):
    """
    calculate the recall of a particular algorithm;
    needs global variable users_train and users_test;
    return a number recall;
    """
    hit = 0
    all = 0

    for user in users_train:
        if user in users_test:

            recommendations = tagBased(user, n)

            for entry in recommendations:
                item = entry[0]

                #print "USER: "
                # print "--------“
                #print item
                # print type(item)
                #print "--------"

                #print userItems[user]
                # print type(userItems[user][0])
                #print "--------"
                #print ""

                if item in userItems[user]:
                    hit += 1
            all = all + len(userItems[user])

    print "hit: " + str(hit)
    print "all: " + str(all)

    return hit / (all * 1.0)


def Precision(train, test, n):
    """
    calculate the precision of a particular algorithm;
    needs global variable users_train and users_test;
    return a number precision;
    """
    hit = 0
    all = 0

    for user in users_train:
        if user in users_test:

            recommendations = tagBased(user, n)

            for entry in recommendations:
                item = entry[0]

                if item in userItems[user]:
                    hit += 1
            all = all + n

    print "hit: " + str(hit)
    print "all: " + str(all)

    return hit / (all * 1.0)