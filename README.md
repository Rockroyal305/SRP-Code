# This repository is for Synopsys's 2022 Science Fair.

## It is code for a program that converts english audio or text to images corresponding with that text using Google Cloud's Speech-to-Text API and OpenAI's Glide Text to Image AI. It can help to augment written or spoken communication.

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/8.0.0/mermaid.min.js"></script>
</head>

<body>
    <div class="mermaid">graph TD
        A[Input Audio File] --&gt; B[Google Speech to Text API]
        B[Google Speech to Text API] --&gt; C[List of Sentences]
        D[Input Text File] --&gt; C[List of Sentences]
        C[List of Sentences] --&gt; E[Glide Text to Image AI]
        E[Glide Text to Image AI] --&gt; F[Output Image for Each Sentence]
    </div>

</body>
<script>
    var config = {
        startOnLoad: true,
        theme: 'default',
        flowchart: {
            useMaxWidth: false,
            htmlLabels: true
        }
    };
    mermaid.initialize(config);
    window.mermaid.init(undefined, document.querySelectorAll('.language-mermaid'));
</script>

</html>
```