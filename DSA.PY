



# now we wuill make something that will have a less timecomplexity

class Solution(object):
    def calcluateMaxProfit(self,prices):
         maxProfit=0
         for i in range(len(prices)):    
           currentDay=prices[i]
           low=1
           high=len(prices)-1
           while low < len(prices)/2 and high > len(prices)/2 :
               if prices[low] >currentDay and prices[low]-currentDay>maxProfit:
                   maxProfit=prices[low]-currentDay
               if prices[high]>currentDay and prices[high]-currentDay>maxProfit:
                   maxProfit=prices[high]-currentDay
               low=low+1
               high=high-1     
             
         return maxProfit 
         
stock_calculator=Solution()


print(stock_calculator.calcluateMaxProfit([43,1,19,42,6,4,31]))
       

















# this was good until a long array came and the time complexity excedded
# here's another one to check best day to sell stock

# class Solution(object):
#     def maxProfit(self, prices):
#      profit=0  
#      for i in range(len(prices)):
#          j=i+1
#          while j < len(prices):
#              if prices[i]<prices[j] and prices[j]-prices[i]> profit:
#                  profit= prices[j]-prices[i]
#              j=j+1
      
#      return profit
     




# stock_calculator=Solution()


# print(stock_calculator.maxProfit([0,1,19,3,6,4,11]))




























# we are going to make a algorithm  that returns the square root of a given number

# class Solution(object):
#     def mySqrt(self, x):
#         number=x
#         subtractor=1
#         counter=0
        
#         while number-subtractor >= 0 :
#             counter=counter+1
#             print(number,subtractor,counter)
#             number=number-subtractor
#             subtractor = subtractor+2
            
            
            
            
#         return counter   
        
# solution_instance = Solution()

# print(solution_instance.mySqrt(86))