Assignment
Main branch for Production
Develop
Feature1
Feature2
....
1.	Branching can be structured something like below

Main – Production deployment. Will be merged from Develop branch

Develop – Development branch. All features branch will be merged to this branch

Feature/Feature1 & Feature/Feature2 
– Feature branches. It will be created from Develop branch and Code needs to be tested before merging with develop branch.
For each feature branch i.e. Feature/feature1 & Feature/feature2, we can create a temporary feature branch. These branches will be used for development and testing of the feature


https://github.com/jagasworld/assignment
(Provided screenshots below in case if you are not allowed to use the links)
Written a basic python program with read and write operations in each feature branch and then created a PR request to merge it with develop branch. Merge conflicts have been resolved. Finally, after all necessary testing, code needs to be merged with Main branch. 
