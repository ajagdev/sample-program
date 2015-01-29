# Input: text file 
#         --> format == "1234;Sample Text;Followed by more stuff"
# Output: print the line with the maximum int 
#         and if the file contains two same max ints then 
#         print the line that appeared in the text file first 
# Purpose: program reads an input file (given for testing purpose) 
#          with lines and prints the line with the max int


with open("P1.txt", "r") as f: #open file and read all the lines at once
	str = f.readlines()

lines = [None] * len(str) #list of the lines split from the ';'
nums = [None] * len(str) #list of the nums extracted from the lines

for x in range(len(lines)):
	lines[x] = str[x].split(';')  #split each line at ';'
	nums[x] = int(lines[x][0])	#extract the numbers for the lines

num_line = nums.index(max(nums)) #get the index of the max num
print str[num_line]