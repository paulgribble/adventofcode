% Advent of Code 2015 Day 2
% https://adventofcode.com/2015/day/2

% Part 1
boxes = importdata('ac201502_input.txt');
total_paper = 0;
for i=1:length(boxes)
    a_box = boxes{i};
    box_sides = split(a_box, 'x');
    l = str2num(box_sides{1});
    w = str2num(box_sides{2});
    h = str2num(box_sides{3});
    box_sa = (2*l*w) + (2*w*h) + (2*l*h);
    sides = sort([l*w, w*h, l*h]);
    small_side = sides(1);
    box_sa = box_sa + small_side;
    total_paper = total_paper + box_sa;
end
fprintf('Part 1: total paper needed is %d\n', total_paper);

% Part 2
boxes = importdata('ac201502_input.txt');
total_ribbon = 0;
for i=1:length(boxes)
    a_box = boxes{i};
    box_sides = split(a_box, 'x');
    l = str2num(box_sides{1});
    w = str2num(box_sides{2});
    h = str2num(box_sides{3});
    edges_sorted = sort([l, w, h]);
    ribbon = 2*edges_sorted(1) + 2*edges_sorted(2) + l*w*h;
    total_ribbon = total_ribbon + ribbon;
end
fprintf('Part 2: total ribbon needed is %d\n', total_ribbon);


