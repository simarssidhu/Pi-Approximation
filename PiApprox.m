x = 1.01;
Max_Iter = 1000;  % if lowering Max_Iter, delete Approx and True_Error variables in Workspace and then Run
Exponent = 2;
Precision = 1000000;

for i=1:Max_Iter
    x = x^((Exponent)^(cos(x)));
    Approx(i,1) = 2*x;
    True_Error(i,1) = (pi - 2*x)/pi;
end

digits(Precision);
x = x*2;
display(vpa(x));
diary ('pi.txt')
vpa(x)
diary off

Iter = 1:Max_Iter;
plot(Iter,Approx);

clear True_Error;
clear Approx;