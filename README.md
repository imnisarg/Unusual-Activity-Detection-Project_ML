# Unusual-Activity-Detection-Project_ML

# Purpose
This project aims to classify abnormal activities in a video . Technologies used are computer vision and deep learning techniques.

# Installation Instructions 
The libraries that need to be installed to run the code are
1) Numpy
2) cv2
3) tensorflow
4) keras
5) mss
6) PIL
7) pyxhook
8) pandas

# Process Flow
Training
1) A training video is prepared by capturing it or using an already available video.
2) From a video, we read a frame and also the next frame. We compute the flow matrix between these two frames.
3) The flow matrix between the two frames is in polar form representing the magnitude and angle of flow.
3) After computing a flow matrix for a frame , we divide the next frame into blocks ( no of blocks in a frame depend on the hyperparameters no of rows & columns per block) . For each block we compute the information for motion flow and hence finally compute the motion influence map. The results for each frame are combinedly stored in a motion influence map matrix.
Note:- Choosing large number of blocks will increase the computation time but it slightly gives better results. We have choosen blocks of size 20*20 in this project and it works well.
5) On this motion influence map matrix , we apply a Kmeans clustering for each block with k=5 and store the centres obtained for each block seperately.

Note:- Training is done on normal videos i.e the videos with no abnormal activities.

Testing
1) All the feature extraction steps till Kmeans clustering are repeated and a eucledian distance between the cluster obtained is compared with training cluster matrix.
2) If the eucledian distance for a particular block is greater than some threshold , then some unusual activity is detected in that block.
3) We identify all such blocks and show rectangles over the blocks with unusual activity detected.

# Further Possibilities
One can use various deep learning models as well for the above purpose, the code in models.py correspond to the different deep learning models that can be used to solve the problem.
