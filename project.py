import requests
from bs4 import BeautifulSoup
import streamlit as st

API = "FILL IN"
IMAGE_URL = "https://image.tmdb.org"

def main():

    streamlit()
# Resquests from the API for TV shows or Movies
def API_request(choice):

    if choice == "tv" or choice == "movie":
        resp_dict = 0
        count = 1
        data = []

        # Requests for TV shows
        if choice == "tv":
            response = requests.get(
                f"https://api.themoviedb.org/3/tv/popular?api_key={API}&language=en-US&page="
            )
            resp_dict = response.json()

            # Creates the TV list
            for range in resp_dict["results"]:
                img_src = image_scrape(range["id"], "tv")
                data.append(
                    {
                        "id": range["id"],
                        "title": range["name"],
                        "overview": range["overview"],
                        "img": (IMAGE_URL + img_src),
                    }
                )

        # Request for Movies
        if choice == "movie":
            response = requests.get(
                f"https://api.themoviedb.org/3/movie/popular?api_key={API}&language=en-US&page="
            )
            resp_dict = response.json()

            # Creates the movie list
            for range in resp_dict["results"]:
                img_src = image_scrape(range["id"], "movie")
                data.append(
                    {
                        "id": range["id"],
                        "title": range["title"],
                        "overview": range["overview"],
                        "img": (IMAGE_URL + img_src),
                    }
                )

        return grid(data)

    else:
        raise ValueError("Choice not compatible")


# Webscraping function, using beautifulsoup and requests.
def image_scrape(id, choice):

    if not id or not choice:
        raise ValueError("ID or choice were not given!")

    response = requests.get(f"https://www.themoviedb.org/{choice}/{id}")
    soup = BeautifulSoup(response.text, "html.parser")
    image = soup.select_one("div.poster img")["data-src"]
    return image


# The function that creates the dashbaord using streamlit
def streamlit():
    st.set_page_config(layout="wide")
    # st.title("Movie picker!" )
    st.markdown(
        "<h1 style='text-align: center;'>Entertainment Picker!</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h3 style='text-align: center;'>We help you see what's popular!</h3>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h5 style='text-align: center;'>Will it be a movie or a TV-show today?</h5>",
        unsafe_allow_html=True,
    )

    (
        col1,
        col2,
        col3,
        col4,
        col5,
        col6,
        col7,
        col8,
        col9,
        col10,
        col11,
        col12,
    ) = st.columns(12)

    with col6:
        st.button("Movies", on_click=API_request, args=("movie",))

    with col7:
        st.button("TV", on_click=API_request, args=("tv",))


# The movie/TV grid that gets selected after a choice.
def grid(data):

    col1, col2, col3, col4 = st.columns(4, gap="medium")

    with col1:
        for key in range(0, 20, 4):
            st.image(data[key]["img"])
            st.subheader(data[key]["title"])
            st.caption(data[key]["overview"])

    with col2:
        for key in range(1, 20, 4):
            st.image(data[key]["img"])
            st.subheader(data[key]["title"])
            st.caption(data[key]["overview"])

    with col3:
        for key in range(2, 20, 4):
            st.image(data[key]["img"])
            st.subheader(data[key]["title"])
            st.caption(data[key]["overview"])

    with col4:
        for key in range(3, 20, 4):
            st.image(data[key]["img"])
            st.subheader(data[key]["title"])
            st.caption(data[key]["overview"])


if __name__ == "__main__":
    main()
