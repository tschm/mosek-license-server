import marimo

__generated_with = "0.10.5"
app = marimo.App(width="medium")


@app.cell
def _():
    from mosek_license import license

    license.upsert()
    return (license,)


@app.cell
def _():
    import mosek.fusion as fusion

    with fusion.Model("cqo1") as M:
        # this is optional, just to be safe...
        # M.putlicensepath(license.current())

        x = M.variable("x", 3, fusion.Domain.greaterThan(0.0))
        y = M.variable("y", 3, fusion.Domain.unbounded())

        # Create the aliases
        # z1 = [ y[0],x[0],x[1] ]
        # and z2 = [ y[1],y[2],x[2] ]
        z1 = fusion.Var.vstack(y.index(0), x.slice(0, 2))
        z2 = fusion.Var.vstack(y.slice(1, 3), x.index(2))

        # Create the constraint
        # x[0] + x[1] + 2.0 x[2] = 1.0
        M.constraint(
            "lc", fusion.Expr.dot([1.0, 1.0, 2.0], x), fusion.Domain.equalsTo(1.0)
        )

        # Create the constraints
        # z1 belongs to C_3
        # z2 belongs to K_3
        # where C_3 and K_3 are respectively the quadratic and
        # rotated quadratic cone of size 3, i.e.
        # z1[0] >= sqrt(z1[1]^2 + z1[2]^2)
        # and  2.0 z2[0] z2[1] >= z2[2]^2
        qc1 = M.constraint("qc1", z1, fusion.Domain.inQCone())
        M.constraint("qc2", z2, fusion.Domain.inRotatedQCone())

        # Set the objective function to (y[0] + y[1] + y[2])
        M.objective("obj", fusion.ObjectiveSense.Minimize, fusion.Expr.sum(y))

        # Solve the problem
        M.solve()

        # Get the linear solution values
        solx = x.level()
        soly = y.level()

        # Get conic solution of qc1
        qc1lvl = qc1.level()
        qc1sn = qc1.dual()

    return qc1lvl, qc1sn, solx, soly


@app.cell
def _(qc1lvl, qc1sn, solx, soly):
    print("x1,x2,x3 = %s" % str(solx))
    print("y1,y2,y3 = %s" % str(soly))
    print("qc1 levels                = %s" % str(qc1lvl))
    print("qc1 dual conic var levels = %s" % str(qc1sn))
    return


if __name__ == "__main__":
    app.run()
