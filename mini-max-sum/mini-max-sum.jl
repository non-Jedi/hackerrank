function get_min_max_of_4(a::Array{Int64, 1})
    min_value = typemax(Int64)
    max_value = typemin(Int64)
    total = 0
    for i in a
        total += i
        if i < min_value
            min_value = i
        end
        if i > max_value
            max_value = i
        end
    end
    total - max_value, total - min_value
end

a = parse.(Int64, split(readline(STDIN), " "))
min, max = get_min_max_of_4(a)
println("$min $max")
