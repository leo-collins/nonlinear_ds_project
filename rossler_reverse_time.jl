using DifferentialEquations, Plots, LaTeXStrings

plotly()

function rosslerrule(du, u, p, t)
	a, b, c = p
	x, y, z = u

	du[1] = y + z
	du[2] = -x - a*y
	du[3] = -b - z*(x - c)
end

p0 = [0.06, 0.3, 4.9]
u0 = [0.1, 0.1, 0.1]

prob = ODEProblem(rosslerrule, u0, (0, 200), p0)
sol = solve(prob, Rosenbrock23(), reltol=1e-6, abstol=1e-6)

plot(sol, idxs=(1,2,3))