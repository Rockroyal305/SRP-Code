# This repository is for Synopsys's 2022 Science Fair.

## It is code for a program that converts english audio or text to images corresponding with that text using Google Cloud's Speech-to-Text API and OpenAI's Glide Text to Image AI. It can help to augment written or spoken communication.

```mermaid
  graph TD;
      A[Input Audio File] --> B[Upload to Google Cloud Storage];
      B[Upload to Google Cloud Storage] --> C[Google Speech to Text API];
      C[Google Speech to Text API] --> D[List of Sentences];
      E[Input Text File] --> D[List of Sentences];
      D[List of Sentences] --> F[Glide Text to Image AI];
      F[Glide Text to Image AI] --> G[Output Image for Each Sentence]
```
