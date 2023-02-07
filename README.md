# NLP_assignment2
This repository is for the second assignment of NLP course (COMP 8730 ). We evaluate n-gram language models on spell correction problem to see how they perform. 

## Setup

 you need to download or clone the repository. You can use the code below to clone it.

     git clone https://github.com/rezaBarzgar/NLP_assignment2.git

install the required libraries by running the following code:

    pip install -r requirements.txt
    
  The last step of setup is installing pytrec_eval for the evaluation part
  

    pip install pytrec-eval
    
## run the project!
for runing the project and reproducing the results you can run the following codes:

    cd /src
    python run main.py


## Results


The results are shown as the following plots 

Horizental axis: 0 -> corpus is only news categories of brown, 14 -> corpus is the whole brown corpus

vertical: Success score 

![alt text](https://github.com/rezaBarzgar/NLP_assignment2/blob/master/data/1-gram.png)
![alt text](https://github.com/rezaBarzgar/NLP_assignment2/blob/master/data/2-gram.png)
![alt text](https://github.com/rezaBarzgar/NLP_assignment2/blob/master/data/3-gram.png)
![alt text](https://github.com/rezaBarzgar/NLP_assignment2/blob/master/data/5-gram.png)
![alt text](https://github.com/rezaBarzgar/NLP_assignment2/blob/master/data/10-gram.png)
