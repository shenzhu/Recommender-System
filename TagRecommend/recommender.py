def tagBased(user, n):
    """
    get the recommendations for a particular user;
    return a list that holds turples, the first element of turple is url, the second element of turple is socre the url gets;
    recommendations:[(url, score), (url, score)......]
    """
    recommendations = {}

    # get the items and the times user tagged them, tagged_items is a dict
    tagged_items = user_items[user]

    for tag, wut in user_tags[user].items():
        for item, wti in tag_items[tag].items():
            # if items have been tagged, do not recommend them
            if item in tagged_items:
                continue
            if item not in recommendations:
                recommendations[item] = wut * wti
            else:
                recommendations[item] += wut * wti

    # sort recommendations
    recommendations = sorted(recommendations.iteritems(), key = lambda d:d[1], reverse = True)
    #recommendations = recommendations[0: n]

    # print recommendations

    return recommendations


def tagBasedTFIDF(user, n):
    """
    get the recommendations for a particular user;
    return a list that holds turples, the first element of turple is url, the second element of turple is score the url gets;
    recommendations: [(url, score), (url, score)......]
    """
    recommendations = {}

    tagged_items = user_items[user]

    for tag, wut in user_tags[user].items():
        for item, wti in tag_items[tag].items():
            if item in tagged_items:
                continue
            if item not in recommendations:
                recommendations[item] = wut * wti / log(1 + tagFre[tag])
            else:
                recommendations[item] += wut * wti / log(1 + tagFre[tag])

    recommendations = sorted(recommendations.iteritems(), key = lambda d:d[1], reverse = True)
    recommendations = recommendations[0:n]

    return recommendations


def tagBasedTFIDF2(user, n):
    """
    get the recommendations for a particular user;
    return a list that holds turples, the first element of turple is url, the second element of turple is score the url gets;
    recommendations: [(url, score), (url, score)......]
    """
    recommendations = {}

    tagged_items = user_items[user]

    for tag, wut in user_tags[user].items():
        for item, wti in tag_items[tag].items():
            if item in tagged_items:
                continue
            if item not in recommendations:
                recommendations[item] = wut * wti / (log(1 + tagFre[tag]) * log(1 + itemFre[item]))
            else:
                recommendations[item] += wut * wti / (log(1 + tagFre[tag]) * log(1 + itemFre[item]))

    recommendations = sorted(recommendations.iteritems(), key = lambda d:d[1], reverse = True)
    recommendations = recommendations[0:n]

    return recommendations
