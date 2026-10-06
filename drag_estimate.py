import numpy as np

def wing_FF_incompressible(tc, xc=0.3):
    return 1+(0.6*tc)/(xc) + 100*(tc**4)

def get_friction_coeff(L, V, nu=1.57e-4,):
    Re_L = (V*L) / (nu)
    return 0.074/(Re_L**(0.2))

def estimate_skin_friction_drag(root, tip, height, V, t, steps=100, rho=0.002377):
    y = np.linspace(0,height,steps+1)
    midpt = (y[1:] + y[:-1])/2
    dy = height/steps
    c_y = ((tip-root)/height) * midpt + root # chord as a function of the position along fin span
    tc = t/(c_y)

    q = 0.5 * rho * (Vmax**2)

    Cf = get_friction_coeff(L=c_y,V=V)
    formfac = wing_FF_incompressible(tc)

    Df = (Cf)*(formfac)*(2*c_y*dy) 

    return np.sum(Df) * q

root = 7.0
tip = 3.0
height = 4.0

thickness = 0.25
Vmax = 312

# convert units in inches to feet
thickness = thickness/12
root = root/12
tip = tip/12
height = height/12

drag = estimate_skin_friction_drag(root,tip,height,Vmax,thickness)
print(drag)

