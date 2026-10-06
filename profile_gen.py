import numpy as np;
import matplotlib.pyplot as plt

def generate_prev_profile(chord, thickness=0.25, c_pts=200, le_max_t_percent = 0.04, te_max_t_percent=0.975):
    x_axis = np.linspace(0,chord, c_pts+1, endpoint=True);

    y_upper = np.zeros_like(x_axis)
    y_lower = np.zeros_like(x_axis)

    # LE bevel reaches max thickness at 4% chord
    # TE bevel tapers to a point starting at 97.5% chord

    half_t = 0.5*thickness

    LE_maxpt = round(c_pts*le_max_t_percent)
    TE_maxpt = round(c_pts*te_max_t_percent)

    LE_slope = (0.5*thickness)/(chord*le_max_t_percent)

    y_upper[0:LE_maxpt+1] = LE_slope * x_axis[0:LE_maxpt+1]    
    y_lower[0:LE_maxpt+1] = -y_upper[0:LE_maxpt+1]  

    y_upper[9:TE_maxpt] = half_t
    y_lower[9:TE_maxpt] = -half_t

    y_upper[TE_maxpt:] = half_t - (x_axis[TE_maxpt:] - chord*te_max_t_percent)
    y_lower[TE_maxpt:] = -y_upper[TE_maxpt:]

    # Selig format
    y_upper = np.flip(y_upper)
    upper = np.column_stack((np.flip(x_axis),y_upper))
    lower = np.column_stack((x_axis[1:], y_lower[1:]))

    coords = np.concatenate((upper,lower), axis=0)

    
    return(coords);

def profile_plot(coords):
    x = coords[:,0]
    y = coords[:,1]

    plt.plot(x,y, lw=2)
    plt.ylim(-2,2)
    plt.grid(True)
    plt.title(f"Chord = {coords[0,0]} inches")
    plt.ylabel("y, inch")
    plt.xlabel(f"x, inch")
    plt.show()


prev_coords = generate_prev_profile(5)
profile_plot(prev_coords)