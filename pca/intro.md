Hello, and welcome to this course on principal component analysis.

PCA belongs to the class of algorithms that perform something known as low rank approximation.
As we know, the rank of a matrix is the number of linearly independent columns and rows.
And generally the rank of a matrix corresponds to how much redundancy there is in the dataset.
If some columns in a matrix can be represented as linear combinations of other columns, then we can conclude that those columns are unnecessary.
If you remember, we had addressed this phenomenon in the module on linear regression - which we called multicollinearity.
We had discussed how linear regression fails when the data has multicollinearity - or in other words, linear regression fails if the data is low-rank.
We had also talked about how PCA can help remove this multicollinearity, and render the dataset full rank by removing the dependency.

The geometrical interpretation of PCA is even more interesting. Imaging you are a photographer and you are covering a press conference in an auditorium.
Let's say that there's a stage, and the speakers sitting on the stage in a single line. Now the question is - what is the best position for you to occupy on the stage,
so that you are able to photograph all the speakers properly.

Now say that the speakers are sitting like this, and you are standing in the same line here. This is a bad position, because you'll be able to see the profile of only one person,
and everyone else will be eclipsed.

But say you were standing right in front of the stage, along the perpendicular bisector of the line of the speakers, then you'd be able to see everyone properly. So by choosing that position,
you are essentially maximizing the information that you are receiving. That happens because you are selecting a position that maximizes the variance in your data. So geometrically, that's what
PCA does - it gives you the best low dimensional camera angle into your data. This module is all about how that works and how to use it.

We will start with some elementary statistics and vector algebra required to motivate PCA before dealing with the PCA algorithm in earnest. And as in the previous modules,
we will first look at the numpy / pandas / scikit-learn version of PCA, and then migrate the same concepts to big data with spark and MLlib.

As we will see, PCA can be a very powerful technique - firstly because it's cheap to use. Like linear regression, it's just a series of matrix operations. And secondly, PCA is unsupervised,
so a asuccessful application of it can all by itself reveal some very intersting insights about your data, even without resorting to machine learning.
And finally it's an indispensable visualization tool because it compresses data into fewer dimensions and you can pick two or three dimensions to visualize it.

I hope you enjoy this module, and see you in the next video.
