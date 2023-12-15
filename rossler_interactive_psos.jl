using GLMakie, DynamicalSystems

function rosslerrule(u, p, t)
	a, b, c = p
	x, y, z = u

	du1 = -y - z
	du2 = x + a*y
	du3 = b*x + z*(x - c)

	return SVector(du1, du2, du3)
end

u0 = [0.5, 0.5, 0.5]
p0 = [0.332, 0.3, 4.9]

rossler = CoupledODEs(rosslerrule, u0, p0)

X, t = trajectory(rossler, 2000.0; Ttr=1000.0, Δt=0.01)

interactive_poincaresos_scan(X, 1; direction=1)