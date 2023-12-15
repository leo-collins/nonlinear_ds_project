using DynamicalSystems, Plots, LaTeXStrings

#plotly()
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
X, t = trajectory(rossler, 1000.0; Ttr=900.0, Δt=0.01)
scene = plot(X[:, 1], X[:, 2], X[:, 3], lw=0.8, color=:black,
xlabel=L"x", ylabel=L"y", zlabel=L"z", size=(1000, 1000), legend=false,
camera=(10,15))


# rossler = CoupledODEs(rosslerrule, [0.00001, 0.00001, 0.00001], p0)
# X2, t2 = trajectory(rossler, 103; Δt=0.01)
# plot!(scene, X2[:, 1], X2[:, 2], X2[:, 3], color=:red, lw=4)

# fp, eigs, stable = fixedpoints(rossler, IntervalBox(-30..30, -30..30, -30..30))
# for i in range(length=length(fp))
#     if stable[i]
#         scatter!(scene, Tuple(fp[i]), markersize=2, markercolor=:red
#         scatter!(scene, Tuple(fp[i]), markersize=2, markercolor=:red)
#     end
# end
