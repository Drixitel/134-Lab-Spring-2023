# <p style="text-align: center;">  Error Propagation </p>

# Calculate $R_T$ and its error prop
- <span style="color:red"> **Calculation in Excel**</span>


$$
R_T = R + R_L
$$

> $$\sigma_{R_T}^2 = \left(\frac{\partial R_T}{\partial R} \right)^2 \cdot \sigma_{R}^2 + \left(\frac{\partial R_T}{\partial R_L} \right)^2 \cdot \sigma_{R_L}^2$$

> $$\sigma_{R_T}^2 = \left( 1 \right)^2 \sigma_{R}^2 + \left( 1 \right)^2 \sigma_{R_L}^2$$

$$
\sigma_{R_T}^2 = \sigma_{R}^2 +  \sigma_{R_L}^2
$$


# Calculate the period $P$ and its error 
- <span style="color:red">**No longer needed**</span>

$$
P = t_1-t_2
$$

> $$\sigma_P^2 = \left(\frac{\partial P}{\partial t_1} \right)^2 \cdot \sigma_{t_1}^2 + \left(\frac{\partial P}{\partial t_2} \right)^2 \cdot \sigma_{t_2}^2$$

> $$\sigma_P^2 = \left( 1 \right)^2 \sigma_{t_1}^2 + \left( -1 \right)^2 \sigma_{t_2}^2$$

$$
\sigma_P^2 = \sigma_{t_1}^2 +  \sigma_{t_2}^2
$$

# Calculate the phase $\phi$ and its error

- td = Time difference measured by oscilloscope 
- <span style="color:red">**Calculation in Excel**</span>


$$
\phi = 360 \cdot \frac{td}{P} = deg
$$

$$
\phi = 2\pi \cdot \frac{td}{P} = rad
$$

> $$\sigma_\phi^2 = \left(\frac{\partial \phi}{\partial td} \right)^2 \cdot \sigma_{td}^2 + \left(\frac{\partial \phi}{\partial P} \right)^2 \cdot \sigma_{P}^2$$

$$ 
\sigma_\phi^2 = \left(360 \cdot \frac{1}{P}\right)^2 \cdot \sigma_{td}^2 + \left(360 \frac{td}{P^2} \right)^2\cdot \sigma_{P}^2
$$

# Calculate resonant frequency $\omega_0$ and its error prop
>> This is from known characteristics (ideal)
- <span style="color:red"> **Requires code due to complextity** </span>

$$
w_0 = \frac{1}{\sqrt{LC}}
$$

> $$\sigma_{\omega_0}^2 = \left(\frac{\partial \omega_0}{\partial L} \right)^2 \cdot \sigma_{L}^2 + \left(\frac{\partial \omega_0}{\partial C} \right)^2 \cdot \sigma_{C}^2$$

> $$\sigma_{\omega_0}^2 = \left(\frac{-1}{2\cdot L^{\frac{3}{2}}\cdot C^{\frac{1}{2}}} \right)^2 \cdot \sigma_{L}^2 + \left(\frac{-1}{2\cdot L^{\frac{1}{2}}\cdot C^{\frac{3}{2}}}\right)^2 \cdot \sigma_{C}^2$$

 $$\sigma_{\omega_0}^2 = \left(\frac{1}{2\cdot L^{\frac{3}{2}}\cdot C^{\frac{1}{2}}} \right)^2 \cdot \sigma_{L}^2 + \left(\frac{1}{2\cdot L^{\frac{1}{2}}\cdot C^{\frac{3}{2}}}\right)^2 \cdot \sigma_{C}^2$$



# Calculate the resonant frequency $\omega_0$ and its error 
>> This is from the PDE (real)
- <span style="color:red"> **no longer used** </span>

$$
\tan(\phi) = \frac{\omega^2 - \omega_0^2}{\omega \Gamma}
$$

$$
\omega_0 = \sqrt{\omega^2 -\tan(\phi)\omega\Gamma} 
$$

$$
\omega_0 = \sqrt{\omega^2 -\tan(\phi)\frac{R_T}{L}\omega} 
$$

> minimum
>> $$\omega^2 \geq \tan(\phi)\omega\Gamma $$

>> $$\omega \geq \tan(\phi)\Gamma$$

> $$\sigma_{\omega_0}^2 = \left(\frac{\partial \omega_0}{\partial w} \right)^2 \cdot \sigma_{w}^2 + \left(\frac{\partial \omega_0}{\partial \phi} \right)^2 \cdot \sigma_{\phi}^2 + \left(\frac{\partial \omega_0}{\partial R_T} \right)^2 \cdot \sigma_{R_T}^2 + \left(\frac{\partial \omega_0}{\partial L} \right)^2 \cdot \sigma_{L}^2$$



$$
\sigma_{\omega_0}^2 = \left(\frac{2L\omega -\tan{\phi}R_T}{2\sqrt{L}\cdot \sqrt{L\omega^2 -\tan(\phi)R_T\omega}}\right)^2 \cdot \sigma_{w}^2
$$
$$
+ \left(\frac{-\sec^2(\phi)R_T\omega}{2\sqrt{L}\sqrt{L\omega^2-\tan(\phi)R_T\omega}}\right)^2 \cdot \sigma_{\phi}^2
$$

$$
+ \left(\frac{-\tan(\phi)\omega}{2\sqrt{L}\sqrt{L\omega^2-\tan(\phi)R_T\omega}}\right)^2 \cdot \sigma_{R_T}^2 
$$
$$
+ \left(\frac{\tan(\phi)R_T\omega}{2L^{\frac{3}{2}}\sqrt{L\omega^2 - \tan(\phi)R_T \omega}} \right)^2 \cdot \sigma_{L}^2
$$


# Need: Plot $\phi$ Vs. $\omega$ and Amplitude Vs. $\omega$
