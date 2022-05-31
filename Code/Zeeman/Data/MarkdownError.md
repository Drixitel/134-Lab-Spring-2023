# First Error: Peak Selection 
> Criteria: narrow peak $\pm$ 2 pixels, Wide peak $\pm$ 3.5 pixels 

> Measure $x_i$ with $\sigma_{x_i}$
>> Propagate $\sigma_{x_i}$ to $\sigma_{\Delta \text{Yvalues}}$
- Error prop Formula for $f(x,t)$

> $$\sigma_f^2 = (\frac{\partial f }{\partial x})^2\cdot (\sigma_x)^2 + (\frac{\partial f }{\partial t})^2\cdot (\sigma_t)^2$$

## 1. 
$$
\text{Diameter}= D = x_f - x_i 
$$

$$
\sigma_D^2 = (1)^2 (\sigma_{x_f})^2 + (-1)^2 (\sigma_{x_i})^2\\
$$

>$$
\sigma_D^2 = (\sigma_{x_f})^2 +  (\sigma_{x_i})^2\\
$$

## 2. 
$$
\text{Radius}= R = \frac{D}{2}
$$

$$
\sigma_R^2 = (\frac{1}{2})^2 (\sigma_D)^2
$$
>$$
\sigma_R = \frac{1}{2} (\sigma_D)
$$


## 3.
-  $f = 135\cdot 10^{-3}$ meters 
- focal length 135 mm
- For small angles $\tan(\theta) = \theta$
$$
\text{Angle} = \theta = \frac{R}{f} 
$$

>$$
\sigma_{\theta}^2 = (\frac{1}{f})^2 (\sigma_R)^2
$$

## 4. 
$$
(\theta_a)^2- (\theta_b)^2 = \frac{2}{\bar{E}}\cdot (E_a - E_b) = \frac{2}{\bar{E}}\cdot\frac{1}{2} \mu_0 B
$$

- $ \Delta E' = (E_a - E_b) = \frac{1}{2} \mu_0 B$
- $\bar{E} = 3.638\cdot 10^{-12}$ erg
$$
\Delta E' = \frac{\bar{E}}{2}\cdot (\theta_a)^2- (\theta_b)^2
$$
$$
\Delta E' = \frac{\bar{E}}{2}\cdot(\theta_a)^2- \frac{\bar{E}}{2}\cdot(\theta_b)^2
$$

$$
\sigma_{\Delta E'}^2= (\bar{E} \cdot \theta_a)^2 (\sigma_{\theta_a})^2 +(-\bar{E} \cdot\theta_b)^2 (\sigma_{\theta_b})^2
$$

>$$
\sigma_{\Delta E'}^2= (\bar{E} \cdot \theta_a)^2 (\sigma_{\theta_a})^2 +(\bar{E} \cdot\theta_b)^2 (\sigma_{\theta_b})^2
$$

## 5. 
Add in quadrature the error in the Magnetic Field
$$
\text{True Error} = \sigma_{\Delta \text{Yvalues}} = \sqrt{\frac{\sigma_{\Delta E'}^2+ \sigma_B^2}{2}}
$$

# Error prop for $\theta^2$ 
$$
\sigma_{\theta^2}^2 = (2\theta)^2(\sigma_{theta})^2
$$
$$
\sigma_{\theta^2} = (2\theta)(\sigma_{theta})
$$