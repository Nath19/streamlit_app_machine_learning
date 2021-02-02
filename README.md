# Welcome to Streamlit 👋

**The fastest way to build custom ML tools.**

Streamlit lets you create apps for your machine learning projects with deceptively simple Python scripts. It supports hot-reloading, so your app updates live as you edit and save your file. No need to mess with HTTP requests, HTML, JavaScript, etc. All you need is your favorite editor and a browser. 





## Installation

```
pip install streamlit
streamlit hello
```

## Example

Streamlit lets you build interactive apps ridiculously easily:

```
import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
```

![img](https://camo.githubusercontent.com/1e18efff3f06946e9d1559712cea0cb76364f004/68747470733a2f2f73747265616d6c69742d64656d6f2d646174612e73332d75732d776573742d322e616d617a6f6e6177732e636f6d2f737175617265642d696d6167652d666f722d6769746875622d726561646d652d322e706e67)

## A Bigger Example

Despite its simplicity Streamlit lets you build incredibly rich and powerful tools. [This demo project](https://github.com/streamlit/demo-self-driving) lets you browse the entire [Udacity self-driving-car dataset](https://github.com/udacity/self-driving-car) and run inference in real time using the [YOLO object detection net](https://pjreddie.com/darknet/yolo).



![Making-of Animation](https://raw.githubusercontent.com/streamlit/demo-self-driving/master/av_final_optimized.gif)

 

The complete demo is implemented in less than 300 lines of Python. In fact, the app contains [only 23 Streamlit calls](https://github.com/streamlit/demo-self-driving/blob/master/app.py) which illustrates all the major building blocks of Streamlit. You can try it right now with:

```
pip install --upgrade streamlit opencv-python
streamlit run https://raw.githubusercontent.com/streamlit/demo-self-driving/master/app.py
```



## More Information

 

- Our [launch post](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace)

- Our lovely [community](https://discuss.streamlit.io/)

- Streamlit [documentation](https://docs.streamlit.io/)

- More [demo projects](https://github.com/streamlit/)

- If you would like to contribute, see [instructions here](https://github.com/streamlit/streamlit/wiki/Contributing)

  
