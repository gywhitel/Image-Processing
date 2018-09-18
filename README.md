# Computer Vision
This repository mainly record the code of EQ2425 *Analysis and Search of Visual Data* Projects.
We mainly used openCV-Python to do the job. Maybe implement those tasks in Matlab later.
## Project I
- Feature detection by SIFT and SURF
- Test the robustness after image transformation
- Feature matching
## Project II
This project is basically to implement the algorithm proposed by Josef, Andrew in ***A Text Retrieval Approach to Object Matching in Videos***. More details can be found in ***Mobile Visual Search*** by Giord .etc

## Image retrieval
### TF-IDF(Term Frequency-Inversed Document frequency)
A document can be represented by a vector of word frequencies.
$$Doc = [f_{t1}, f_{t2},...,f_{tn}]$$
Similarly, an image can be represented by a vector of visual words(descriptors)
But consider that every descriptor is likely to appear only once, we modify the descriptor to weighted(ITF) descriptors.
Visual word seems something meaningful. 
Thus, an image is represented by a vector of TF-IDF., which is like spatial coordinates when clustering.

$$tf_d-ifd_t = n_{id}/ n_d \times log(N/ df_t) $$
![](https://i.stack.imgur.com/XJAYK.png)

- Image Feature extraction
  - Traverse images in folders
  - extract the object index by regular expression filter
  - store all the feature in a text file
- Constract vocabulary tree
