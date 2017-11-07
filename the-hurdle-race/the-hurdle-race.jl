function needed_drinks(k::Int16, a::Array{Int16, 1})
    high = maximum(a)
    if k >= high
        0
    else
        high - k
    end
end

n, k = parse.(Int16, split(readline(STDIN), " "))
a = parse.(Int16, split(readline(STDIN), " "))
println(needed_drinks(k, a))
