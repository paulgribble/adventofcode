fc = load('day01_input.txt'); % frequency changes
n = length(fc);

f = sum(fc); % final frequency
fprintf("Part 1: answer is %d\n", f);

f = 0;                                  % initial frequency
i = 1;                                  % which frequency change to apply
found = false;                          % haven't found a repeat yet
flist = ones(1,1e6)*realmax;            % store all frequencies
ii = 1;                                 % how many frequencies we've stored
fprintf("Part 2: answer is ...");       % it's going to take a while

while (isempty(find(f==flist,1)))       % while we haven't found a repeat,
    flist(ii) = f;                      % store the current frequency
    f = f + fc(i);                      % compute new frequency
    i = mod(i,n) + 1;                   % increment index into fc array
    ii = ii + 1;                        % increment index into flist
end
fprintf(" %d\n", f);

