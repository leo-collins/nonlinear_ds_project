using BifurcationKit, Plots, Setfield

function rossler!(u, p)
    a, b, c, = p
    x, y, z = u

    [
        -y-z,
        x + a*y,
        b*x + z*(x-c)
    ]
end

recordFromSolution(x, p) = (X = x[1], Y = x[2], Z = x[3])

par = (a=0.2, b=0.3, c=4.9)
u0 = [0.0, 0.0, 0.0]

prob = BifurcationProblem(rossler!, u0, par, (@lens _.a), record_from_solution=recordFromSolution)

opts_br = ContinuationPar(p_min=0.0, p_max=0.4, dsmax=0.001, dsmin=0.00001, ds=0.0001,
detect_bifurcation=3, nev=3, max_steps=1000, n_inversion=10)

br = continuation(prob, PALC(), opts_br; bothside=true)

opts_po = ContinuationPar(p_min=0.01, p_max=0.4, dsmax=0.01, dsmin=0.0001, ds=0.001,
detect_bifurcation=3, nev=3, max_steps=10000, n_inversion=4)

br_po = continuation(br, 2, opts_po, PeriodicOrbitOCollProblem(20, 5); δp=0.00001, record_from_solution=recordFromSolution)
# br_po = continuation(br, 2, opts_po, PeriodicOrbitTrapProblem(M=200; jacobian=:Dense); ampfactor=10.0, δp=0.002, record_from_solution=recordFromSolution)

br_po_pd = continuation(br_po, 1, opts_po; ampfactor = 1.0, δp = 0.001, record_from_solution=recordFromSolution)

br_po_pd_bp = continuation(br_po_pd, 1, opts_po; ampfactor = 0.1, δp = 0.01)

# plot(br, br_po, br_po_pd, vars=(:param, :X))
plot(br, br_po, br_po_pd, br_po_pd_bp)
