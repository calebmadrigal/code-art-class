# Code Art Class

## Lesson 2: Draw a line

In this lesson, we'll learn how to draw a line using a bunch of points.

<img src="line.png" width=500>

Let's start by drawing a diagonal line from the top left to the bottom right. If you look at the screen coordinates image below, you can notice that if we just set each of the pixels where x==y, we'll draw a line.

![screen coordinates](screen_coordinates.png)

We could do this by individually setting each pixel like this:

    img1.point((0, 0), fill ='red')
    img1.point((1, 1), fill ='red')
    img1.point((2, 2), fill ='red')
    img1.point((3, 3), fill ='red')
    img1.point((4, 4), fill ='red')

Note that we just use the same value for both x and y. But in order to do this in a simpler way, we can just use a `for` loop like this:

    for i in range(100):
        img1.point((i, i), fill ='red')

## Challenges

For the following challenges, modify the `line.py` file...

### Challenge 1

Draw a second line somewhere using the same techniques. Some ideas to try:

* You could try adding some value to either the `x` or `y` coordinates like:

    `img1.point((i+10, i), fill ='red')`

