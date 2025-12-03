'''
in terminal command to setup 
conda activate  # activate base environment
jupyter lab     # open jupyter lab in chrome browser
# now in browser create a file and paste the json data
# and load the data in python programing and print it.

# JSON DATA
[
  {"name": "Alice", "rating": "5 ", "feedback": "Great product!!", "age": "25"},
  {"name": "Bob", "rating": "four", "feedback": "ok but late Delivery", "age": "30"},
  {"name": " Charlie", "rating": "two", "feedback": "BAD EXPERIENCE "},
  {"name": "Diana", "feedback": "Loved it!", "rating": "5", "age": "28"},
  {"name": "Eve", "rating": "3.5", "feedback": "Average - could be better", "age": "20"},
  {"name": "Alice", "rating": "5", "feedback": "Great product again!", "age": "25"}
]


# assignment 1
# Next step
# to give data to machine model we have to clean and structure the data first
# 1. data is inconsistent -> mixed type (rating -> integer, string)
# 2. missing data -> (age) -> None
# 3. duplicate data -> use set to deduplicate data.


# assignment 2
# next 
# get insights
# 1. get avg rating
# 2. percentage of poor rating


# assignment 3 -> build a product recommendation feature(Rule Based, not ML)
# 1. if user rating >= 4, recommend same brand products. -> "Apple"
# 2. if user rating < 4, recommend different brand products.-> "Samsung"
'''