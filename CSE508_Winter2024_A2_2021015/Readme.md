# CSE508 Information Retrieval
### Winter 2024
## Report Assignment-2
Ankit Kumar 2021015

- I have edited the A2 - Data.csv file and added the 0th column as the 'Serial' column
- used the first image of the url list to rank the images and text similarity

## Image Processing

- Preprocessing Techniques: I've used resizing, contrast adjustment, brightness adjustment, exposure alterations, and random flips/mirroring.
## Image Feature Extraction

- Model: I've used ResNet50 (pre-trained on ImageNet) for feature extraction.
- Normalization: I've normalized the extracted image features.
## Text Feature Extraction

- Preprocessing Techniques: My preprocessing includes lowercasing, tokenization, stop word removal, and stemming/lemmatization.
- TF-IDF: I've calculated TF-IDF scores for the text reviews.
## Image and Text Retrieval

- Similarity Metric: I'm using cosine similarity to match images and text.
- Data Structures: I'm assuming you're using basic data structures (like lists or dictionaries) for this.
## Combined Retrieval

- Approach: I average the cosine similarity scores from image and text retrieval.  
composite_similarity = (simlarity_score + image_similarity)/2
## Results and Analysis

Results: Image similarity is the superior retrieval method due to the consistent visual nature of products. Text reviews, even for similar products, can exhibit significant variation

Furthermore, I think since most of them are guitar images or guitar related accessories, the image similarity is more accurate than text similarity since reviews can be subjective and can vary from person to person.

Challenges:
- One missing review
- Links were giving 404 error

```
Serial 2235. URL: ['https://images-na.ssl-images-amazon.com/images/I/71F3npeHUDL._SY88.jpg', 'https://images-na.ssl-images-amazon.com/images/I/71wHUWncMGL._SY88.jpg']
Serial 3317. URL: ['https://images-na.ssl-images-amazon.com/images/I/71B8OOE5N8L._SY88.jpg', 'https://images-na.ssl-images-amazon.com/images/I/81SX3oAWbNL._SY88.jpg']
Serial 2912. URL: ['https://images-na.ssl-images-amazon.com/images/I/718niQ1GEwL._SY88.jpg']
Serial 2265. URL: ['https://images-na.ssl-images-amazon.com/images/I/61OboZT-kcL._SY88.jpg']
Serial 2088. URL: ['https://images-na.ssl-images-amazon.com/images/I/710a2Pyh5lL._SY88.jpg']
Serial 3474. URL: ['https://images-na.ssl-images-amazon.com/images/I/816NMd0LexL._SY88.jpg']
```
- had to implement parallel processing to speed up the downloading and image processing which might have degraded the enhancing process since the images were not downloaded in the order they were processed.
- Semantic Matching: Cosine similarity might not perfectly capture the deeper meanings and relationships between images and text.

## Potential Improvements
### Advanced Feature Extraction:
- Beyond ResNet50: Explore other pre-trained CNNs (EfficientNet, DenseNet) or domain-specific models if applicable.
- Fine-Tuning: Adapt a pre-trained model for your specific dataset.
- Object Detection: Localize objects in images for more granular feature extraction.
### Text Embeddings:
- Word Embeddings: Word2Vec, GloVe, or context-sensitive embeddings (BERT, ELMo) can capture richer semantic relationships.
- Sentence Embeddings: Encode entire reviews to overcome the limitations of TF-IDF.
### Similarity Matching:
- Beyond Cosine Similarity: Consider learned metrics or those more robust to sparsity.
### Evaluation:
- Quantitative Metrics: Calculate precision, recall, and F1 scores for performance evaluation.
- Qualitative Analysis: Examine failure cases and successful retrievals to understand strengths and weaknesses.

# Test Cases
Output For input ID: 307

Text Retrieval:
```
[Provided Text Serial: 307]: 
--------------------------------------------------
Similar Text 1 | Serial:  2301
Associated urls:  ['https://images-na.ssl-images-amazon.com/images/I/71VbqpzO7WL._SY88.jpg']
Serial Review:  I find this unit adequate, I use it with my MacBook as part of a portable 'winter' studio. I also own a Scarlet 2i2 (Gen 1)  which I use in my primary studio  I find the 2i2 has superior sound quality  less audible distortion / lower noise  and I prefer the 2i2's Neutrik style XLR/TRS output connector. The Behringer is a good value  it works fine and has good features / performance for the price  but like other Behringer products I've used, the sound quality / noise / distortion, leave me wanting a better product. If features or budget are at the top of your list, this product should do the job; if however sound quality is of primary importance then I'd recommend the Scarlet 2i2 (look for sales or a used Gen 1).
Cosine Similarity of the images (between 307 & 2301): 0.781276524066925
Cosine similarity of textual content: 0.15168247962905304
Composite Similarity Score: 0.46647950184798903
--------------------------------------------------
--------------------------------------------------
Similar Text 2 | Serial:  1778
Associated urls:  ['https://images-na.ssl-images-amazon.com/images/I/71rHP8gon9L._SY88.jpg', 'https://images-na.ssl-images-amazon.com/images/I/713OLYeyZuL._SY88.jpg', 'https://images-na.ssl-images-amazon.com/images/I/71g1wgbzcZL._SY88.jpg', 'https://images-na.ssl-images-amazon.com/images/I/81ZoTVfjk6L._SY88.jpg', 'https://images-na.ssl-images-amazon.com/images/I/71qciZl0-JL._SY88.jpg', 'https://images-na.ssl-images-amazon.com/images/I/81RmK4+yWIL._SY88.jpg']
Serial Review:  This pickup has a great, traditional, single coil strat sound. I'm really pleased with the sweet clear tone this delivers. You can make it scream with your amp setting if that's what you want. It's really great looking, too! I had no issues at all with the soldering connections, and the volume and tone pots work well as does the jack. I used this on a cigar box guitar build, and I love the tone! This homemade CBG sounds like a legitimate strat. I would definitely use this pickup again in the future, and I have no doubt it would sound good to swap out the pups on a cheapo commercial strat with these. My only complaint, and it's a small one, is that the knobs included had a tiny bit of smearing on the gold paint. It's not a big deal because many pups don't include knobs at all, and there are so many knob options available at very affordable prices. I actually used the knobs anyway, so I'm not going to knock a star off for that. The tone and looks of the pickup are fantastic at this price!
Cosine Similarity of the images (between 307 & 1778): 0.7570115923881531
Cosine similarity of textual content: 0.13745469150666684
Composite Similarity Score: 0.44723314194740993
--------------------------------------------------
--------------------------------------------------
Similar Text 3 | Serial:  1108
Associated urls:  ['https://images-na.ssl-images-amazon.com/images/I/61fS9QY4IHL._SY88.jpg']
Serial Review:  Really tough sound. Made out of plastic but it's both overdrive and distortion and everything in between.
Cosine Similarity of the images (between 307 & 1108): 0.7042622566223145
Cosine similarity of textual content: 0.136762044082603
Composite Similarity Score: 0.4205121503524587
--------------------------------------------------
```

Image Retrieval: https://images-na.ssl-images-amazon.com/images/I/71UyzJrC3DL._SY88.jpg
```
[Provided Image Serial: 307_1.jpg]:
--------------------------------------------------
Similar Image 1 | Serial :  2983_1.jpg
Associated urls:  ['https://images-na.ssl-images-amazon.com/images/I/810onrz-lPL._SY88.jpg']
Serial Review:  Worked perfect for what I needed them for!!!!
Cosine Similarity of the Images: 0.8711623549461365
Cosine similarity of text (between 307 & 2983): 0.0
Composite Similarity Score: 0.43558117747306824
--------------------------------------------------
--------------------------------------------------
Similar Image 2 | Serial :  3145_1.jpg
Associated urls:  ['https://images-na.ssl-images-amazon.com/images/I/81Eq6y34BYL._SY88.jpg']
Serial Review:  Superb feel and sound!

Tips for wah success:
- rock pedal all of the way forward
- match the volume knob to your Bass
- crank the "Q"
- love life!

Seriously, the range this pedal hits when the "Q" is amazing. I love how expressive the tone is when you get it going! I think it retains the low end and adds a creamy wah in the highs and mids. Don't listen to nay-sayers that claim you lose lows!

To put it bluntly, it's needed on your board!
I've used it with delays, octave up/downs, and overdrives, and just the straight-up clean; never found a sound I didn't like or couldn't use!

Buy it.
Cosine Similarity of the Images: 0.8703261613845825
Cosine similarity of text (between 307 & 3145): 0.05278830209764825
Composite Similarity Score: 0.4615572317411154
--------------------------------------------------
--------------------------------------------------
Similar Image 3 | Serial :  2894_1.jpg
Associated urls:  ['https://images-na.ssl-images-amazon.com/images/I/81uE5b-YDbL._SY88.jpg', 'https://images-na.ssl-images-amazon.com/images/I/81kc7eEmQ3L._SY88.jpg']
Serial Review:  Just got my pedal board yesterday!  I love it.  Before I had my pedals strewn all over the floor.  Now they're organized and easier to use.  The board is larger than I expected b/c I didn't pay attention to the measurements in the description.  But I'm glad I chose this one.  It gives me an excuse to purchase more pedals.  Obviously the stock photo shows many pedals placed really close together which is not realistic considering the cables that are involved.  I'm attaching photos of my board for better reference.  Eventually, as I add more pedals I will place the power supply under the board, but for now I like the blue illumination of the AGP power supply.

I definitely recommend this board as it is very sturdy and comes with everything you need to set it up.  I had a blast configuring my simple set up!  Rock on fellow musicians!
Cosine Similarity of the Images: 0.8681767582893372
Cosine similarity of text (between 307 & 2894): 0.027275323838441518
Composite Similarity Score: 0.44772604106388936
--------------------------------------------------
```