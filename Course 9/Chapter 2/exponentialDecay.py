#Lesson Link: https://www.boot.dev/lessons/3ae4708e-0a55-4bae-8011-6de75bce05ab

def decayed_followers(intl_followers, fraction_lost_daily, days):
    retentionRate = 1 - fraction_lost_daily
    return (intl_followers * (retentionRate ** days))
