import streamlit as st
from PIL import Image


# ----------------------------------------------------------------------
# Load some images into variables using PIL.Image

image_mscoco_bar = Image.open("./bar_mscoco.png")
image_mscoco_elbow = Image.open("./elbow_mscoco.png")

image_flickr30k_bar = Image.open("./bar_flickr30k.png")
image_flickr30k_elbow = Image.open("./elbow_flickr30k.png")

# ----------------------------------------------------------------------
# Create a navigation bar

navigation_page = st.sidebar.radio(
    label = "Navigation Menu",
    options = ["Home", "Data Analysis", "Run inference"],
    index = 0
)

# ----------------------------------------------------------------------

if navigation_page == "Home":
    st.title("6th Sem Mini Project, CSE")
    st.subheader("Topic")
    st.write("Image captioning using CNNs and LSTMs using PyTorch")
    st.subheader("Team members")
    st.write("1DS20CS**145** - **Aum** Patil")
    st.write("1DS20CS**157** - **Prutha** Vasisht")
    st.write("1DS20CS**165** - **Rishab** Rajesh Sharma")
    st.subheader("Working")
    st.write("**Input:** an image file (.jpg)")
    st.write("**Output:** a sentence that describes the image")

# ----------------------------------------------------------------------

elif navigation_page == "Data Analysis":
    st.title("Data Analysis")
    tab1, tab2 = st.tabs(["Flickr 30k", "MS COCO"])

    with tab1: # The tab that contains analytics for Flickr 30k dataset

        col1, col2, col3, col4 = st.columns(4) # 4 columns to highlight key facts about the dataset

        with col1:
            st.metric(
            label = "Images",
            value = "?????",
            delta = "-????",
            help = "Total number of images in dataset"
            )

        with col2:
            st.metric(
            label = "Unique words",
            value = "?????",
            delta = "-????",
            help = "Total number of unique words from all captions in the dataset"
            )

        with col3:
            st.metric(
            label = "Caption to Image",
            value = "?:?",
            delta = "-????",
            help = "Number of captions describing each image in the dataset, aka caption to image ratio"
            )
        
        with col4:
            st.metric(
            label = "Words per image",
            value = "?.???",
            delta = "-????",
            help = "Average number of unique words that describe an image in the dataset"
            )
        
        st.write("---")
        
        st.subheader("Parts of Speech")
        st.image(
            image = image_flickr30k_bar,
            caption = "Frequency distribution of tokens having various POS labels",
            width = 400
        )

        st.subheader("Semantic clustering")
        st.image(
            image = image_flickr30k_elbow,
            caption = "Clustering all unique words in dataset using KMeans, and then finding the optimal number of clusters by plotting the Elbow curve",
            width = 400
        )

    with tab2: # The tab that contains analytics for MS COCO dataset

        col1, col2, col3, col4 = st.columns(4) # 4 columns to highlight key facts about the dataset

        with col1:
            st.metric(
            label = "Images",
            value = 82783,
            delta = "????",
            help = "Total number of images in dataset"
            )

        with col2:
            st.metric(
            label = "Unique words",
            value = 85261,
            delta = "????",
            help = "Total number of unique words from all captions in the dataset"
            )

        with col3:
            st.metric(
            label = "Caption to Image",
            value = "5:1",
            delta = "????",
            help = "Number of captions describing each image in the dataset, aka caption to image ratio"
            )
        
        with col4:
            st.metric(
            label = "Words per image",
            value = "1.029",
            delta = "????",
            help = "Average number of unique words that describe an image in the dataset"
            )
        
        st.write("---")
        
        st.subheader("Parts of Speech")
        st.image(
            image = image_mscoco_bar,
            caption = "Frequency distribution of tokens having various POS labels",
            width = 400
        )

        st.subheader("Semantic clustering")
        st.image(
            image = image_mscoco_elbow,
            caption = "Clustering all unique words in dataset using KMeans, and then finding the optimal number of clusters by plotting the Elbow curve",
            width = 400
        )

# ----------------------------------------------------------------------

elif navigation_page == "Run inference":
    st.title("Model in action")
    st.write("---")
    st.metric(
        label = "BLEU",
        value = 0.276,
        delta = "Satisfactory",
        help = "Explain the meaning of BLEU score here" # pending
    )

    st.write("---")

    # pending: write code here for running inference - input a file from user and output the caption as a string inside st.write(str)

    pass