# SoTA T2I Adapting and Finetuning - mensa-food

## Introduction

While state-of-the-art text-to-image models excel at generating idealized images, their performance in highly specific, real-world domains remains a key challenge. This project investigates adapting Stable Diffusion v1.5 [1] to the niche visual style of German university cafeteria (Mensa) food. Our primary obstacle was the nature of the dataset itself; sourced from authentic photos, it was characterized by inconsistent lighting, poor shot angles, and non-professional composition.
Using a curated set of just 50 images, we employed Low-Rank Adaptation (LoRA) [2] to fine-tune the model, exploring the impact of 512x512 vs. 1024x1024 resolutions [3]. Our results were evaluated qualitatively in a ComfyUI workflow and quantitatively with FD, DINOv2, and dgm-eval [4] metrics. The findings definitively show that LoRA is a highly effective strategy for domain adaptation, proving that a model can successfully learn a specific and imperfect visual style from as few as 50 images to generate coherent and stylistically accurate results.


## References

- [1] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer, “High-Resolution Image Synthesis with Latent Diffusion Models,” arXiv.org, Dec. 20, 2021. https://arxiv.org/abs/2112.10752
- [2] E. J. Hu et al., “LORA: Low-Rank adaptation of Large Language Models,” arXiv.org, Jun. 17, 2021. https://arxiv.org/abs/2106.09685
- [3] Hollowstrawberry, “GitHub - hollowstrawberry/kohya-colab: Accessible Google Colab notebooks for Stable Diffusion Lora training, based on the work of kohya-ss and Linaqruf,” GitHub. https://github.com/hollowstrawberry/kohya-colab
- [4] G. Stein et al., “Exposing flaws of generative model evaluation metrics and their unfair treatment of diffusion models” Advances in Neural Information Processing Systems, vol. 36, 2023.

