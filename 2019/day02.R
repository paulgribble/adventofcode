# Part 1
opcodes <- scan("day02_input.txt", sep=",")

day2run <- function(opcodes) {
  i = 1
  while (i <= length(opcodes)-4) {
    i1 = opcodes[i+1]
    i2 = opcodes[i+2]
    i3 = opcodes[i+3]
    if (opcodes[i]==1) {
      opcodes[i3+1] = opcodes[i1+1] + opcodes[i2+1]
    }
    else if (opcodes[i]==2) {
      opcodes[i3+1] = opcodes[i1+1] * opcodes[i2+1]
    }
    else if (opcodes[i]==99) {
      break
    }
    i <- i + 4
  }
  return(opcodes[1])
}

opcodesp1 = opcodes
opcodesp1[1+1] = 12
opcodesp1[2+1] = 2
p1 = day2run(opcodesp1)
cat(sprintf("Part 1: answer = %d", p1))

# Part 2
ij = expand.grid(seq(0,99),seq(0,99))
for (i in seq(nrow(ij))) {
  opcodesp2 = opcodes
  opcodesp2[1+1] = ij[i,1]
  opcodesp2[2+1] = ij[i,2]
  p2 = day2run(opcodesp2)
  if (p2 == 19690720) {
    cat(sprintf("Part 2: answer is %d", 100 * ij[i,1] + ij[i,2]))
    break
  }
}

