#Lesson Link: https://www.boot.dev/lessons/d4b077d7-3d68-4cd6-8996-ff54bccf7585

class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"


# dont touch above this line


def vanity(influencer):
    influencer.vanity = ((influencer.num_bio_links * 5) + influencer.num_selfies)


def vanity_sort(influencers):
    vanityDictionary = {}
    for currentInfluencer in influencers:
        vanity(currentInfluencer)
    return (sorted(influencers, key=lambda x: x.vanity))

