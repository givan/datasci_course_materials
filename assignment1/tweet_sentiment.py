import sys
import json

def find_single_sentiment_in_text(sentiment_data, text):
	total_sentiment = 0.0
	term = sentiment_data[0]
	score = sentiment_data[1]
	term_count = text.count(term)
	total_sentiment = term_count * score
	print "total_sentiment: %s, term: %s, score: %s, count: %s"%(str(total_sentiment), term, str(score), str(term_count))
	return total_sentiment

def find_sentiment_in_text(scores, text):
	# for each sentiment score
	#print text
	total_sentiment = 0.0
	idx = 0
	for i in range(len(scores)):
		total_sentiment += find_single_sentiment_in_text(scores[idx], text)
	
	return total_sentiment


def hw(scores, tweet_file):
    # read one tweet at a time
	# retrieve its text
	#result_sentiments = []
	for tweet_line in tweet_file:
		tweet_sentiment = 0.0
		#print tweet_line
		tweet_json = json.loads(tweet_line)
		if 'text' in tweet_json:
			tweet_text = tweet_json['text'].encode('utf-8') 
			tweet_sentiment = find_sentiment_in_text(scores, tweet_text)		
		#result_sentiments.append(tweet_sentiment)
		print tweet_sentiment

def hw2(scores, tweet_file):
    # read one tweet at a time
	# retrieve its text
	#result_sentiments = []
	idx = 0
	for tweet_line in tweet_file:
		tweet_sentiment = 0.0
		#print tweet_line
		tweet_json = json.loads(tweet_line)
		if 'text' in tweet_json:
			tweet_text = tweet_json['text'].encode('utf-8') 
			tweet_sentiment = find_single_sentiment_in_text(scores[idx], tweet_text)		
		#result_sentiments.append(tweet_sentiment)
		print tweet_sentiment

		
def lines(fp):
    print str(len(fp.readlines()))
	
def build_sent_dict(afinnfile_path):
    afinnfile = open(afinnfile_path)
    scores = []
    for i, line in enumerate(afinnfile):
		term, score = line.split("\t") # each line is tab del
		scores.append((term, int(score))) # convert the score to int
    return scores

	
def main():
    #sent_file = open(sys.argv[1])
	scores = build_sent_dict(sys.argv[1])
	tweet_file = open(sys.argv[2])
	hw2(scores, tweet_file)
    # lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
