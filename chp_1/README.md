# Chapter 1 - Role of Algorithms in Computing

## 1.1 Questions
1. 1. *Example of sorting:* Finding the highest premium of policies written within the month, is a sorting problem.
   2. *Example of shortest distance:* Map routing
2. *Other than speed, other measures of efficiency:* memory use.
3. Dictionaries, as k,v pairs. 
   1. Time complexity that is constant, for retrieval. 
   2. Iteration and nesting possible.
4. Travelling Salesman and Shortest-path
   1. Both are np-complete
   2. Travelling Salesman
      1. Finding the shortest possible round-trip path to all points from a single point.
      2. Shortest ROUTE
   3. Shortest Distance
      1. Start and end point - no return needed.
      2. Only one obligatory node.
5. 1. Best solution problem: flight-control system
   2. Approximate solutions: Recommendation engine.
6. A reservation system is an example of a problem where some nights the restaurant needs to allocate seats and has 
reservations for all seats. Other times, reservations come in below the restaurants capacity and seating is allocated 
with this in mind. This type of problem at times presents all inputs needed for execution and at other times input comes 
partially, and full input may come later.

## 1.2 Questions
### Exercises
1. Search engine - requires algorithms to parse strings, score nodes, find efficient paths.
2. Insertion sort runs in 8n^2 steps and merge stort runs in 64 _n_ lg _n_ steps. For which values of _n_ does insertion 
sort beat merge sort? <br>
   <t>a. ChapterOne.java.compareInsertionSortWithMerge(); 45
3. What is the smallest value of _n_ such that an algorithm whose running time is 100 _n_ ^2 runs faster than an 
algorithm whose running time is 2^n on the same machine<br>
 <t> b. ChapterOne.java.smallestValueOfN(); 16

### Problems
1. For each function f(n) and time t in the following table, determine the largest size n of a problem that can be solved 
in time t, assuming that the algorithm to solve the problem takes f(n) microseconds.

| _____ | 1 Second | 1 Second | 1 Second |<br>
|_____|_____|