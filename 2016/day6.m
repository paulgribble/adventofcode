% Advent of Code 2016 Day 6
% https://adventofcode.com/2016/day/6

% load the data
m = importdata("day6_input.txt");
m = cell2mat(m);

% setup variable to store frequencies of
% each char in each position
[r,c] = size(m);
F = zeros(26,c);

% count frequencies
for i=1:r
    for j=1:c
        letterpos = m(i,j) - 'a' + 1;
        F(letterpos,j) = F(letterpos,j) + 1;
    end
end

% Part 1: find most common character in each position
[val,ind] = max(F);
message1 = char('a'+ind-1);
fprintf("Part 1: the message is %s\n", message1)

% Part 2: find the least common character in each position
[val,ind] = min(F);
message2 = char('a'+ind-1);
fprintf("Part 2: the message is %s\n", message2)
