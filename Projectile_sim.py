import math
import matplotlib.pyplot as plt
#Mass And Radius(Physical Properties Of Object)
mass = 5
Radius = .1
#Intial Pos No Drag
xi = 0
yi = 0
#Intial Pos Drag
xi_drag = 0
yi_drag = 0
#Intial Velocity
v = 50
#Angel Of Projection
A = 60
#Time
Time = []
dt = .0001 
t = 0
#Data For Graphing
  #Drag Data
KE_Data_drag = []
PE_Data_drag = []
xi_data_drag = []
yi_data_drag = []
  #No Drag Data
xi_data = []
yi_data = []
KE_Data = []
PE_Data = []
i = 0
#Spilting Velocity Vectors
vsin = v * math.sin(A * math.pi/180)
vcos = v * math.cos(A * math.pi/180)
vsin_drag = v * math.sin(A * math.pi/180)
vcos_drag = v * math.cos(A * math.pi/180)
#Calculating Time Of Flight
T = 2 * vsin / 9.8
while True:
    #Vecolity At Every Point
    v = math.sqrt(vsin**2 + vcos**2) 
    v_drag = math.sqrt(vsin_drag ** 2 + vcos_drag**2)
    #Ke and Pe Calculation
    ke = 1/2 * (mass) * (v**2)
    ke_drag = 1/2 * (mass) * (v_drag**2)
    pe = mass * 9.8 * yi
    pe_drag = mass * 9.8 * yi_drag
    #Calculating Air Resistance
    F_drag = .5 * .47 * math.pi * (Radius**2) * (v_drag**2) * 1.225
    Fx = -F_drag * (vcos_drag / v_drag)
    Fy = -F_drag * (vsin_drag / v_drag)
    # Update Position
    xi += dt * vcos
    yi += dt * vsin
    xi_drag += dt * vcos_drag
    yi_drag += dt * vsin_drag
    #Adding The Data
    xi_data_drag.append(xi_drag)
    yi_data_drag.append(yi_drag)
    xi_data.append(xi)
    yi_data.append(yi)
    KE_Data.append(ke)
    PE_Data.append(pe)
    KE_Data_drag.append(ke_drag)
    PE_Data_drag.append(pe_drag)
    Time.append(t)
    # Update Velocity
      #Updating Velocity With Drag
    vcos_drag += (Fx / mass) * dt
    vsin_drag += (Fy / mass) * dt - 9.8 * dt
      #Updating Velocity Without Drag
    vsin -= 9.8 * dt
    #Breaking On Basis Of Velocity in Y
    if yi < 0 or yi_drag < 0:
        break
    i += 1
    t += dt
#Calualting Time of Flight With Drag
T_Drag = i*dt
#Caluating Slope Can Be Used In Future
for i in range(len(xi_data) - 1):
    m = (yi_data[i + 1] - yi_data[i])/(xi_data[i + 1] - xi_data[i])
print(T)
print(T_Drag)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(xi_data_drag, yi_data_drag, label="With Drag")
ax1.plot(xi_data, yi_data, label="No Drag")
ax1.set_xlabel("x (m)")
ax1.set_ylabel("y (m)")
ax1.set_title("Projectile Motion Comparison")
ax1.legend()

ax2.plot(Time, PE_Data, label="No Drag PE")
ax2.plot(Time, KE_Data, label="No Drag KE")
ax2.plot(Time, PE_Data_drag, label="With Drag PE")
ax2.plot(Time, KE_Data_drag, label="With Drag KE")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Energy (J)")
ax2.set_title("Energy vs Time")
ax2.legend()

plt.tight_layout()
plt.show()
