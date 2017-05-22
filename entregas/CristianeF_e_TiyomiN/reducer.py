import sys
var = []
current_word = None
current_count = 0
word = None
for line in sys.stdin:
    # remove leading and trailing whitespaces
    line = line.strip()
    # convert count (currently a string) to int
    try:
	# parse the input we got from mapper.py
        word, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
		var.append([current_word, current_count])
        current_count = count
        current_word = word
var=sorted(var, key=lambda x : x[1], reverse=True)
for n in var[:1500]:
	print ("%s\t%d" % (n[0], n[1]))

