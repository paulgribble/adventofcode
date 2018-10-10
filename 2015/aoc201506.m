% Advent of Code 2015 Day 6
% https://adventofcode.com/2015/day/6

% PART ONE

% set up a data structure to represent the problem

L = zeros(1000, 1000); % a 1000x1000 grid of zeros (all lights start 'off')

% read the input file line by line,
% interpret the instructions and execute them

fid = fopen('aoc201506_input.txt', 'r');
while ~feof(fid)    
    l = fgetl(fid);     % read in next line of file as a character array
    l = split(l, ' ');  % split by the space character
    if strcmp(l{1}, 'toggle') % it's a toggle instruction
        xy1 = split(l{2}, ',');                   % extract the coordinates
        xy1 = [str2num(xy1{1}), str2num(xy1{2})]; % convert to num
        xy2 = split(l{4}, ',');                   % extract the coordinates
        xy2 = [str2num(xy2{1}), str2num(xy2{2})]; % convert to num
        xy1 = xy1 + [1 1]; % MATLAB indexing starts at 1!
        xy2 = xy2 + [1 1];
        % toggle the whole range, vectorized!
        L(xy1(1):xy2(1), xy1(2):xy2(2)) = ~L(xy1(1):xy2(1), xy1(2):xy2(2));
    else % must be a 'turn on' or a 'turn off' instruction
        xy1 = split(l{3}, ',');                   % extract the coordinates
        xy1 = [str2num(xy1{1}), str2num(xy1{2})]; % convert to num
        xy2 = split(l{5}, ',');                   % extract the coordinates
        xy2 = [str2num(xy2{1}), str2num(xy2{2})]; % convert to num
        xy1 = xy1 + [1 1]; % MATLAB indexing starts at 1!
        xy2 = xy2 + [1 1];
        if strcmp(l{2}, 'off')
            L(xy1(1):xy2(1), xy1(2):xy2(2)) = 0;
        elseif strcmp(l{2}, 'on')
            L(xy1(1):xy2(1), xy1(2):xy2(2)) = 1;
        end
    end
end
fclose(fid);

% how many lights are lit?
n_lit = sum(sum(L));
fprintf('Part 1: there are %d lights lit\n', n_lit);


% PART TWO

% set up a data structure to represent the problem

L = zeros(1000, 1000); % a 1000x1000 grid of zeros (all lights start 'off')

% read the input file line by line,
% interpret the instructions and execute them

I = importdata('aoc201506_input.txt', '%s'); % import lines as strings

for i=1:length(I)
    l = split(I{i}, ' ');  % split by the space character
    if strcmp(l{1}, 'toggle') % it's a toggle instruction
        xy1 = split(l{2}, ',');                   % extract the coordinates
        xy1 = [str2num(xy1{1}), str2num(xy1{2})]; % convert to num
        xy2 = split(l{4}, ',');                   % extract the coordinates
        xy2 = [str2num(xy2{1}), str2num(xy2{2})]; % convert to num
        xy1 = xy1 + [1 1]; % MATLAB indexing starts at 1!
        xy2 = xy2 + [1 1];
        % toggle the whole range, vectorized!
        L(xy1(1):xy2(1), xy1(2):xy2(2)) = L(xy1(1):xy2(1), xy1(2):xy2(2)) + 2;
    else % must be a 'turn on' or a 'turn off' instruction
        xy1 = split(l{3}, ',');                   % extract the coordinates
        xy1 = [str2num(xy1{1}), str2num(xy1{2})]; % convert to num
        xy2 = split(l{5}, ',');                   % extract the coordinates
        xy2 = [str2num(xy2{1}), str2num(xy2{2})]; % convert to num
        xy1 = xy1 + [1 1]; % MATLAB indexing starts at 1!
        xy2 = xy2 + [1 1];
        if strcmp(l{2}, 'off')
            L(xy1(1):xy2(1), xy1(2):xy2(2)) = L(xy1(1):xy2(1), xy1(2):xy2(2)) - 1;
            L_tmp = L(xy1(1):xy2(1), xy1(2):xy2(2));
            L_tmp(L_tmp < 0) = 0;
            L(xy1(1):xy2(1), xy1(2):xy2(2)) = L_tmp;
        elseif strcmp(l{2}, 'on')
            L(xy1(1):xy2(1), xy1(2):xy2(2)) = L(xy1(1):xy2(1), xy1(2):xy2(2)) + 1;
        end
    end
end

% how many lights are lit?
bright_level = sum(sum(L));
fprintf('Part 2: total brightness is %d\n', bright_level);


