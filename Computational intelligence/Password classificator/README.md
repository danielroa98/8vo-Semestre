# Password Classification
The idea is to classify the password, based on its strongness:
- 0 for weak;
- 1 for medium; and
- 2 for strong.

source: https://medium.com/@faizann20/machine-learning-based-password-strength-classification-7b2a3c84b1a6

#A . Data
The passwords used in our analysis are from 000webhost leak that is available online. How did we figure out which passwords were stronger and which were weaker? Well, there is a tool called PARS by Georgia Tech university which have all the commercial password meters integrated into it. All I did was give that tool all the passwords and it gave me new files for each commercial password strength meter. The files contained the passwords with one more column i.e their strength based on the commercial password strength meters.



https://towardsdatascience.com/building-a-logistic-regression-in-python-step-by-step-becd4d56c9c8
