# Problem
>This is an image of a disk that once contained several files. They were deleted prior to imaging, unfortunately. To find the flag, we're going to need to bring some of them back from the dead. The flag is actually broken up between two of them. Carve the files out of the image and restore any missing file headers to find the pieces to reassemble.

description from website, the last line provided hint to solve problem.
- the file we want is image only
- we may need to fix header

# Solution
use command to extract all the image.
`binwalk --dd "image:jpg" DF3.001`
The command will also fix the header for us, here is the two image:
![first_pic](./assests/368D2.jpg)
![second_pic](./assests/388CE.jpg)

flag: `poctf{uwsp_5h1v3r_m3_71mb3r5}`

