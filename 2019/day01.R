# Part 1
m <- scan("day01_input.txt")
total_fuel <- sum(floor(m/3)-2)
cat(sprintf("Part 1: total fuel is %d\n", total_fuel))

# Part 2
total_fuel <- 0
for (i in seq(length(m))) {
  fm <- 0
  f = floor(m[i]/3)-2
  while (f > 0) {
    fm <- fm + f
    f <- floor(f/3)-2
  }
  total_fuel <- total_fuel + fm
}
cat(sprintf("Part 2: total fuel needed is %d\n", total_fuel))
