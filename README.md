# Python simple project


## Configure environment

```

conda activate project-env

conda deactivate
 
```

```

conda env create -n project-env -f ./env.yml

conda env update -n project-env -f ./env.yml

```

## Download model

```

python download_openai_community_model.py 124M

```


## Execute

```

python src/gh_ex/interactive_conditional_samples.py --model_name 774M --top_k 40 --length 256

```


## Execute

```

python src/main.ipynb

```

OR in the notebook:

```

src/main.ipynb

```





## Links

[github](https://github.com/Diegoomal)

[github_gpt2](https://github.com/openai/gpt-2)

[medium_tutorial](https://timhanewich.medium.com/running-openais-gpt-2-language-model-on-your-pc-5d5e1b9fbb8b)