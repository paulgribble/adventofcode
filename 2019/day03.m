% Part 1
fid = fopen('day03_input.txt','r');
w1 = fgetl(fid); w1 = split(w1,',');
w2 = fgetl(fid); w2 = split(w2,',');
fclose(fid);
W1 = zeros(20000,10000);
W2 = zeros(20000,10000);
xyc = [0,0]; offset=[10000,5000];
for i=1:length(w1)
   wire = w1{i};
   if wire(1)=='L'
       xy = [-str2num(wire(2:end)) 0];
   elseif wire(1)=='R'
       xy = [ str2num(wire(2:end)) 0];
   elseif wire(1)=='U'
       xy = [0  str2num(wire(2:end))];
   elseif wire(1)=='D'
       xy = [0 -str2num(wire(2:end))];
   end
   W1(xyc+offset):W1([xyc(1)+xy(1) xyc(2)]+offset) = 1;
end

