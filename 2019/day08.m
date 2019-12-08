%% PART 1
fid = fopen("day08_input.txt","r");
I = fgetl(fid);
fclose(fid);
rows = 6; cols = 25;

%I = '123456789012';
%rows = 2; cols = 3;

n = length(I);
layers = n / (rows*cols);
PW = zeros(rows,cols,layers);
ii = 1;
for i=1:layers
    for j=1:rows
        for k=1:cols
            PW(j,k,i) = str2num(I(ii));
            ii = ii + 1;
        end
    end
end

nzeros = 0;
minzeros = realmax;
minzerolayer = 0;
for i=1:layers
    tmp = PW(:,:,i);
    tmp = tmp(:);
    nz = length(find(tmp==0));
    if (nz < minzeros)
        minzeros = nz;
        minzerolayer = i;
    end
end
tmp = PW(:,:,minzerolayer);
tmp = tmp(:);
part1 = length(find(tmp==1)) * length(find(tmp==2));
fprintf("Part 1: answer is %d\n", part1)

%% PART 2
fid = fopen("day08_input.txt","r");
I = fgetl(fid);
fclose(fid);
rows = 6; cols = 25;

%I = '0222112222120000';
%rows = 2; cols = 2;

n = length(I);
layers = n / (rows*cols);
PW = zeros(rows,cols,layers);
ii = 1;
for i=1:layers
    for j=1:rows
        for k=1:cols
            PW(j,k,i) = str2num(I(ii));
            ii = ii + 1;
        end
    end
end

PW2 = PW(:,:,layers);
for i=((layers-1):-1:1)
    tmp = PW(:,:,i);
    for j=1:rows
        for k=1:cols
            if tmp(j,k) < 2
                PW2(j,k) = tmp(j,k);
            end
        end
    end
end
figure;
imagesc(PW2)
axis([-1 cols+1 -1 rows+1])

