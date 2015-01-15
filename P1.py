# Input: text file 
#         --> format == "1234;Sample Text;Followed by more stuff"
# Output: print the line with the maximum int 
#         and if the file contains two same max ints then 
#         print the line that appeared in the text file first 
# Purpose: program reads an input file (given for testing purpose) 
#          with lines and prints the line with the max int

with open("P1.txt", "r") as f:
	str = f.readlines()

lines = [None] * len(str)
nums = [None] * len(str)

for x in range(len(lines)):
	lines[x] = str[x].split(';')
	nums[x] = int(lines[x][0])

num_line = nums.index(max(nums))
print str[num_line]