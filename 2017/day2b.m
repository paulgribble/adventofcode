S = load('day2_input.txt');

[r,c] = size(S);

checksum = 0;

i1 = NaN;
i2 = NaN;

for i=1:r
    for j=1:c
        for k=1:c
            if (mod(S(i,j),S(i,k)) == 0) & (~(j==k))
                i1 = j;
                i2 = k;
            end
        end
    end
    checksum = checksum + (S(i,i1) / S(i,i2));
end
