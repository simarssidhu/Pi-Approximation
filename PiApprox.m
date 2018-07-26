% Numerical Approximation for Pi

x = 1.01;   % Initial base of exponential
Max_Iter = 1000;  % Number of iterations
Exponent = 2;   % Exponent of exponential
Precision = 1000000;    % Number of digits

% Algorithm for approximation

for i=1:Max_Iter
    x = x^((Exponent)^(cos(x)));
    Approx(i,1) = 2*x;
    True_Error(i,1) = (pi - 2*x)/pi;
end

digits(Precision);  % Sets number of digits to be shown
x = x*2;
display(vpa(x));
diary ('pi.txt')    % Saves pi result into .txt file
vpa(x)
diary off

Iter = 1:Max_Iter;
plot(Iter,Approx);  % Plots approximation of pi vs. number of iteration

clear True_Error;
clear Approx;
