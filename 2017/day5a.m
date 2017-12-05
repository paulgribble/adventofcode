%% part 1

%L = load('day5_input.txt');
L = [0 3 0 1 -3];

i = 1;
Ln = length(L);
steps = 0;

while ((i<=Ln)&(i>=1))
    itmp = i;
    i = i + L(i);
    L(itmp) = L(itmp) + 1;
    steps = steps + 1;
end
disp(sprintf('%d steps', steps));

%% part 2

L = load('day5_input.txt');
%L = [0 3 0 1 -3];

i = 1;
Ln = length(L);
steps = 0;

while ((i<=Ln)&(i>=1))
    itmp = i;
    if (L(i)>=3)
        inc = -1;
    else
       inc = 1; 
    end
    i = i + L(i);
    L(itmp) = L(itmp) + inc;
    steps = steps + 1;
end
disp(sprintf('%d steps', steps));

