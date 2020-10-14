# ELI5-Generation

Based off the Reddit forum "Explain Like I'm 5," ELI5-Generation is a model for long-form question answering where this model generates simple explanations in response to a diverse array of open-ended questions using supporting documents from the web. Compared to some datasets, ELI5 often requires multi-sentence answers, but each answer should be simple enough such that it's comprehensible by a 5-year-old.

### New Avenue
We decided to pursue another avenue: using GPT-2.

In the original GPT-2 paper, the researchers outlined how it was possible to use zero-shot task transfer to use GPT-2 to auto-summarize articles. To induce summarization behavior, we concatenate the tokens from the article with a delimiter (e.g. `<summarize>`) and the summary. The resulting output will now be an abstractive summary.
![](https://miro.medium.com/max/1400/1*BTnLm7X52fI5R6CY4bO2rA.png)

Similarly, we thought it might be worthwhile testing whether feeding in the question as an article and ELI5 answers as the summary would work as an ELI5 generator.

### Explanations
> When you want machine learning to convey the meaning of a text, it can do one of two things: rephrase the information, or just show you the most important parts of the content. The first approach is called abstractive summarization, while the second is called extractive summarization.

Using GPT-2 for this solution would perform abstractive summarization, so the summaries would look very human-like but would be questionable in terms of their correctness. Since we are not extracting features from the article to summarize, it would make sense that we could abstractively generate simple explanations for a given question.

Zero-shot tasks are tasks for which there are no ground truths available. Our zero-shot task transfer will learn from the model parameters of known tasks with ground truth and correlate known tasks with zero-shot tasks.

### Meeting Notes
Refer to the Wiki: https://github.com/Skyline-9/ELI5-Generation/wiki

### Goals
- Test out GPT-2 Approach
