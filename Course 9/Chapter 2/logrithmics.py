#Lesson Link: https://www.boot.dev/lessons/390a8bcc-e633-4628-8be8-d44932f4fcd1

import math


def get_influencer_score(num_followers, average_engagement_percentage):
    return (math.log(num_followers, 2) * average_engagement_percentage)
