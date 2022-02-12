# GreyCampus-Mod6

## SVM - Support Vector Machine
 
Used for classification and regression analysis. 
SVM can be used for 2D and 3D planes. 

### How it works : 
- identify the right hyper-plane
- select the hyperplane which segregates the classes better 
- the margins have to be as large as possible
- the support vectors are the most useful data points because they are the ones most likely to be incorrectly classified.

#### Terminology : 

**Support Vector Points** = the points closest to the hyperplane

**Margins** = the distance of the vectors from the hyperplane

**Hyperplane** = margin maximizing hyperplane MMH

### Advantages: 

- maximizes the margin between two classes in the feature space characterized by a ***kernel*** function
- robust with respect to high input dimension 

 *kernel is a mathematical function that transforms the data to the required form  
 
 Kernel Methods in SVM : 
 
 - Polynomial Kernel - used in image or signal processing
 - Gaussian Kernel - no prior knowledge of the data
 - Gaussian Radial Basis Function 
 - Laplace Radial Basic Function
 - Hyperbolic Tangent Kernel - used in NN/DL
 - Sigmoid Kernel- proxy for NN
 - Bessel Function of First Kind Kernel - removes cross terms in Maths
 - Anova Radial Basis Kernel - analysis of variance 
 - Linear Spline Kernel in 1D - sparse data, text identification, image detection

