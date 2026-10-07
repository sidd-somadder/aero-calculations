import numpy as np;
import matplotlib.pyplot as plt
from pathlib import Path

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
    TE_slope = half_t / (chord * (1 - te_max_t_percent))

    y_upper[0:LE_maxpt+1] = LE_slope * x_axis[0:LE_maxpt+1]    
    y_lower[0:LE_maxpt+1] = -y_upper[0:LE_maxpt+1]  

    y_upper[LE_maxpt+1:TE_maxpt] = half_t
    y_lower[LE_maxpt+1:TE_maxpt] = -half_t

    y_upper[TE_maxpt:-1] = half_t - TE_slope*(x_axis[TE_maxpt:-1] - chord*te_max_t_percent)
    y_lower[TE_maxpt:-1] = -y_upper[TE_maxpt:-1]

    y_upper[-1] = 0
    y_lower[-1] = 0

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

def save_profile_coords(coords, title="profile"):
    Path("saved_profile_coords").mkdir(exist_ok=True)

    filename = f"{title}.dat"

    filepath = Path("saved_profile_coords") / filename

    with open(filepath, 'w') as f:
        for row in coords:
            f.write(f"  {row[0]:.6e}  {row[1]:.6e}\n")

    print(f"Profile coordinates saved to {filepath}.")

prev_coords = generate_prev_profile(5)
profile_plot(prev_coords)
save_profile_coords(coords=prev_coords,title="prev_profile_5inchchord")