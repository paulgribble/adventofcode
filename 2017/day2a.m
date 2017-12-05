S = load('day2_input.txt');

[r,c] = size(S);

checksum = 0;

for i=1:r
    checksum = checksum + (max(S(i,:))-min(S(i,:)));
end

disp(sprintf('checksum = %d', checksum))
