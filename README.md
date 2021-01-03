# M2-PIXEL-PALETTE

The purpose of this individual project is to color an image with very precise rules with a challenge on the optimization/complexity and understandability of the code, divided into simple and explicit functions.

At the beginning, the image, of scalable size, is totally black. It is necessary to have a list of colors, all different and distributed to cover in a regular way the possible colors. Typically, if we needed $256^{3}$ colors, it would be all the combinations for red/green/blue between 0 and 255. Here we need fewer colors. Then we need to blend this list to have a random order.

The first color in the list will be put on a pixel in the center of the image. Then, for each successive color C in the list, it will be assigned to a pixel which is always free (black) and which is adjacent to an already colored pixel, of color C', so that C' is the closest possible color to C. Note: It is possible to choose the distance between colors as you wish. Here the Euclidean distance between two vectors of dimension 3 (rgb) has been chosen.

Therefore, at any moment in the image, there are "border" pixels that are colored but have one or more free pixels as neighbors. The next color in the list must be placed against the border pixel that most closely matches it, until the image is filled.

A variant has also been implemented, which consists in the image having a dominant color and therefore being filled by a gradient of the latter.

Sample images of the results of the normal version as well as of the variant are available in the "images" folder.