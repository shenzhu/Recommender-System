def getRecommendations(user):
    recommend_items = {}
    tagged_items = user_items[user]

    # tag and wut stands for the tags and times of the tag that the user rated  
    for tag, wut in user_tags[user].items():
	for item, wti in tag_items[tag].items():
            # if items have been tagged, do not recommend them                  
            if item in tagged_items:
                continue
            if item not in recommend_items:
		recommend_items[item] = wut * wti
            else:
	        recommend_items[item] += wut * wti

    return recommend_items

