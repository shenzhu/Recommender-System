from operator import itemgetter, attrgetter
from math import sqrt

def load_data():
	"""
	load movieLens data into program
	return two dicts, user_movie and movies
	user_movie: {userId: {userId: rating},
						 {userId: rating},
						 ......
				 userId: {userId: rating},
				 		 {userId: rating},
				 		 {userId: rating},
				 		 ......
				 ......}
	movies: {movieId: movieTitle,
			 movieId: movieTitle,
			 ......}
	"""
	filename_user_movie = 'data/u.data'
	filename_movieInfo = 'data/u.item'

	user_movie = {}
	for line in open(filename_user_movie):
		(userId, itemId, rating, timestamp) = line.strip().split('\t')
		user_movie.setdefault(userId, {})
		user_movie[userId][itemId] = float(rating)

	movies = {}
	for line in open(filename_movieInfo):
		(movieId, movieTitle) = line.split('|')[0：2]
		movies[movieId] = movieTitle

	return user_movie, movies

def average_rating(user):
	"""
	calculate the average rating of a user
	"""
	average = 0
	for u in user_movie[user].keys():
		average += user_movie[user][u]
	average = average * 1.0 / len(user_movie[user].keys())
	return average

def calUserSim(user_movie):

	"""
	build inverse table for movie_user
	movie_user: {movieId: [userId, userId, userId...],
				 movieId: [userId, userId, userId...],
				 ....... }
	"""
	movie_user = {}
	# loop over all the users
	for ukey in user_movie.keys():
		# loop over all the movies the user has rated
		for mkey in user_movie[ukey].keys():
			if mkey not in movie_user:
				movie_user[mkey] = []
			movie_user[mkey].append(ukey)

	"""
	calculate co-rated movies between users
	C: {userId: {userId: [itemId, itemId, itemId...]},
	            {userId: [itemId, itemId, itemId...]},
	            ......
	    userId: {userId: [itemId, itemId, itemId...]},
	            {userId: [itemId, itemId, itemId...]},
	            ......
	    ......}
	"""
	C = {}
	# loop over all the movies and users that rated them
	for movie, users in movie_user.item():
		# loop over all users that rated certain movie
		for u in users:
			C.setdefault(u, {})
			for n in users:
				if u == n:
					continue
				C[u].setdefault(n, [])
				C[u][n].append(movie)

	"""
	calculate user similairy (person correlation)
	userSim: {userId: {userId: 0},
	                  {userId: 0},
	                  ...
	          userId: {userId: 0},
	                  {userId: 0},
	                  ...
	          ......}
	"""
	userSim = {}
	for u in C.keys():
		for n in C[u].keys():
			userSim.setdefault(u, {})
			userSim[u].setdefault(n, 0)

			# average score of user
			average_u_rate = average_rating(u)
			average_n_rate = average_rating(n)

			part1 = 0
			part2 = 0
			part3 = 0

			# loop over the co-rated movies of u and n
			for m in C[u][n]:
				part1 += (user_movie[u][m] - average_u_rate) * (user_movie[n][m] - average_n_rate) * 1.0
				part2 += pow(user_movie[u][m] - average_u_rate, 2) * 1.0
				part3 += pow(user_movie[n][m] - average_n_rate, 2) * 1.0

			part2 = sqrt(part2)
			part3 = sqrt(part3)
			if part2 == 0:
				part2 = 0.001
			if part3 == 0:
				part3 == 0.001
			userSim[u][n] = part1 / (part2 * part3)
	return userSim

def getRecommendations(user, user_movie, movies, userSim, N):
	"""
	get the recommendations of certain user
	pred: {item: score,
		   item: score
		   ......}
    """
    interacted_items = user_movie[user].keys()
    average_u_rate = average_rating(user)
    sumUserSim = 0
    # loop over the most similar n users and its person correlation
    for n, nuw in sorted(userSim[user].items(), key = itemgetter(1), reverse = True)[0:N]:
    	average_n_rate = average_rating(n)

    	for i, nrating in user_movie[n].items():
    		# filter movies user interacted before
    		if i in interacted_items:
    			continue
    		pred.setdefault(i, 0)
    		pred[i] += nuw * (nrating - average_n_rate)
    	sumUserSim += nuw

    for i, rating in pred.items():
    	pred[i] = average_u_rate + (pred[i] * 1.0) / sumUserSim

    # top 10 pred
    pred = sorted(pred.items(), key = itemgetter(1), reverse = True)[0:10]
    return pred

# test
if __name__ = "__main__":
	# load data
	user_movie, movies = load_data()

	# calculate user similarity
	userSim = calUserSim(user_movie)

	# recommend
	pred = getRecommendations('100', user_movie, movies, userSim, 20)

	# display recommend result
	for i, rating in pred:
		print 'film: %s, rating: %s' % (movies[i], rating)


