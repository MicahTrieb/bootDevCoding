#Lesson Link: https://www.boot.dev/lessons/e30cadd2-5610-4b47-bcf3-e54bb44d07a6
#   
def selection_sort(nums):


    for currentIndex in range (0, len(nums)):
        for currentInnerIndex in range(currentIndex + 1, len(nums)):
            if nums[currentIndex] > nums[currentInnerIndex]:
                nums[currentIndex], nums[currentInnerIndex] = nums[currentInnerIndex], nums[currentIndex]

    return(nums)
                
            

                
            

