# Attention-based-image-captioning

The above code is regarding attention based image captioning

This model is based on the Encoder-Decoder framework with attention layer in the middle

Here the convolution layer outputs of VGG16 model are sent into a fully connected layer and then are sent as inputs of Attention layer, thus this acts as the encoder

The decoder is a RNN based on GRUs 

The model is trained on the Flicker8k dataset containing 8091 images mapped to 40455 captions (5 each)

Thus training the model on tuning the hyper parameters yielded in results with train loss of 0.012 and a test loss of 0.028 and the Bleu-1 score of 0.558 (Bleu : 0.13)

Here are the few predictions from the model

<p align="center">
  Original Image
</p>
<p align="center">
  <img src="/images/1897025969_0c41688fa6.jpg" width="350" title="original image">
</p>
<p align="center">
  <img src="/images/Screenshot%20(106).png"  title="original image">
</p>
<p align="center">
  Bleu-1 Score
</p>
<p align="center">
  <img src="/images/Screenshot%20(109).png"  title="original image">
</p>

<p align="center">
  Original Image
</p>
<p align="center">
  <img src="/images/3453259666_9ecaa8bb4b.jpg" width="350" title="original image">
</p>
<p align="center">
  <img src="/images/Screenshot%20(107).png"  title="original image">
</p>
<p align="center">
  Bleu-1 Score
</p>
<p align="center">
  <img src="/images/Screenshot%20(110).png"  title="original image">
</p>

<p align="center">
  Original Image
</p>
<p align="center">
  <img src="/images/3220140234_e072856e6c.jpg" width="350" title="original image">
</p>
<p align="center">
  <img src="/images/Screenshot%20(108).png"  title="original image">
</p>
<p align="center">
  Bleu-1 Score
</p>
<p align="center">
  <img src="/images/Screenshot%20(111).png"  title="original image">
</p>

