#Lesson Link: https://www.boot.dev/lessons/70e1a5ad-7425-414d-bd41-d6579c133290

def get_follower_prediction(follower_count, influencer_type, num_months):
    returnValue = follower_count
    if influencer_type == "fitness":
        while num_months >= 1:
            returnValue = returnValue * 4
            num_months -= 1
    if influencer_type == "cosmetic":
        while num_months >= 1:
            returnValue = returnValue * 3
            num_months -= 1
    else:
        while num_months >= 1:
            returnValue = returnValue * 2
            num_months -= 1
    return returnValue
