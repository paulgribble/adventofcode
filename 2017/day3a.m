%% part 1

% 17  16  15  14  13
% 18   5   4   3  12
% 19   6   1   2  11
% 20   7   8   9  10
% 21  22  23  24  25

target = 325489;

% distance of our target = distance of the nearest odd square to origin +
% distance of input to nearest odd square

x = 0;
y = 0;
dx = 0;
dy = -1;
i = 0;
while (i ~= target)
    i = i + 1;
    if (i==target)
        disp(abs(x)+abs(y));
    end
    if ((x==y) | ((x<0)&(x==-y)) | ((x>0)&(x==(1-y))) ) % a corner
        tmp = dx;
        dx = -dy;
        dy = tmp;
    end
    x = x + dx;
    y = y + dy;
end

%% part 2

