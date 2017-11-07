
n = parse(Int, readline(STDIN))
integers = parse.(Int64, split(readline(STDIN)))
println(sum(integers))
