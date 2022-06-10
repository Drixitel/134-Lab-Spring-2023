# Required Functions
1. Need list or Database to take in Measured & Calculated values per droplet ionization
> Droplet Database: 
>> Idetifier: Droplet(i) for $i \in (1,2,3...)$ for a specific ionization<br>

>> Set:<br>
>> - V, b, g, p, $\eta_0$, $\rho$, d<br>

>> Measured/Computed:<br>
>> - $v_{y0i}$ = $\frac{ x_{i0}}{ t_{i0}}$<br>
>> - $a$<br>
>> - $\eta_{eff}$<br>
>> - $v_{yEi}$= $\frac{ x_{iE}}{ t_{iE}}$<br>
>> - $q$<br>


2. Need equation/function for radius (simplified for coding)
> $$a = \sqrt{\left(\frac{b}{2p}\right)^2 + \frac{9v_{y0}\eta_0}{2 \rho g}} -\left(\frac{b}{2p}\right)$$
> > $$a = \sqrt{\left(\alpha\right)^2 + \beta} -\left(\alpha\right)$$


3. Need equation/function for charge (simplified for coding)
> $$ q = \frac{4}{3}\pi \rho g \frac{d}{V}\left(
\sqrt{\left(\frac{b}{2p}\right)^2 + \frac{9v_{y0}\eta_0}{2 \rho g}} -\left(\frac{b}{2p}\right)
\right)^3 \cdot \frac{v_{yE}-v_{y0}}{v_{y0}}$$
> > $$ q = \frac{4}{3}\pi \rho g \frac{d}{V}a^3 \cdot \frac{v_{yE}-v_{y0}}{v_{y0}}$$

4. Need equations for Error propagation 
5. Need Graphs see images saved from speaking with the professor 


# Velocity propagation 
> $$V_f = V_r = V = \frac{x}{t}$$

# Error prop for Velocities 
> $$\sigma_V^2 = (\frac{\partial V }{\partial x})^2\cdot (\sigma_x)^2 + (\frac{\partial V }{\partial t})^2\cdot (\sigma_t)^2$$

>> $$\frac{\partial V }{\partial x} = \frac{1}{t}$$

>> $$\frac{\partial V }{\partial t} = \frac{-x}{t^2}$$

$$
\sigma_{vf}^2 = \sigma_{vr}^2=  (\frac{1}{t})^2\cdot (\sigma_x)^2 + (\frac{x}{t^2})^2\cdot (\sigma_t)^2
$$


# Radius Propagation
> $$a = \sqrt{\left(\frac{b}{2p}\right)^2 + \frac{9v_{y0}\eta_0}{2 \rho g}} -\left(\frac{b}{2p}\right)$$
> > $$a = \sqrt{\left(\alpha\right)^2 + \beta} -\left(\alpha\right)$$
> > $$a = \sqrt{\left(\alpha\right)^2 + \gamma \cdot v_{y0}} -\left(\alpha\right)$$

> $$\sigma_a^2 = (\frac{\partial a }{\partial v_{y0}})^2\cdot (\sigma_{v_{y0}})^2 $$

$$
\sigma_a^2 = \left(\frac{\gamma}{2\sqrt{\alpha^2 - \gamma \cdot v_{y0}}}\right)^2 \cdot (\sigma_{v_{y0}})^2 
$$


# Charge Propagation
> $$q = \frac{18\pi}{V}\cdot\sqrt{\frac{\eta_0^3}{2gp}}\cdot \left( \frac{1}{(1+\frac{b}{p a})}\right)^{\frac{3}{2}}\cdot d \cdot \sqrt{v_{y0}}\cdot(v_{yE}-v_{y0}) $$

>> $$q = \phi\cdot d \cdot\sqrt{v_{y0}}\cdot(v_{yE}-v_{y0}) $$

>> $$\sigma_q^2 = (\frac{\partial q }{\partial v_{y0}})^2\cdot (\sigma_{v_{y0}})^2 +(\frac{\partial q }{\partial v_{yE}})^2\cdot (\sigma_{v_{yE}})^2 +(\frac{\partial q }{\partial d})^2\cdot (\sigma_{d})^2 $$


$$
\sigma_q^2 = \left(\frac{\phi \cdot d \cdot ( v_{yE}-3v_{y0} )}{2\sqrt{v_{y0}}}\right)^2\cdot (\sigma_{v_{y0}})^2 +(\phi \cdot d \cdot \sqrt{v_{y0}})^2\cdot (\sigma_{v_{yE}})^2 +(\phi \cdot\sqrt{v_{y0}}\cdot(v_{yE}-v_{y0}))^2\cdot (\sigma_{d})^2 
$$


# Sample Variance Function
$$ 
s^2 = \frac{1}{n-1}\Sigma(x_i - \mu)^2
$$

> $s^2$ : Sample (finite) Variance<br>
$x_i$ : sample value<br>
$\mu$ : mean value of samples<br>
n : number of "bounces"<br>
>> e.g.: D1_ionization1 = [1(vf,vr), 2(vf,vr), 3(vf,vr)], n =  3 for 3 "bounce recordings" 

# Simple Average Vs Weighted Average 
> `Simple` is used if the uncertianty is consistent for each measure<br>
`Weighted` is used to incerase our uncertianty and would be due to each measurement having different uncertainies 

## Simple Average and it's Uncertianty 
$$
\bar{X} = \frac{1}{n}\Sigma x_i \\
$$
$$
\sigma_{\bar{X}} = \frac{\sigma_x}{\sqrt{n}}
$$
> where `$\sigma_x$` is the assigned uncertainty not a calculated one (?)


## Weighted 
$$
\bar{X} = \Sigma \left(\frac{x_i}{\sigma_{x_i}^2} \cdot \frac{1}{\Sigma \frac{1}{\sigma_{x_i}^2}} \right)
$$

>>> Q: is the uncertainty $\sigma_{\bar{X}}$ the same for both simple an weighted?<br>
>>> Q: major issue I see is each uncertainty per droplet would be assumed to be identical - I cannot remember if we can do that

# Compute new sigma per set of 3
> $$\sigma_q^2 = \frac{1}{\Sigma_i^3(\frac{1}{\sigma_{qi}^2})}$$


# Compute new Charge per set of 3 
> using weighted mean
>> $$ \bar{q} = \frac{\Sigma_i^3(\frac{q_i}{\sigma_i^2})}{\Sigma_i^3(\frac{1}{\sigma_{qi}^2})}
$$
