
from mrjob.job import MRJob


class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        parts = line.split(',')
        if len(parts) == 3:
            city = parts[0]     
            votes = parts[2] 
            yield (city, votes)


    def reducer(self, city, votes):

        votes_list = [int(vote) for vote in votes]


        min_votes = min(votes_list)
        max_votes = max(votes_list)

        yield (city, (min_votes, max_votes))


if __name__ == '__main__':
    MRWordFreqCount.run()

