# computationalthinkingandprogrammingpy
Analysing and Problem Solving

# Dynamic Programming Problem
1.Problem Statement - Mobile Data Plan Optimization using Dynamic Programming

A customer has multiple mobile data plans. Each plan has a cost and a corresponding benefit. The customer has a fixed budget and wants to select a combination of plans that provides the maximum total benefit without exceeding the budget.

This problem can be solved using Dynamic Programming (DP) and is similar to the 0/1 Knapsack Problem.

* Approach

Each mobile plan has:

Cost → Amount required to select the plan.
Benefit → Value gained from selecting the plan.
Budget → Maximum amount the customer can spend.

The DP array stores the maximum benefit that can be obtained for every possible budget from 0 to the given budget.

The algorithm considers each plan one at a time and updates the DP table to find the optimal combination.

Example:
Plan	Cost	Benefit
A	    ₹200	 30
B	    ₹400	 60
C	    ₹500	 70
D	    ₹300	 40

Maximum Budget: ₹1000

The optimal combination is:

A + C + D

Total Cost = ₹200 + ₹500 + ₹300 = ₹1000
Total Benefit = 30 + 70 + 40 = 140

* Why Dynamic Programming?
Dynamic Programming is suitable because the problem has:

Optimal Substructure – The optimal solution can be constructed from optimal solutions to smaller subproblems.
Overlapping Subproblems – The same budget subproblems can occur repeatedly.

DP avoids unnecessary repeated calculations and efficiently finds the maximum benefit.

* Complexity

Let:
n = number of plans
B = available budget

Time Complexity: O(n × B)

Space Complexity: O(B)

For this example:
n = 4
B = 1000

So the algorithm performs approximately 4000 DP iterations.

Technologies Used
Python
PyTorch
Dynamic Programming

Output:
Selected Plans: ['A', 'C', 'D']
Total Cost: 1000
Maximum Benefit: 140

//** 1st Problem explanation completed **//
