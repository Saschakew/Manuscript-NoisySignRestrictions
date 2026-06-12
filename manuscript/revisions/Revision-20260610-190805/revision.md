# Revision notes

Source milestone: M47 standard-DW proof gate audit

1) We need to change the manuscript to the unit variance assumption Var(epsilon)=1! Never use diag(B)=1 normalization. We mixed these things up in the draft and in my comments inside the draft, you can see where we need to adjust!

2) I want a standard GMM estimator with the usual efficient weighting matrix. We currently have moment conditions like E\{z_1(B)^2z_2(B)^2\}
-s_{11}(B)s_{22}(B)-2s_{12}(B)^2\\
E\{z_1(B)z_2(B)^3\}-3s_{22}(B)s_{12}(B) where the s depent on the B and the variance of the noise, correct? so instead of computing s as a sample average, cant we just tread the variances of the noise as a parameter we estimate and for a given noise variance parameter, we can estimate 
