function count_num_max(a::Array{Int})
    num_max = 0
    max_val = typemin(Int)
    for i in a
        if i > max_val
            num_max = 1
            max_val = i
        elseif i == max_val
            num_max += 1
        end
    end
    num_max
end

n = parse(Int, readline(STDIN))
a = parse.(Int, split(readline(STDIN), " "))
println(count_num_max(a))
