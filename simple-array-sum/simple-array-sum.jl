
n = parse(Int, readline(STDIN))
integers = parse.(Int, split(readline(STDIN)))
println(sum(integers))
