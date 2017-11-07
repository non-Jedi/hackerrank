function create_stairs(n::Int)::Array{String}
    output = Array{String}(n)
    for i in range(1, n)
        output[i] = repeat(" ", n - i) * repeat("#", i)
    end
    output
end

n = parse(Int, readline(STDIN))
for i in create_stairs(n)
    println(i)
end
