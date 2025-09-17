# from difflib import SequenceMatcher

# with open('demo1.txt') as one_file, open ('demo2.txt') as two_file:
#     data_file1 = one_file.read() # use readlines to compair lines insted of strings 
#     data_file2 = two_file.read()
#     matches = SequenceMatcher(None,data_file1,data_file2).ratio()
#     print(f"the plagiarized content is {matches * 100}%")

# finding the exact diff between the files using Htmldiff() class

from difflib import HtmlDiff

with open ('demo1.txt') as one_file, open ('demo2.txt') as two_file:
    lines1 = one_file.readlines()
    lines2 = two_file.readlines()

# creat an instaence from HtmlDiff 

    html_diff = HtmlDiff().make_file(lines1,lines2, fromdesc='demo1.txt', todesc='demo2.txt')
# creat a file with name of output_file 
    with open('diff_report.html','w') as output_file:
        output_file.write(html_diff)

print("html diff report is genrated as 'diff_report.html'")