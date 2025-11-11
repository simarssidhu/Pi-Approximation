# Pi-Approximation

## Introduction

This is a Matlab program for a quick numerical approximation of ![pi](http://mathurl.com/6cu2u8.png).

## How it works

This numerical method uses the following iterative algorithm:

![Main Equation](http://mathurl.com/y9dnx6jd.png)

where 
- ![x_i](http://mathurl.com/qym38jh.png) is the current iteration's estimate
- ![x_i-1](http://mathurl.com/y7tx4362.png) is the previous iteration's estimate

Reiterating this equation `Max_Iter` times will give an approximation of ![pi/2](http://mathurl.com/2e4usyb.png). Simply multiply this number by 2 to get the approximate of ![pi](http://mathurl.com/6cu2u8.png).

## Things to note

This program will store the value of your ![pi](http://mathurl.com/6cu2u8.png) approximation in a .txt file called `pi.txt`. To change the precision of the value stored, you can change the variable `Precision` in the PiApprox.m.

Try playing around with the variables `x` and `Exponent` to see which values arrive to the approximation quicker.

## Python port performance

The Python script mirrors the MATLAB loop but relies on pure-Python arbitrary
precision arithmetic by default. That makes the million-digit run
significantly slower than MATLAB's symbolic toolbox, which calls into the
compiled GMP/MPFR libraries. Installing [`gmpy2`](https://pypi.org/project/gmpy2/)
lets `mpmath` switch to those libraries and the script automatically uses that
faster backend when it is present. If even that is not enough, the remaining
option is to implement the loop in C or C++ directly on top of GMP/MPFR so the
entire computation stays in compiled code.
