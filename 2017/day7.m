%% part 1

fid = fopen('day7_input_test.txt','r');
T = [];
p = ["(",")",",","->","0","1","2","3","4","5","6","7","8","9"];
while ~feof(fid)
    tmp = string(fgetl(fid));
    %disp(tmp);
    tmp = split(replace(tmp,p,""));
    T = [T; string(tmp)];
end
fclose(fid);

[words,~,idx] = unique(T);
numOccurrences = histcounts(idx,numel(words));
[yy,ii] = min(numOccurrences);
rootword = words(ii);
disp(sprintf('the bottom program is %s',rootword));

%% part 2


