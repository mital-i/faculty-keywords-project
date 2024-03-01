# Faculty Keywords Project

# Description: 
As an employee of the UCI Biological Sciences School, me and my supervisor collected data from the faculty, sepcifically keywords/terms that desrcibed their research endeavors. We wanted to find a way to streamline the collaboration efforts between professors by finding which professors would be more compatible based on keywords. 

# How to Install and Run: 
If you don't have VS Code downloaded, download it here: https://code.visualstudio.com/ 
Make sure you have the write packages installed before running the program. I have listed them below and you can download them using pip. 
- pandas
- gensim
- numpy

After you have these installed, run the program. The program has "Yassa, Michael" as the sample input however you may change that to the name of any professor you would like to look for. Make sure it is in the format Last Name, First Name. The program will give you a list of potential collaborators as well as the total number of potential collaborators. 

# Learnings: 
During the development of this project, I started by first attempting to the Open AI API in order to do the job for me, however I quickly ran into the token and request limit. I switched gears to use the Gemini API however it wasn't as refined at the Open AI API and I had the same limit issue. I researched vectorization and cosine similarity which seemed like the most reliable method. 
