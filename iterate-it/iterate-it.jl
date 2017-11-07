function count_reps(n::Int32, a::Array{Int32, 1})
    reps = 0
    while length(a) > 0
        b = Array{Int32, 1}(0)
        for i in a
            for j in a
                val = i - j
                if val != 0
                    push!(b, abs(val))
                end
            end
        end
        a = b
        reps += 1
    end
    reps
end


n = parse(Int32, readline(STDIN))
a = parse.(Int32, split(readline(STDIN), " "))
print(count_reps(n, a))
