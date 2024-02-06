# IntersectingChordes

## Problem 1
  Two parallel lists: The first contains the radian measure of the start or end. The second contains the identifiers of the chords. The identifiers are denoted 's_x' and'ex', where's' is the starting point of the  chord, 'e' is the end point of the chord, and s_x < e_x. The radian measures are sorted in ascending order.

## Solution 1 : Computational approach  

<p align="center">
   <img width="250" height="200" src="https://github.com/AkshataSalunkhe/IntersectingChordes/assets/143021478/dfbc6800-a685-4ecd-ab1a-c687d8487529">
</p>
Approch : 

<p align="center">
   <img width="600" height="1000" src="https://github.com/AkshataSalunkhe/IntersectingChordes/assets/143021478/5ac1f5b3-70cc-449f-9b5d-6590c83cb903">
</p>

Intersection Logic :  
    Sorted dictionery by identifiers to extract exact s1 and e1 pairs and then extracted 4 points from give list and sorted them again by radian values. Then by analysing end numbers of identifiers, the alternate numbers are equal then they will intersect like 1212 or 2121 if the end numbers are 1122 or 2211 then it won't. 

Complexity:  
1. Sorting the dictionary by keys: O(n log n), where 'n' is the number of chords.  
2. Nested loops for pairwise comparison: O(n^2), where 'n' is the number of chords.  
Therefore, the overall time complexity of the code is O(n log n + n^2). In big O notation, when expressing the time complexity, we generally focus on the dominant term, which is the term with the highest growth rate. In this case, the dominant term is n^2. Therefore, the big O notation for the provided code is O(n^2).  

Note: If given radian list is sorted with identifiers then the complexity would be O(n^2). 
