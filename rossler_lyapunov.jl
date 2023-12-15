using ChaosTools, Plots, DynamicalSystems

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

as = 0.2:0.00001:0.3;
λs = zeros(length(as), 3)

# Since `DynamicalSystem`s are mutable, we need to copy to parallelize
systems = [deepcopy(rossler) for _ in 1:Threads.nthreads()-1]
pushfirst!(systems, rossler)

Threads.@threads for i in eachindex(as)
    system = systems[Threads.threadid()]
    set_parameter!(system, 1, as[i])
    λs[i, :] .= lyapunovspectrum(system, 10000; Δt = 0.1, show_progress=true)
end

scene = plot(as, λs[:, 1])
plot!(scene, as, λs[:, 2])
plot!(scene, as, λs[:, 3])


# fig = Figure()
# ax = Axis(fig[1,1]; xlabel = L"a", ylabel = L"\lambda")
# for j in 1:2
#     lines!(ax, as, λs[:, j])
# end
# fig