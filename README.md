# Cat vs Dog Image Classification using TensorFlow

This project demonstrates how to build an image classification model using TensorFlow to classify cats and dogs. The model uses a convolutional neural network (CNN) architecture called Xception, which has been pre-trained on the ImageNet dataset and fine-tuned on the cats vs dogs dataset.

## Getting Started

### Prerequisites

- Python 3.6 or later
- TensorFlow 2.5 or later
- Matplotlib
- NumPy

### Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/cat-vs-dog-classification.git
cd cat-vs-dog-classification
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

## Dataset

The dataset used in this project is the "Microsoft Cats and Dogs" dataset, which can be downloaded from [here](https://www.microsoft.com/en-us/download/details.aspx?id=54765) or using the following command:

```
!curl -O https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip
```

The dataset contains 25,000 images of cats and dogs (12,500 each) and is split into training and testing sets. The images are of varying sizes and resolutions.

To use the dataset, you will need to unzip the file and specify the path to the extracted directory in the `data_dir` variable in the code.

Please note that this dataset is intended for research purposes only and should not be used for commercial purposes without permission from Microsoft.


### Usage

For how to make and use the model open the Model_1 jupyter notebook and read the documentations provided there cell by cell. The other two models rely mostly on the same functions expect for the changes in the model structure and minor changes to the training process. Feel free to experiment on your own by changing the models or adjusting hyperparameters.
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the [TensorFlow Cats and Dogs Tutorial](https://www.tensorflow.org/tutorials/images/classification)
- The Xception model architecture is from the paper ["Xception: Deep Learning with Depthwise Separable Convolutions"](https://arxiv.org/abs/1610.02357) by François Chollet.
