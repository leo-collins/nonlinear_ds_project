using DynamicalSystems, Plots, LaTeXStrings

# plotly()
gr()

function rosslerrule(u, p, t)
	a, b, c = p
	x, y, z = u

	du1 = -y - z
	du2 = x + a*y
	du3 = b*x + z*(x - c)

	return SVector(du1, du2, du3)
end

p0 = [0.3, 0.3, 4.9]
u0 = [0.1, 0.1, 0.1]

rossler = CoupledODEs(rosslerrule, u0, p0)

n = 100
pvalues = 0.359:0.000001:0.361
# pvalues = 0.2776:0.000001:0.2785
pmap = PoincareMap(rossler, (1, 2.0); direction=1)
Y, t = trajectory(pmap, 500.0)
# Plots.scatter(Y[:, 2], Y[:, 3])

output = orbitdiagram(pmap, 2, 1, pvalues; n, Ttr=400)

L = length(pvalues)
x = Vector{Float64}(undef, n*L)
y = copy(x)
for j in 1:L
    x[(1 + (j-1)*n):j*n] .= pvalues[j]
    y[(1 + (j-1)*n):j*n] .= output[j]
end

Plots.scatter(x, y; markersize=0.8, color="black", size=(960, 720), legend=false)
# plot!([0.2776, 0.2776, 0.2785, 0.2785, 0.2776], [1.597, 1.631, 1.631, 1.597, 1.597], color="red", lw=2)
# Plots.ylims!(-4, -3)
Plots.xlabel!(L"a")
Plots.ylabel!(L"y")