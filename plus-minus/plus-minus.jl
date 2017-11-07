function sort_plus_minus(a)
    positive = negative = zeros = 0
    for i in a
        if i > 0
            positive += 1
        elseif i < 0
            negative += 1
        elseif i == 0
            zeros += 1
        end
    end
    positive, negative, zeros
end

n = parse(Int, readline(STDIN))
a = parse.(Int, split(readline(STDIN), " "))

positive, negative, zeros = sort_plus_minus(a)

println(convert(Float32, positive / n))
println(convert(Float32, negative / n))
println(convert(Float32, zeros / n))
