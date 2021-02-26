#!/usr/bin/env python3

shortMovieLines = open("movie_lines_short.txt", "w")


with open("movie_lines.txt", 'r', encoding='iso-8859-1') as f:

	head = [next(f) for x in range(3000)]

	for line in head:

		shortMovieLines.write(line)