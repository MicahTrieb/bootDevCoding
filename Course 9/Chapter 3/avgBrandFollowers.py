#Lesson Link: https://www.boot.dev/lessons/7d38f457-fbd2-42ae-adc2-b2ca6f8bfaee

def get_avg_brand_followers(all_handles, brand_name):
    currentBrandLoyalty = 0
    totalCalculatingList = []
    if isinstance(all_handles, list):
        for currentList in all_handles:
            for currentHandle in currentList:
                if brand_name in currentHandle:
                    currentBrandLoyalty += 1
                    
    return (currentBrandLoyalty / len(all_handles))
