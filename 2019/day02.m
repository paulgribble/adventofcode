% Part 1
opcodes = load("day02_input.txt");

opcodesp1 = opcodes;
opcodesp1(1+1) = 12;
opcodesp1(2+1) = 2;
p1 = day2run(opcodesp1);
fprintf("Part 1: answer = %d\n", p1);

% Part 2
ij = combvec(0:99,0:99)';
for i=1:size(ij,1)
  opcodesp2 = opcodes;
  opcodesp2(1+1) = ij(i,1);
  opcodesp2(2+1) = ij(i,2);
  p2 = day2run(opcodesp2);
  if (p2 == 19690720)
    fprintf("Part 2: answer is %d\n", 100 * ij(i,1) + ij(i,2));
    break
  end
end

function p = day2run(opcodes)
  i = 1;
  while (i <= length(opcodes)-4)
    i1 = opcodes(i+1);
    i2 = opcodes(i+2);
    i3 = opcodes(i+3);
    if (opcodes(i)==1)
      opcodes(i3+1) = opcodes(i1+1) + opcodes(i2+1);
    elseif (opcodes(i)==2) 
      opcodes(i3+1) = opcodes(i1+1) * opcodes(i2+1);
    elseif (opcodes(i)==99) 
      break
    end
    i = i + 4;
  end
  p=opcodes(1);
end
