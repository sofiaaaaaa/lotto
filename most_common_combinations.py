#!/usr/bin/env python

import sys
import csv
from itertools import combinations
from collections import defaultdict

if len(sys.argv) > 1:
  file = sys.argv[1]
else:
  file = "lottos_615.csv"

class LottoCounter:
  counters = {}

  def processrow(self, row):
    for i in range(2, len(row)+1):
      for c in combinations(row, i):
        self.processcombination(tuple(sorted(c)))

  def processcombination(self, c):
    self.counters.setdefault(len(c), defaultdict(int))[c] += 1

  def printcommon(self):
    for k in sorted(self.counters, reverse=True):
      print("\nMost common {} number combinations:\n".format(k))
      counter = self.counters[k]
      mostcommon = sorted(counter, key=counter.get, reverse=True)[:10]
      if counter[mostcommon[0]] <= 1:
        print("No duplicates")
        next
      for j in mostcommon:
        if counter[j] > 1:
          print("{}: \t{}".format(",".join(j), counter[j]))

lc = LottoCounter()
with open(file, 'rb') as csvfile:
  lottoreader = csv.reader(csvfile)
  for row in lottoreader:
    lc.processrow(row)
lc.printcommon()
