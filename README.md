# Cat vs. Dog Image Classification Using TensorFlow

This project demonstrates how to build an image classification model using TensorFlow to classify images of cats and dogs. The model employs a Convolutional Neural Network (CNN) architecture based on Xception, pre-trained on the ImageNet dataset and fine-tuned on the Cats vs. Dogs dataset. This project highlights the use of transfer learning and fine-tuning techniques to achieve high classification accuracy.

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Training and Evaluation](#training-and-evaluation)
- [Usage](#usage)
- [Results](#results)
- [Demo](#demo)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started

Follow the instructions below to set up and run the project on your local machine.

### Prerequisites

- Python 3.6 or later
- TensorFlow 2.5 or later
- Matplotlib
- NumPy

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/cat-vs-dog-classification.git
    cd cat-vs-dog-classification
    ```

2. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Dataset

The dataset used in this project is the "Microsoft Cats and Dogs" dataset, containing 25,000 images of cats and dogs (12,500 each). The images are of varying sizes and resolutions, split into training and testing sets. The dataset can be downloaded from [here](https://www.microsoft.com/en-us/download/details.aspx?id=54765) or using the following command:

```bash
!curl -O https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip
```

After downloading, unzip the file and specify the path to the extracted directory in the `data_dir` variable in the code.

**Note:** This dataset is intended for research purposes only and should not be used for commercial purposes without permission from Microsoft.

## Model Architecture

The model is based on the Xception architecture, which is a highly efficient CNN model that utilizes depthwise separable convolutions to reduce the number of parameters without sacrificing performance. The Xception model was fine-tuned on the Cats vs. Dogs dataset to adapt it to the specific task of binary image classification.

## Training and Evaluation

The model was trained using TensorFlow on a subset of the dataset, with the remaining images used for validation and testing. Key techniques used include:

- **Transfer Learning:** Leveraging the pre-trained Xception model on the ImageNet dataset.
- **Fine-Tuning:** Adjusting the last few layers of the pre-trained model to improve performance on the specific dataset.

The training process is documented in the `Model_1.ipynb` Jupyter notebook, which provides detailed explanations and code for each step.

## Usage

To use the model, open the `Model_1.ipynb` notebook and follow the instructions provided in each cell. The other two models (`Model_2.ipynb` and `Model_3.ipynb`) utilize similar functions with slight variations in the model architecture and training process. Feel free to experiment by modifying the models or adjusting hyperparameters.

## Results

The final model achieved an accuracy of **XX%** on the test set, demonstrating its effectiveness in distinguishing between cats and dogs. (Replace **XX%** with your actual result)

## Demo

You can interact with a live demo of the model via [this link](#). (Add the actual link once the demo is set up)

Alternatively, you can watch a video demonstration [here](#). (Add the video link)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the [TensorFlow Cats and Dogs Tutorial](https://www.tensorflow.org/tutorials/images/classification).
- The Xception model architecture is from the paper ["Xception: Deep Learning with Depthwise Separable Convolutions"](https://arxiv.org/abs/1610.02357) by François Chollet.
- Thanks to Microsoft for providing the [Cats and Dogs Dataset](https://www.microsoft.com/en-us/download/details.aspx?id=54765).

---