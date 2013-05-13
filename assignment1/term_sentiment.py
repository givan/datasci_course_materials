import sys

def calc_unknown_terms_sentiment(scores, tweet_file):
    print scores

def build_sent_dict(afinnfile_path):
    afinnfile = open(afinnfile_path)
    scores = []
    for i, line in enumerate(afinnfile):
		term, score = line.split("\t") # each line is tab del
		scores.append((term, int(score))) # convert the score to int
    return scores

def main():
	scores = build_sent_dict(sys.argv[1])
	tweet_file = open(sys.argv[2])
	calc_unknown_terms_sentiment(scores, tweet_file)

if __name__ == '__main__':
	main()
