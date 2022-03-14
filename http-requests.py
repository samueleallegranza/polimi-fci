import requests
import statistics

TRIES = 20
ENDPOINT = "https://google.it/"
measures = []

for i in range(TRIES):
    r = requests.get(ENDPOINT)
    measures.append(r.elapsed.microseconds /1000)
    print("Response time {} ms".format(r.elapsed.microseconds /1000))

print("Min: {} ms".format(min(measures)))
print("Max: {} ms".format(max(measures)))
print("Avg: {} ms".format(sum(measures)/len(measures)))
print("Avg: {} ms".format(statistics.mean(measures)))