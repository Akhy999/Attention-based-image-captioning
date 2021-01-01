# Attention-based-image-captioning

The above code is regarding attention based image captioning

This model is based on the Encoder-Decoder framework with attention layer in the middle

Here the convolution layer outputs of VGG16 model are sent into a fully connected layer and then are sent as inputs of Attention layer, thus this acts as the encoder

The decoder is a RNN based on GRUs 

The model is trained on the Flicker8k dataset containing 8091 images mapped to 40455 captions (5 each)

Thus training the model on tuning the hyper parameters yielded in results with train loss of 0.012 and a test loss of 0.028 and the Bleu-1 score of 0.558 (Bleu : 0.13)

![Alt text](./images/Screenshot (106).png)
![Alt text](./images/Screenshot (109).png)
