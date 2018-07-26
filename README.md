# Pi-Approximation

## Introduction

This is program for a quick numerical approximation of ![pi](http://mathurl.com/6cu2u8.png).

## How it works

This numerical method uses the following iterative algorithm:

![Main Equation](http://mathurl.com/y9dnx6jd.png)

where 
- ![x_i](http://mathurl.com/qym38jh.png) is the current iteration's estimate
- ![x_i-1](http://mathurl.com/y7tx4362.png) is the previous iteration's estimate

Reiterating this equation Max_Iter times will give an approximation of ![pi/2](http://mathurl.com/2e4usyb.png). Simply multiply this number by 2 to get the approximate of ![pi](http://mathurl.com/6cu2u8.png).

## Things to note

This program will store the value of your ![pi](http://mathurl.com/6cu2u8.png) approximation in a .txt file called `pi.txt`. To change the precision of the value stored, you can change the variable `Precision` in the PiApprox.m.

Try playing around with the variables `x` and `Exponent` to see which values arrive to the approximation quicker.
