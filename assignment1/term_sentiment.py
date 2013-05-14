import sys
import json

def calc_unknown_terms_sentiment(scores, tweet_file):
    # read tweet lines one by one
	# parse the line into a json object
	# test if 'text' is present
		# break down the 'text' field to words
		# for each word
			# probe if it is in the scores
			# if yes, add its score to the current tweet score
			# if not, add the term to the list of "unknown" terms for the current tweet
		# at this point, we have the set of unknown terms and the total tweet score
		# for each unknown phrase/word
			# look at the dictionary with unknown phrases
			# if found there add the current tweet score to the value
			# if not found add the current word to the dictionary having the value of the current tweet score
	
	# print the unknown word to sentiment score dictionary

	#print scores
	
	unknown_phrases = {}
	for tweet_line in tweet_file:
		tweet_sentiment = 0.0
		unknown_words = set()
		tweet_json = json.loads(tweet_line)
		if 'text' in tweet_json and tweet_json['text']:
			tweet_text = tweet_json['text']
			
			tweet_words = tweet_text.split() # split by whitespace only
			# print tweet_words
			for word in tweet_words:
				#print ascii_word
				if word in scores:
					tweet_sentiment += float(scores[word])
				elif word not in unknown_words:
					unknown_words.add(word)
			
			for	unknown_word in unknown_words:
				if unknown_word in unknown_phrases:
					unknown_phrases[unknown_word] += tweet_sentiment
				else:
					unknown_phrases[unknown_word] = tweet_sentiment
	
	for unknown_phrase, sentiment_value in unknown_phrases.items():
		print "%s %s"%(unknown_phrase, str(sentiment_value))

def build_sent_dict(afinnfile_path):
    afinnfile = open(afinnfile_path)
    scores = {}
    for i, line in enumerate(afinnfile):
		term, score = line.split("\t") # each line is tab del
		scores[term.decode('utf-8', 'ignore')] = float(score) # convert the score to int
    return scores

def main():
	scores = build_sent_dict(sys.argv[1])
	tweet_file = open(sys.argv[2])
	calc_unknown_terms_sentiment(scores, tweet_file)

if __name__ == '__main__':
	main()
